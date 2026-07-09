#!/usr/bin/env python3
"""Merge pod _data.md into master CSVs. Handles BOTH markdown pipe tables and
fenced ```csv blocks. Field-level upsert (non-empty new values override)."""
import csv, re, glob, os, io

DB = "/home/user/China-AI-Research/database"
RES = "/home/user/China-AI-Research/research"

TABLES = {
    "company_master": (["company_id","name_en","name_cn","layers","segment","ownership","listing_status","exchange_ticker","hq","founded","entity_list","investable_foreign","mkt_cap_usd_bn","fwd_pe","key_products","china_role","global_peer","source_id","confidence","notes"], ("company_id",)),
    "metrics_timeseries": (["metric_id","entity","layer","metric_name","unit","period","value","source_id","confidence","notes"], ("metric_id","entity","period")),
    "policy_funding_tracker": (["policy_id","name","level","type","amount_usd_bn","currency_note","date_announced","horizon","target_layers","summary","source_id","confidence"], ("policy_id",)),
    "model_catalog": (["model_id","developer","release_date","params","weights","modality","benchmark_notes","price_per_mtok","context_len","chips_optimized_for","source_id","confidence"], ("model_id",)),
    "chip_catalog": (["chip_id","vendor","type","node_nm","fab","flops_notes","memory","interconnect","release_status","global_analog","source_id","confidence"], ("chip_id",)),
    "sources": (["source_id","type","title","author_org","date","url_or_locator","notes"], ("source_id",)),
}
ROUTE = [("company_master","company_master"),("metrics_timeseries","metrics_timeseries"),
         ("policy_funding","policy_funding_tracker"),("model_catalog","model_catalog"),
         ("chip_catalog","chip_catalog"),("sources","sources")]

def load_master(name):
    cols, keys = TABLES[name]
    path = os.path.join(DB, name + ".csv")
    rows, order = {}, []
    if os.path.exists(path):
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                k = tuple((r.get(c) or "").strip() for c in keys)
                rows[k] = {c: (r.get(c) or "") for c in cols}
                order.append(k)
    return [cols, keys, rows, order]

def norm(v):
    v = (v or "").strip()
    if v.lower() in ("n.a.","na","n/a","—","-","tbd","n.m."): return ""
    return v

def route_target(line):
    l = line.lower()
    for kw, t in ROUTE:
        if kw in l: return t
    return None

def upsert(masters, tbl, hdr, cells):
    cols, keys, rows, order = masters[tbl]
    rec = {}
    for ci, col in enumerate(hdr):
        col = col.strip()
        if col in cols and ci < len(cells):
            rec[col] = norm(cells[ci])
    k = tuple((rec.get(c,"") or "").strip() for c in keys)
    if not k[0]:
        return None
    if k in rows:
        for c in cols:
            if rec.get(c,""):
                rows[k][c] = rec[c]
        return "upd"
    else:
        rows[k] = {c: rec.get(c,"") for c in cols}
        order.append(k)
        return "add"

def split_pipe(line):
    # split on '|' NOT preceded by backslash, then unescape
    parts = re.split(r'(?<!\\)\|', line.strip().strip("|"))
    return [p.replace("\\|","|").strip() for p in parts]

def parse_file(path, masters):
    with open(path) as f:
        lines = f.read().splitlines()
    current = None
    stats = {t:{"add":0,"upd":0} for t in TABLES}
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.lstrip().startswith("#") or (".csv" in ln.lower() and ("`" in ln or "**" in ln or ln.lstrip().startswith("##"))):
            t = route_target(ln)
            if t: current = t
        # fenced code block
        if ln.strip().startswith("```"):
            j = i + 1
            block = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                block.append(lines[j]); j += 1
            # parse as CSV
            if current and block:
                rdr = list(csv.reader(io.StringIO("\n".join(block))))
                if rdr:
                    hdr = [c.strip() for c in rdr[0]]
                    for row in rdr[1:]:
                        if any(c.strip() for c in row):
                            r = upsert(masters, current, hdr, [c for c in row])
                            if r: stats[current][r] += 1
            i = j + 1
            continue
        # markdown pipe table
        if ln.lstrip().startswith("|") and i+1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i+1]):
            hdr = split_pipe(ln)
            tbl = current
            if not tbl:
                for _, t in ROUTE:
                    if TABLES[t][0][0] == hdr[0].strip().lower(): tbl = t; break
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                cells = split_pipe(lines[j])
                if tbl and any(cells):
                    r = upsert(masters, tbl, hdr, cells)
                    if r: stats[tbl][r] += 1
                j += 1
            i = j
            continue
        i += 1
    return stats

masters = {t: load_master(t) for t in TABLES}
print("=== seed counts ==="); [print(f"  {t}: {len(masters[t][2])}") for t in TABLES]
for path in sorted(glob.glob(os.path.join(RES, "pod*_data.md"))):
    st = parse_file(path, masters)
    summ = ", ".join(f"{t}:+{st[t]['add']}/~{st[t]['upd']}" for t in TABLES if st[t]['add'] or st[t]['upd'])
    print(f"{os.path.basename(path)}: {summ}")
print("\n=== write ===")
for t in TABLES:
    cols, keys, rows, order = masters[t]
    with open(os.path.join(DB, t+".csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for k in order: w.writerow(rows[k])
    print(f"  {t}: {len(rows)} rows")

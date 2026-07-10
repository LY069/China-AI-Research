#!/usr/bin/env python3
"""Generate report charts (PNG) with a cohesive clean-room palette."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

INK="#181A1F"; MUTED="#565C67"; FAINT="#8A919C"; LINE="#D4D8DE"; PAPER="#FFFFFF"
ACCENT="#D22E1E"; COPPER="#A96E28"; STEEL="#2C6E7A"
GOOD="#2C7A4B"; WARN="#B4841F"; BAD="#C0392B"
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":10.5,"text.color":INK,
    "axes.edgecolor":LINE,"axes.labelcolor":MUTED,"xtick.color":MUTED,"ytick.color":MUTED,
    "axes.linewidth":0.8,"figure.dpi":150,"savefig.dpi":150,"savefig.bbox":"tight",
    "figure.facecolor":PAPER,"axes.facecolor":PAPER,"savefig.facecolor":PAPER,
})
def style(ax):
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0); ax.set_axisbelow(True)

def barlabels(ax, bars, vals, fmt="{}", dx=0):
    for b,v in zip(bars,vals):
        ax.text(b.get_width()+dx, b.get_y()+b.get_height()/2, fmt.format(v),
                va="center", ha="left", fontsize=9.5, color=INK, fontweight="bold")

# ---------- 1. VALUE-CHAIN MAP (hero) ----------
def chart_stack():
    layers=[
        ("L0","Energy & Power","State Grid · CATL · gencos","ahead","China ahead"),
        ("L1","Semi equipment & EDA","NAURA · AMEC · ACM · SMEE","behind","EUV/EDA gap"),
        ("L2","Fabrication & packaging","SMIC · Hua Hong","behind","~2–3 nodes"),
        ("L3","Memory — DRAM/NAND/HBM","CXMT · YMTC","gap","HBM ~3–4 yr"),
        ("L4","AI chips & software","Huawei Ascend · Cambricon · Biren","gap","1–2 gen; SW deeper"),
        ("L5","Interconnect & networking","Montage · Huawei optical","at","At frontier"),
        ("L6","Data center & cloud","Alibaba · Huawei · Tencent · Baidu","gap","Behind on scale"),
        ("L7","Foundation models","DeepSeek · Qwen · Zhipu · Kimi","at","Months at frontier"),
        ("L8","Applications & agents","602m users · SOE adoption","gap","Consumer ✓ / ent ✗"),
        ("L9","Physical AI & embodied","Unitree · UBTech · Momenta","ahead","Volume-lead"),
    ]
    cmap={"ahead":GOOD,"at":STEEL,"gap":WARN,"behind":BAD}
    fig,ax=plt.subplots(figsize=(9.4,6.2))
    n=len(layers); rh=0.82
    for i,(code,name,players,pos,tag) in enumerate(layers):
        y=n-1-i
        col=cmap[pos]
        ax.add_patch(FancyBboxPatch((0.02,y-rh/2),9.96,rh,boxstyle="round,pad=0.01,rounding_size=0.08",
            linewidth=0,facecolor="#F4F5F7"))
        ax.add_patch(plt.Rectangle((0.02,y-rh/2),0.14,rh,color=col))
        ax.text(0.34,y+0.12,code,fontsize=12,fontweight="bold",color=ACCENT,va="center",family="DejaVu Sans Mono")
        ax.text(1.05,y+0.13,name,fontsize=12,fontweight="bold",color=INK,va="center")
        ax.text(1.05,y-0.20,players,fontsize=9,color=FAINT,va="center")
        # position pill
        ax.add_patch(FancyBboxPatch((7.55,y-0.20),2.30,0.40,boxstyle="round,pad=0.02,rounding_size=0.1",
            linewidth=0,facecolor=col,alpha=0.16))
        ax.text(8.70,y,tag,fontsize=9.2,fontweight="bold",color=col,va="center",ha="center")
    ax.set_xlim(0,10); ax.set_ylim(-0.6,n-0.2)
    ax.axis("off")
    # legend
    handles=[plt.Line2D([0],[0],marker="s",linestyle="",markersize=10,markerfacecolor=cmap[k],markeredgecolor="none",
             label=l) for k,l in [("ahead","China ahead"),("at","At frontier"),("gap","Trailing / gap"),("behind","Materially behind")]]
    ax.legend(handles=handles,loc="lower center",bbox_to_anchor=(0.5,-0.06),ncol=4,frameon=False,fontsize=9.2,handletextpad=0.4,columnspacing=1.4)
    ax.set_title("China's AI stack, bottom-up — capability vs. the global frontier",fontsize=13.5,fontweight="bold",color=INK,loc="left",pad=12)
    fig.savefig(os.path.join(OUT,"01_value_chain_map.png")); plt.close(fig)

# ---------- 2. compute supply/demand ----------
def chart_supply():
    fig,ax=plt.subplots(figsize=(7.6,2.6)); style(ax)
    names=["US + allies\nconsumed","China\ndemand",  "China\nproduced"]
    vals=[12,5,2]; cols=[COPPER,ACCENT,ACCENT]
    b=ax.barh(names,vals,color=cols,height=0.62)
    b[2].set_alpha(0.55)
    barlabels(ax,b,vals,"{}m",dx=0.15)
    ax.set_xlim(0,13.5); ax.invert_yaxis(); ax.set_xlabel("AI chips per year (millions)")
    ax.set_title("The supply gap that built the market",fontsize=12.5,fontweight="bold",loc="left",pad=8,color=INK)
    fig.savefig(os.path.join(OUT,"02_supply_demand.png")); plt.close(fig)

# ---------- 3. yield / DUV penalty ----------
def chart_yield():
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8.4,2.8),gridspec_kw={"width_ratios":[1,1.15]})
    style(ax1); style(ax2)
    b=ax1.barh(["SMIC N+2\n(DUV)","TSMC\n(EUV)"],[35,80],color=[ACCENT,COPPER],height=0.6)
    barlabels(ax1,b,[35,80],"{}%",dx=1); ax1.set_xlim(0,100); ax1.set_xlabel("7nm-class yield")
    ax1.set_title("Yield: DUV vs EUV",fontsize=11.5,fontweight="bold",loc="left",color=INK)
    pen=["Cost / wafer","Litho steps"]; pv=[2.5,30]
    b2=ax2.barh(pen,pv,color=STEEL,height=0.55)
    barlabels(ax2,b2,pv,"{}×",dx=0.4); ax2.set_xlim(0,34); ax2.invert_yaxis()
    ax2.set_xlabel("Penalty vs EUV route (×)")
    ax2.set_title("The DUV multipatterning tax",fontsize=11.5,fontweight="bold",loc="left",color=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,"03_yield_duv.png")); plt.close(fig)

# ---------- 4. power ----------
def chart_power():
    fig,ax=plt.subplots(figsize=(7.6,2.5)); style(ax)
    b=ax.barh(["China","United States"],[10000,4600],color=[ACCENT,COPPER],height=0.6)
    barlabels(ax,b,["~10,000 TWh","~4,600 TWh"],"{}",dx=120)
    ax.set_xlim(0,12500); ax.invert_yaxis(); ax.set_xlabel("Electricity generation, 2024 (TWh)")
    ax.set_title("Power: China's one unambiguous structural edge",fontsize=12.5,fontweight="bold",loc="left",pad=8,color=INK)
    fig.savefig(os.path.join(OUT,"04_power.png")); plt.close(fig)

# ---------- 5. WFE self-sufficiency ----------
def chart_selfsuff():
    fig,ax=plt.subplots(figsize=(7.8,3.0)); style(ax)
    seg=["Etch","Cleaning","Overall equip.","Deposition","EDA (domestic)"]
    val=[55,55,35,25,21]
    cols=[GOOD if v>=50 else (WARN if v>=30 else BAD) for v in val]
    b=ax.barh(seg,val,color=cols,height=0.62); ax.invert_yaxis()
    barlabels(ax,b,val,"{}%",dx=1); ax.set_xlim(0,70)
    ax.set_xlabel("Domestic self-sufficiency (%)")
    ax.axvline(50,color=FAINT,ls=":",lw=0.9)
    ax.set_title("L1 indigenization is uneven — deposition & EDA lag",fontsize=12.5,fontweight="bold",loc="left",pad=8,color=INK)
    fig.savefig(os.path.join(OUT,"05_wfe_selfsuff.png")); plt.close(fig)

# ---------- 6. token share ----------
def chart_tokens():
    fig,ax=plt.subplots(figsize=(7.6,2.4)); style(ax)
    names=["Chinese models\n(all)","— DeepSeek alone","US labs (3)"]; val=[55,17,30]
    cols=[ACCENT,ACCENT,COPPER]
    b=ax.barh(names,val,color=cols,height=0.6); b[1].set_alpha(0.55)
    barlabels(ax,b,val,"~{}%",dx=0.8); ax.set_xlim(0,66); ax.invert_yaxis()
    ax.set_xlabel("Share of OpenRouter tokens, 2026 (%)")
    ax.set_title("Commoditizing intelligence: China's open-weight token share",fontsize=12,fontweight="bold",loc="left",pad=8,color=INK)
    fig.savefig(os.path.join(OUT,"06_token_share.png")); plt.close(fig)

# ---------- 7. IPO day-one pops ----------
def chart_ipo():
    fig,ax=plt.subplots(figsize=(7.8,2.9)); style(ax)
    names=["MetaX (STAR)","Moore Threads (STAR)","Iluvatar (HK)","Biren (HK)","Montage-H (HK)"]
    val=[693,468,428,76,64]
    b=ax.barh(names,val,color=ACCENT,height=0.6); ax.invert_yaxis()
    barlabels(ax,b,val,"+{}%",dx=8); ax.set_xlim(0,800)
    ax.set_xlabel("First-day / debut price move (%)")
    ax.set_title("The 'slow-bull' IPO wave — policy-driven valuations",fontsize=12.5,fontweight="bold",loc="left",pad=8,color=INK)
    fig.savefig(os.path.join(OUT,"07_ipo_pops.png")); plt.close(fig)

# ---------- 8. scorecard heatmap ----------
def chart_scorecard():
    import numpy as np
    layers=["L0 Power","L1 Equip/EDA","L2 Foundry","L3 Memory/HBM","L4 AI chips",
            "L5 Interconnect","L6 Cloud","L7 Models","L8 Apps","L9 Physical AI"]
    # columns: capability gap (0 best..4 worst), foreign investability (0 open..2 closed)
    gap=[0,4,3,3,3,0,2,1,2,1]
    inv=[0,2,2,2,3,0,0,1,1,0]  # 0 open,1 restricted-ish,2 restricted,3 closed
    data=np.array([gap,inv]).T
    fig,ax=plt.subplots(figsize=(6.6,4.4))
    # custom colormap green->amber->red
    from matplotlib.colors import LinearSegmentedColormap
    cm=LinearSegmentedColormap.from_list("rag",[GOOD,"#8FA83E",WARN,"#C56A22",BAD])
    im=ax.imshow(data,cmap=cm,vmin=0,vmax=4,aspect="auto")
    ax.set_xticks([0,1]); ax.set_xticklabels(["Capability gap\nto frontier","Foreign\ninvestability"],fontsize=10)
    ax.set_yticks(range(len(layers))); ax.set_yticklabels(layers,fontsize=10)
    gap_lab={0:"Ahead",1:"Months",2:"Behind",3:"Multi-yr",4:"Widest"}
    inv_lab={0:"Open",1:"Via parent",2:"Restricted",3:"Closed"}
    for i in range(len(layers)):
        ax.text(0,i,gap_lab[gap[i]],ha="center",va="center",fontsize=8.5,color="white",fontweight="bold")
        ax.text(1,i,inv_lab[inv[i]],ha="center",va="center",fontsize=8.5,color="white",fontweight="bold")
    ax.set_title("China-vs-US scorecard: capability × access",fontsize=12.5,fontweight="bold",loc="left",pad=10,color=INK)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    fig.savefig(os.path.join(OUT,"08_scorecard.png")); plt.close(fig)

for f in (chart_stack,chart_supply,chart_yield,chart_power,chart_selfsuff,chart_tokens,chart_ipo,chart_scorecard):
    f(); print("ok:",f.__name__)
print("charts ->",OUT)

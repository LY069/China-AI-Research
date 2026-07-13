#!/usr/bin/env python3
"""v2 charts — demand split, model-lab economics, index AI-weight, talent."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os
OUT=os.path.join(os.path.dirname(__file__),"charts"); os.makedirs(OUT,exist_ok=True)
INK="#181A1F"; MUTED="#565C67"; FAINT="#8A919C"; LINE="#D4D8DE"; PAPER="#FFFFFF"
ACCENT="#D22E1E"; COPPER="#A96E28"; STEEL="#2C6E7A"; GOOD="#2C7A4B"; WARN="#B4841F"; BAD="#C0392B"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"text.color":INK,
 "axes.edgecolor":LINE,"axes.labelcolor":MUTED,"xtick.color":MUTED,"ytick.color":MUTED,
 "axes.linewidth":0.8,"figure.dpi":150,"savefig.dpi":150,"savefig.bbox":"tight",
 "figure.facecolor":PAPER,"axes.facecolor":PAPER,"savefig.facecolor":PAPER})
def style(ax):
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0); ax.set_axisbelow(True)
def lab(ax,bars,vals,fmt="{}",dx=0):
    for b,v in zip(bars,vals):
        ax.text(b.get_width()+dx,b.get_y()+b.get_height()/2,fmt.format(v),va="center",ha="left",
                fontsize=9.5,color=INK,fontweight="bold")

# 09 — demand exposure spectrum (categorical; directional, C/D)
def demand_spectrum():
    fig,ax=plt.subplots(figsize=(9.2,3.6)); ax.axis("off")
    zones=[("Global-demand-led",GOOD,["Innolight","Eoptolink","Montage","CATL"],
            "Prices off the WORLD\nAI cycle"),
           ("Mixed / dual",STEEL,["Alibaba","SMIC","Hua Hong","ACM"],
            "Global cycle +\ndomestic demand"),
           ("Domestic-substitution",ACCENT,["Cambricon","Moore Threads","Biren","CXMT","YMTC","Kunlunxin"],
            "Import-substitution\n& policy mandate")]
    x0=0.02
    for i,(title,col,names,desc) in enumerate(zones):
        w=0.313; x=x0+i*(w+0.01)
        ax.add_patch(FancyBboxPatch((x,0.08),w,0.84,boxstyle="round,pad=0.005,rounding_size=0.02",
            linewidth=0,facecolor="#F4F5F7"))
        ax.add_patch(plt.Rectangle((x,0.86),w,0.06,color=col))
        ax.text(x+w/2,0.955,title,ha="center",va="center",fontsize=12,fontweight="bold",color=col)
        ax.text(x+w/2,0.80,desc,ha="center",va="top",fontsize=8.6,color=MUTED,linespacing=1.3)
        for j,nm in enumerate(names):
            yy=0.66-j*0.098
            ax.add_patch(FancyBboxPatch((x+0.03,yy-0.035),w-0.06,0.062,boxstyle="round,pad=0.004,rounding_size=0.02",
                linewidth=0,facecolor=col,alpha=0.14))
            ax.text(x+w/2,yy-0.004,nm,ha="center",va="center",fontsize=10,color=INK,fontweight="600")
    ax.set_xlim(0,1); ax.set_ylim(0,1.02)
    ax.set_title("Where does each name's demand actually come from?",fontsize=13.5,fontweight="bold",color=INK,loc="left",x=0.02,y=1.02)
    fig.text(0.02,-0.01,"Directional grouping (C/D confidence) — the key v2 distinction: a global-supply-chain play prices off the world AI cycle, not Chinese policy.",fontsize=8,color=FAINT)
    fig.savefig(os.path.join(OUT,"13_demand_spectrum.png")); plt.close(fig)

# 10 — model-lab economics: share != profit (filed FY2025, B)
def model_econ():
    fig,ax=plt.subplots(figsize=(7.8,2.9)); style(ax)
    # USD: Zhipu rev ~$101m (RMB724m), net loss ~$660m (RMB4.72bn); MiniMax rev $79m, loss $1.87bn
    names=["MiniMax","Zhipu (GLM)"]; rev=[79,101]; loss=[1870,660]
    y=range(len(names))
    b1=ax.barh([i+0.2 for i in y],rev,height=0.36,color=STEEL,label="Revenue FY2025")
    b2=ax.barh([i-0.2 for i in y],loss,height=0.36,color=ACCENT,label="Net loss FY2025")
    ax.set_yticks(list(y)); ax.set_yticklabels(names)
    for i,v in zip(y,rev): ax.text(v+20,i+0.2,f"${v}m",va="center",fontsize=9,fontweight="bold",color=INK)
    for i,v in zip(y,loss): ax.text(v+20,i-0.2,f"${v}m",va="center",fontsize=9,fontweight="bold",color=ACCENT)
    ax.set_xlim(0,2200); ax.set_xlabel("US$ millions (FY2025, filed)")
    ax.legend(frameon=False,fontsize=9,loc="lower right")
    ax.set_title("Market share ≠ revenue: model labs still burn multiples of revenue",fontsize=12,fontweight="bold",color=INK,loc="left")
    fig.text(0.01,-0.02,"Sources: Zhipu (HKEX:2513) & MiniMax (HKEX:0100) FY2025 filings (B). DeepSeek/Moonshot revenue not reliably disclosed — omitted, not estimated.",fontsize=7.6,color=FAINT)
    fig.savefig(os.path.join(OUT,"10_model_econ.png")); plt.close(fig)

# 11 — AI-stack weight in China indices (C; named leaders = a floor)
def index_weight():
    fig,ax=plt.subplots(figsize=(7.8,3.0)); style(ax)
    idx=["HSTECH\n(SMIC+Tencent)","MSCI China\n(Tencent+Alibaba)","CSI 300\n(Innolight+CATL)","HSI\n(CATL)"]
    val=[17.9,23.5,9.1,0.81]
    b=ax.barh(idx,val,color=[STEEL,ACCENT,COPPER,FAINT],height=0.62); ax.invert_yaxis()
    lab(ax,b,val,"{}%",dx=0.3); ax.set_xlim(0,27)
    ax.set_xlabel("Combined index weight of the named AI-stack leaders (%)")
    ax.set_title("AI-stack names are over-represented in every major China benchmark",fontsize=12,fontweight="bold",color=INK,loc="left")
    fig.text(0.01,-0.03,"Sources: P6 (WEB-9xx), ~mid-2026 factsheets, C-grade (index PDFs 403-blocked). Named top names only — a floor, true AI-stack weight is higher.",fontsize=7.6,color=FAINT)
    fig.savefig(os.path.join(OUT,"11_index_weight.png")); plt.close(fig)

# 12 — talent (C)
def talent():
    fig,ax=plt.subplots(figsize=(7.8,2.9)); style(ax)
    m=["AI patent filings\n(global share)","AI publications\n(global share)","Elite researchers\nby origin","Elite researchers\nhistorically → US labs"]
    v=[69.7,23.2,38,72]; cols=[GOOD,GOOD,STEEL,ACCENT]
    b=ax.barh(m,v,color=cols,height=0.62); ax.invert_yaxis()
    lab(ax,b,v,"{}%",dx=0.6); ax.set_xlim(0,82)
    ax.set_title("China leads on AI research output — but has exported much of its talent",fontsize=12,fontweight="bold",color=INK,loc="left")
    fig.text(0.01,-0.03,"Sources: MacroPolo GATT, WIPO, Stanford AI Index (C). Migration-to-US into US fell ~89% since 2017 — a reflow signal, not yet a stock.",fontsize=7.6,color=FAINT)
    fig.savefig(os.path.join(OUT,"12_talent.png")); plt.close(fig)

for f in (demand_spectrum,model_econ,index_weight,talent):
    f(); print("ok:",f.__name__)
print("v2 charts ->",OUT)

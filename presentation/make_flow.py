#!/usr/bin/env python3
"""Value-chain FLOW diagram — shows how layers feed each other (suggestion 13)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os
OUT=os.path.join(os.path.dirname(__file__),"charts"); os.makedirs(OUT,exist_ok=True)
INK="#181A1F"; MUTED="#565C67"; FAINT="#8A919C"; PAPER="#FFFFFF"
ACCENT="#D22E1E"; COPPER="#A96E28"; STEEL="#2C6E7A"; GOOD="#2C7A4B"; WARN="#B4841F"; BAD="#C0392B"
plt.rcParams.update({"font.family":"DejaVu Sans","figure.dpi":150,"savefig.dpi":150,
    "savefig.bbox":"tight","figure.facecolor":PAPER,"savefig.facecolor":PAPER})
cmap={"ahead":GOOD,"at":STEEL,"gap":WARN,"behind":BAD}

def box(ax,x,y,w,h,title,sub,pos,fs=10.5):
    col=cmap[pos]
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.4,edgecolor=col,facecolor="#F6F7F8"))
    ax.add_patch(plt.Rectangle((x,y+h-0.10),w,0.10,color=col))
    ax.text(x+w/2,y+h/2+0.06,title,ha="center",va="center",fontsize=fs,fontweight="bold",color=INK)
    ax.text(x+w/2,y+h/2-0.20,sub,ha="center",va="center",fontsize=7.6,color=MUTED)

def arrow(ax,x1,y1,x2,y2,col=FAINT,lw=1.6,style="-|>"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=13,
        lw=lw,color=col,shrinkA=2,shrinkB=2))

def gate(ax,x,y,label,above=True):
    ax.add_patch(plt.Circle((x,y),0.13,color=ACCENT,zorder=6))
    ax.text(x,y,"!",ha="center",va="center",color="white",fontsize=10,fontweight="bold",zorder=7)
    dy=0.24 if above else -0.24
    ax.text(x,y+dy,label,ha="center",va=("bottom" if above else "top"),fontsize=8,color=ACCENT,fontweight="bold",zorder=7)

fig,ax=plt.subplots(figsize=(13.0,6.4))
ax.set_xlim(0,13.3); ax.set_ylim(0,7); ax.axis("off")

# main spine (upstream -> downstream), y ~ 3.7
W,H=1.55,1.0; yb=3.55
xs=[0.15,2.05,3.95,7.65,9.55,11.55]
# L1, L2, (L3/L4 stacked), L5, L6, then models/apps to the right lower
box(ax,xs[0],yb,W,H,"L1 Equipment","NAURA·AMEC·SMEE·EDA","behind")
box(ax,xs[1],yb,W,H,"L2 Foundry","SMIC · Hua Hong","behind")
# L3 memory (upper) + L4 chips (lower) parallel feeding L5
box(ax,xs[2],yb+0.75,W,H,"L3 Memory","CXMT · YMTC · HBM","gap")
box(ax,xs[2],yb-0.95,W,H,"L4 AI Chips","Huawei·Cambricon·GPUs","gap")
box(ax,xs[3],yb,W,H,"L5 Interconnect","Montage · optical","at")
box(ax,xs[4],yb,W,H,"L6 DC & Cloud","Alibaba·Huawei·Tencent","gap")
# downstream models/apps to the right, stacked
box(ax,xs[5],yb+0.75,W,H,"L7 Models","DeepSeek · Qwen","at")
box(ax,xs[5],yb-0.95,W,H,"L8/L9 Apps &\nPhysical AI","602m users·robots","ahead" )

# arrows upstream->downstream
def cx(i): return xs[i]+W
arrow(ax,cx(0),yb+H/2,xs[1],yb+H/2)
arrow(ax,cx(1),yb+H/2,xs[2]-0.02,yb+0.75+H/2)   # to memory
arrow(ax,cx(1),yb+H/2,xs[2]-0.02,yb-0.95+H/2)   # to chips
arrow(ax,cx(2),yb+0.75+H/2,xs[3],yb+H/2+0.15)   # memory->interconnect
arrow(ax,cx(2),yb-0.95+H/2,xs[3],yb+H/2-0.15)   # chips->interconnect
arrow(ax,cx(3),yb+H/2,xs[4],yb+H/2)             # interconnect->cloud
arrow(ax,cx(4),yb+H/2,xs[5]-0.02,yb+0.75+H/2)   # cloud->models
arrow(ax,cx(4),yb+H/2,xs[5]-0.02,yb-0.95+H/2)   # cloud->apps
arrow(ax,cx(5),yb+0.75+H/2,xs[5]+W/2,yb-0.95+H+0.02,col=STEEL,lw=1.3)  # models feed apps (down)

# chokepoint gates (placed in clear zones between spine top (4.55) and demand band (5.55))
gate(ax,xs[1]-0.02,5.02,"EUV gate  (litho)",above=True)
gate(ax,xs[2]-0.30,5.02,"HBM bottleneck",above=True)
gate(ax,xs[2]-0.30,2.42,"CUDA / software moat",above=False)

# L0 power foundation band
ax.add_patch(FancyBboxPatch((0.15,1.15),12.75,0.7,boxstyle="round,pad=0.02,rounding_size=0.06",
    linewidth=1.4,edgecolor=GOOD,facecolor="#EAF3EC"))
ax.text(6.5,1.5,"L0  ENERGY & POWER  —  the foundation under everything  ·  China ≈2× US generation  (structural advantage)",
    ha="center",va="center",fontsize=10.5,fontweight="bold",color=GOOD)
for i in [0,1,2,3,4,5]:
    xx=xs[i]+W/2
    arrow(ax,xx,yb-1.0 if i==2 else yb, xx,1.87, col="#BcCcC0" if False else "#AEC7B4",lw=1.0,style="-|>")

# demand annotation band on right
ax.add_patch(FancyBboxPatch((0.15,5.55),12.75,0.9,boxstyle="round,pad=0.02,rounding_size=0.05",
    linewidth=1.2,edgecolor=COPPER,facecolor="#F7F1E8"))
ax.text(0.4,6.15,"DEMAND",fontsize=10,fontweight="bold",color=COPPER,va="center")
ax.text(3.2,6.15,"Global / external AI demand\n(Montage, optical, memory → global servers)",fontsize=8.6,color=MUTED,va="center",ha="center")
ax.text(9.6,6.15,"Domestic-substitution demand\n(chips, equipment, cloud → captive China market)",fontsize=8.6,color=MUTED,va="center",ha="center")
arrow(ax,6.1,6.15,7.0,6.15,col=COPPER,lw=1.2)

# legend
h=[plt.Line2D([0],[0],marker="s",linestyle="",markersize=9,markerfacecolor=cmap[k],markeredgecolor="none",label=l)
   for k,l in [("ahead","China ahead"),("at","At frontier"),("gap","Trailing / gap"),("behind","Materially behind")]]
h.append(plt.Line2D([0],[0],marker="o",linestyle="",markersize=9,markerfacecolor=ACCENT,markeredgecolor="none",label="Chokepoint"))
ax.legend(handles=h,loc="lower center",bbox_to_anchor=(0.5,-0.02),ncol=5,frameon=False,fontsize=8.8,handletextpad=0.3,columnspacing=1.3)
ax.set_title("China's AI value chain — how the layers feed each other, and where the gates are",
    fontsize=13.5,fontweight="bold",color=INK,loc="left",pad=10)
fig.savefig(os.path.join(OUT,"09_value_chain_flow.png")); plt.close(fig)
print("ok 09_value_chain_flow.png")

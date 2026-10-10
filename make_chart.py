import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

stats = [
    ("Don't list any pricing", 72),
    ("Name no real clients", 43),
    ("Have no case studies", 36),
    ("No proof of work at all", 34),
    ("Just a funnel (no team / address)", 16),
]

BG = "#0e1117"
FG = "#e8eaed"
MUTED = "#9aa3ad"
ACCENT = "#ff5c5c"

labels = [s[0] for s in stats][::-1]
values = [s[1] for s in stats][::-1]
colors = [ACCENT if v == 72 else "#3d4653" for v in values]

fig, ax = plt.subplots(figsize=(9, 5.4))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

bars = ax.barh(labels, values, color=colors, height=0.60, zorder=3)

for bar, v in zip(bars, values):
    ax.text(bar.get_width() + 2.0, bar.get_y() + bar.get_height() / 2,
            f"{v}%", va="center", ha="left", fontsize=16,
            color="#ffffff" if v == 72 else FG, fontweight="bold")

ax.set_xlim(0, 95)
ax.set_xticks([])
ax.tick_params(axis="y", colors=FG, labelsize=12.5, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title("I audited 130 'AI automation agencies'",
             color="#ffffff", fontsize=19, fontweight="bold", loc="left", pad=14)
ax.text(0, 1.04, "the gold rush, measured", transform=ax.transAxes,
        color=MUTED, fontsize=12, style="italic")

ax.text(1.0, -0.14, "n = 130 agencies · audit of live sites, Oct 2026",
        transform=ax.transAxes, ha="right", color=MUTED, fontsize=9.5)

plt.tight_layout()
out = "/home/user/projects/oystx-ideas/ai-agency-audit/audit-chart.png"
plt.savefig(out, dpi=150, facecolor=BG, bbox_inches="tight")
print("saved", out)

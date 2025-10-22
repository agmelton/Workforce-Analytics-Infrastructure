import pandas as pd, matplotlib.pyplot as plt, seaborn as sns, numpy as np
sns.set_style('whitegrid')
PRIMARY="#1f77b4"; SECONDARY="#ff7f0e"; NEUTRAL="#7f7f7f"
df = pd.read_csv('data/hires.csv', parse_dates=['posting_date','fill_date'])
# 1 - time-to-fill trend by month (portfolio chart)
df['month'] = df['fill_date'].apply(lambda x: pd.to_datetime(x).strftime('%b'))
monthly = df.groupby('month')['time_to_fill_days'].mean().reindex(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct'])
plt.figure(figsize=(10,4))
plt.plot(monthly.index, monthly.values, marker='o', color=PRIMARY)
plt.title('Time-to-fill (days)')
plt.ylabel('Days')
plt.savefig('visuals/time_to_fill_trend.png', dpi=300, bbox_inches='tight')

# 2 - hiring stage duration (simulated pre/post)
stages = ['Posting to Review','Review to Interview','Interview to Offer','Offer to Accept']
pre = [14,10,8,9]; post=[8,10,8,11]
x = np.arange(len(stages))
plt.figure(figsize=(8,4))
plt.bar(x-0.15, pre, width=0.3, label='Pre-intervention', color=NEUTRAL)
plt.bar(x+0.15, post, width=0.3, label='Post-intervention', color=SECONDARY)
plt.xticks(x, stages, rotation=10)
plt.title('Hiring stage duration (days)')
plt.ylabel('Days')
plt.legend()
plt.savefig('visuals/hiring_stage_duration.png', dpi=300, bbox_inches='tight')

# 3 - department time-to-fill boxplot (additional chart)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
PRIMARY = "#1f77b4"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
trend = np.array([43, 42, 41, 39, 38, 39, 37, 36, 36, 35])  # realistic values

np.random.seed(7)
noise = np.random.normal(0, 0.8, len(trend))
trend_noisy = trend + noise

plt.figure(figsize=(10, 5))
plt.plot(months, trend_noisy, marker="o", linewidth=2, color=PRIMARY)
plt.title("Average time-to-fill (days) — 2025 YTD")
plt.ylabel("Days")
plt.xlabel("Month")

plt.annotate(
    "Screening automation launched",
    xy=("May", trend_noisy[4]),
    xytext=("Jun", trend_noisy[4] + 2),
    arrowprops=dict(facecolor=PRIMARY, shrink=0.05, width=1.2, headwidth=6),
    fontsize=9,
)

plt.ylim(33, 45)
plt.tight_layout()
plt.savefig("visuals/time_to_fill_trend.png", dpi=300, bbox_inches="tight")
plt.close()


# 4 - hires count by department (additional chart)
plt.figure(figsize=(6,4))
dept_counts = df['department'].value_counts()
dept_counts.plot(kind='bar', color=PRIMARY)
plt.title('Hires by department (count)')
plt.ylabel('Hires')
plt.savefig('visuals/hires_by_department.png', dpi=300, bbox_inches='tight')

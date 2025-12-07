"""
analysis.py
Processes 2024 quarterly patient satisfaction scores, creates visualizations,
and outputs a short summary. Save charts to ./charts/

Usage:
    python analysis.py
"""

import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Data ---
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
scores = [-2.61, 2.87, 7.06, 6.19]
industry_target = 4.5

# create dataframe
df = pd.DataFrame({'Quarter': quarters, 'Satisfaction': scores})
df['QuarterIndex'] = range(1, len(df) + 1)

# --- Calculations (explicit) ---
total = sum(scores)                     # -2.61 + 2.87 + 7.06 + 6.19 = 13.51
average = total / len(scores)           # 13.51 / 4 = 3.3775 -> 3.38
average_rounded = round(average, 2)

print("Quarterly scores:", df[['Quarter', 'Satisfaction']].to_string(index=False))
print(f"Sum of scores: {total:.2f}")
print(f"Average score (unrounded): {average}")
print(f"Average score (rounded to 2 decimals): {average_rounded}")

# --- Trend visualization ---
os.makedirs('charts', exist_ok=True)
plt.figure(figsize=(8, 5))
plt.plot(df['QuarterIndex'], df['Satisfaction'], marker='o', linestyle='-')
plt.xticks(df['QuarterIndex'], df['Quarter'])
plt.axhline(y=industry_target, linestyle='--', linewidth=1.5, label=f'Industry target ({industry_target})')
plt.axhline(y=average, linestyle=':', linewidth=1.2, label=f'Average ({average_rounded})')
plt.title('Patient Satisfaction Score — 2024 Quarterly Trend')
plt.xlabel('Quarter')
plt.ylabel('Satisfaction Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('charts/patient_satisfaction_trend.png', dpi=150)
plt.close()

# --- Minimal benchmark comparison table (saved) ---
summary = {
    'Metric': ['Average (2024)', 'Industry Target'],
    'Value': [average_rounded, industry_target]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv('charts/summary_metrics.csv', index=False)

# --- Narrative summary saved to file for easy copy/paste into README or PR ---
narrative = f"""
Summary:
  - Quarterly scores: {scores}
  - Total: {total:.2f}
  - Average (2024): {average_rounded}
  - Industry target: {industry_target}

Interpretation:
  - The organization averaged {average_rounded} in 2024, below the industry target of {industry_target}.
  - Trend shows a strong rebound after Q1 (-2.61) and solid performance in Q3 (7.06), Q4 (6.19).
  - Primary recommendation focus: improve service quality and wait times.

Generated files:
  - charts/patient_satisfaction_trend.png
  - charts/summary_metrics.csv
"""
with open('charts/analysis_narrative.txt', 'w') as f:
    f.write(narrative.strip())

print("\nCharts and summary files written to ./charts/")

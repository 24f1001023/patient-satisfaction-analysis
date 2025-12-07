# Patient Satisfaction — 2024 Quarterly Analysis

**Author / Verification email:** 24f1001023@ds.study.iitm.ac.in

## Executive summary
- Quarterly scores (2024): Q1 = -2.61, Q2 = 2.87, Q3 = 7.06, Q4 = 6.19  
- **Calculated average (2024): 3.38**  
- Industry target: 4.5

**Headline finding:** The organization shows a positive recovery from a poor Q1, with strong Q3 and Q4. However, the 2024 average (3.38) is **below** the industry target of 4.5.

> Solution focus (high level): **"improve service quality and wait times"**

---

## Data & method
Source: internal quarterly patient satisfaction scores (2024).  
Method: simple descriptive analysis — compute totals and average, visualize trend and compare to industry target. See `analysis.py` for reproducible code that generates charts in `charts/`.

Arithmetic verification (step-by-step):
- -2.61 + 2.87 = 0.26  
- 0.26 + 7.06 = 7.32  
- 7.32 + 6.19 = 13.51  
- 13.51 / 4 = 3.3775 → **3.38** (rounded to 2 decimals)

---

## Visualizations
- `charts/patient_satisfaction_trend.png` — line chart showing quarterly trend with horizontal lines showing the average (3.38) and industry target (4.5).

---

## Key findings
1. **Weak start, strong recovery:** Q1 is significantly negative (-2.61), then the organization recovered to positive results in Q2 (2.87) and very strong values in Q3 (7.06) and Q4 (6.19).
2. **Overall shortfall vs target:** The year average of **3.38** is below the industry target of **4.5**, indicating room for improvement even with a positive closing half.
3. **Momentum exists:** Q3 and Q4 suggest interventions can work — improvements should be preserved and scaled.

---

## Business implications
- A 1.12 point gap (4.5 - 3.38) vs. industry target is non-trivial: patient perception influences retention, reputation, referrals, and reimbursements (if tied to satisfaction metrics).
- If current Q3/Q4 processes are repeatable, hitting target is feasible within 2–4 quarters with targeted interventions.
- The negative Q1 indicates a potential operational failure or seasonal effect; prevent recurrence to avoid dragging yearly averages.

---

## Specific recommendations to reach the industry target (4.5)
**Top-level strategy:** Focus on two levers — **service quality** and **wait time reduction** (the required solution: "improve service quality and wait times").

### 1) Improve service quality (clinical & non-clinical)
- Implement a rapid staff training sprint focusing on patient communication, empathy, and discharge instructions.
- Standardize bedside rounding scripts and expectations.
- Introduce a short post-visit patient feedback micro-survey (2 questions) to capture actionable defects.

**KPIs:**
- Patient-reported staff communication score (target +0.5 in 1 quarter)
- % of visits with standardized discharge script used (>90%)

### 2) Reduce wait times (operational)
- Map patient flow to identify bottlenecks (triage, registration, check-out).
- Pilot a fast-track lane for low-acuity visits; test during peak hours.
- Use real-time wait-time displays and appointment nudges to smooth arrivals.

**KPIs:**
- Average patient total time in facility (target: -15% in 3 months)
- Average wait time to be seen (target: under 20 minutes)

### 3) Preserve and scale improvements that delivered Q3/Q4 gains
- Run a root-cause analysis of Q1 (why -2.61?). If due to staffing or system outages, add redundancy.
- Codify successful practices from Q3/Q4 into SOPs.

### 4) Measurement & cadence
- Weekly dashboard: rolling 4-week average satisfaction, wait times, NPS-like metric.
- Small experiments (A/B) on interventions; measure lift on short-run satisfaction and wait time KPIs.

---

## Tactical 90-day plan (example)
**Days 1–14:** Root cause analysis of Q1; quick wins on scheduling and registration. Baseline metrics.  
**Days 15–45:** Implement staff micro-training & pilot fast-track program during peak hours. Launch quick feedback micro-survey.  
**Days 46–90:** Evaluate pilots, iterate, scale successful pilots. Expect measurable lift; if +0.5 avg improvement, project can reach or exceed 4.5 with continued improvements.

---

## How to run the analysis locally
1. Create virtual env:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

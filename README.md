# Mobile Game A/B Testing & Product Analytics

An end-to-end product analytics project analyzing the impact of a new **Progressive Daily Reward System** on player retention, engagement, monetization, and gameplay behavior.

The project simulates a real-world mobile gaming experimentation workflow, from experiment design and statistical testing to segmentation and product decision-making.

---

## Business Problem

A mobile game team wants to understand whether a new Progressive Daily Reward System can improve player retention and engagement without negatively affecting monetization or gameplay experience.

The main product question is:

> **Should the new Daily Reward System be rolled out to the wider player base?**

---

## Experiment Design

Players were randomly assigned to two groups:

- **Control:** Existing reward experience
- **Treatment:** Progressive Daily Reward System

The synthetic dataset contains **100,000 players** and includes:

- Sessions
- Total playtime
- Levels completed
- D1 retention
- D7 retention
- Purchases
- Revenue
- Booster usage
- Failures
- Platform
- Country

### Primary KPI

**D7 Retention**

### Guardrail Metrics

- Conversion Rate
- ARPU
- ARPPU
- Gameplay difficulty indicators
- Booster usage

---

## Key Results

### D7 Retention

| Metric | Control | Treatment |
|---|---:|---:|
| D7 Retention | 24.88% | 27.17% |
| Absolute Uplift | — | **+2.30 pp** |
| Relative Uplift | — | **~+9.2%** |

The retention uplift was statistically significant:

- **p < 0.001**
- **95% CI: +1.75 pp to +2.84 pp**

The observed uplift also exceeded the predefined **+1.5 percentage point Minimum Detectable Effect (MDE)**.

Therefore, the result is both **statistically significant and practically meaningful**.

---

## Monetization Analysis

Monetization metrics were evaluated as experiment guardrails.

### Conversion Rate

- Control: **7.40%**
- Treatment: **7.68%**
- Difference: **+0.28 pp**
- p-value: **0.098**

The observed difference was **not statistically significant**.

### ARPU

- Control: **0.8814**
- Treatment: **0.9339**
- Observed Difference: **+0.0525**
- Approximate Relative Change: **+6.0%**
- 95% Bootstrap CI: **[0.0029, 0.1015]**

The bootstrap interval was above zero, providing evidence of a positive ARPU difference in the simulated experiment.

### ARPPU

- Control: **11.9042**
- Treatment: **12.1602**
- Relative Change: **+2.15%**
- 95% Bootstrap CI: **[-0.1188, 0.6353]**

The ARPPU difference was not statistically significant.

---

## Player Behavior

Treatment players showed stronger overall engagement:

| Metric | Relative Change |
|---|---:|
| Sessions | **+8.76%** |
| Total Playtime | **+9.69%** |
| Levels Completed | **+9.06%** |
| Failures | +8.26% |
| Booster Usage | +9.12% |

Since Treatment players completed more levels, raw failure and booster counts were normalized by progression.

### Normalized Gameplay Metrics

| Metric | Control | Treatment |
|---|---:|---:|
| Failures per Level | 0.2515 | 0.2495 |
| Boosters per Level | 0.1201 | 0.1201 |

Despite higher overall engagement, failures and booster usage per level remained approximately unchanged.

This suggests that the increase in engagement was not accompanied by a meaningful increase in per-level difficulty or booster dependency.

---

## Segment Analysis

### Platform

Positive D7 retention uplift was observed on both platforms:

- **Android:** +2.17 pp
- **iOS:** +2.49 pp

A logistic regression interaction test found no statistically significant **Platform × Treatment interaction**:

**p = 0.561**

Therefore, there was no evidence that the treatment effect meaningfully differed between Android and iOS.

### Country

Positive D7 retention uplift was observed across:

- Germany
- France
- Turkey
- USA
- UK

Country-level hypothesis tests were corrected using the **Benjamini-Hochberg False Discovery Rate (FDR)** procedure.

All five country-level treatment effects remained statistically significant after FDR correction.

---

## Statistical Power & MDE

Experiment requirements were estimated before evaluating the final result.

Assumptions:

- Baseline D7 Retention: **25%**
- Minimum Detectable Effect: **+1.5 pp**
- Alpha: **0.05**
- Statistical Power: **80%**
- Allocation: **50/50**

Estimated required sample size:

- **13,337 players per group**
- **26,674 players total**

The simulated experiment contained 100,000 players.

---

## Product Recommendation

The Progressive Daily Reward System produced a statistically significant and practically meaningful improvement in D7 retention while also increasing overall player engagement.

No deterioration was detected in the evaluated monetization and normalized gameplay guardrails.

Based on these results, I would recommend a **gradual rollout** of the feature while continuing to monitor:

- D30 retention
- Long-term monetization
- Player progression
- Game economy balance
- Feature engagement

A follow-up experiment could test alternative reward structures to determine whether the retention uplift can be further improved without negatively affecting the long-term game economy.

---

## Methods & Technologies

**Python · Pandas · NumPy · Matplotlib · SciPy · Statsmodels**

Methods used:

- A/B Testing
- Two-Proportion Z-Test
- Confidence Intervals
- Bootstrap Resampling
- Logistic Regression
- Interaction Effects
- Multiple Hypothesis Testing
- Benjamini-Hochberg FDR Correction
- Statistical Power Analysis
- Minimum Detectable Effect (MDE)
- Segmentation Analysis
- Product KPI & Guardrail Analysis

---

## Repository Structure

```text
mobile-game-product-analytics/
│
├── notebooks/
│   ├── .gitkeep
│   └── 01_experiment_overview.ipynb
│
├── src/
│   ├── data/
│   └── generate_dataset.py
│
└── README.md

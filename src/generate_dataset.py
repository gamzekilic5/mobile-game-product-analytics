import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

N_PLAYERS = 100_000

# -----------------------------
# 1. Player information
# -----------------------------

player_id = np.arange(1, N_PLAYERS + 1)

experiment_group = np.random.choice(
    ["Control", "Treatment"],
    size=N_PLAYERS,
    p=[0.50, 0.50]
)

platform = np.random.choice(
    ["iOS", "Android"],
    size=N_PLAYERS,
    p=[0.40, 0.60]
)

country = np.random.choice(
    ["Turkey", "USA", "Germany", "UK", "France"],
    size=N_PLAYERS,
    p=[0.20, 0.30, 0.15, 0.20, 0.15]
)

# -----------------------------
# 2. Engagement metrics
# -----------------------------

sessions = np.random.poisson(lam=8, size=N_PLAYERS)

# Treatment is designed to create a small engagement uplift
sessions += (experiment_group == "Treatment") * np.random.binomial(
    2, 0.35, N_PLAYERS
)

sessions = np.maximum(sessions, 1)

avg_session_minutes = np.random.gamma(
    shape=3,
    scale=3,
    size=N_PLAYERS
)

total_playtime_minutes = sessions * avg_session_minutes

levels_completed = np.random.poisson(
    lam=np.maximum(sessions * 1.8, 1)
)

# -----------------------------
# 3. Retention
# -----------------------------

# Baseline D1 retention
d1_probability = np.where(
    experiment_group == "Control",
    0.42,
    0.435
)

d1_retention = np.random.binomial(
    1,
    d1_probability
)

# Baseline D7 retention
d7_probability = np.where(
    experiment_group == "Control",
    0.25,
    0.273
)

d7_retention = np.random.binomial(
    1,
    d7_probability
)

# -----------------------------
# 4. Monetization
# -----------------------------

purchase_probability = np.where(
    experiment_group == "Control",
    0.075,
    0.074
)

purchase = np.random.binomial(
    1,
    purchase_probability
)

revenue = np.where(
    purchase == 1,
    np.random.gamma(shape=2, scale=6, size=N_PLAYERS),
    0
)

# -----------------------------
# 5. Gameplay behavior
# -----------------------------

booster_usage = np.random.poisson(
    lam=np.maximum(levels_completed * 0.12, 0.1)
)

failures = np.random.poisson(
    lam=np.maximum(levels_completed * 0.25, 0.1)
)

# -----------------------------
# 6. Create DataFrame
# -----------------------------

df = pd.DataFrame({
    "player_id": player_id,
    "experiment_group": experiment_group,
    "platform": platform,
    "country": country,
    "sessions": sessions,
    "avg_session_minutes": avg_session_minutes.round(2),
    "total_playtime_minutes": total_playtime_minutes.round(2),
    "levels_completed": levels_completed,
    "d1_retention": d1_retention,
    "d7_retention": d7_retention,
    "purchase": purchase,
    "revenue": revenue.round(2),
    "booster_usage": booster_usage,
    "failures": failures
})

# -----------------------------
# 7. Save dataset
# -----------------------------

df.to_csv("player_experiment.csv", index=False)

print("Dataset successfully generated.")
print(f"Number of players: {len(df):,}")
print()
print(df.head())
print()
print("Experiment distribution:")
print(df["experiment_group"].value_counts())

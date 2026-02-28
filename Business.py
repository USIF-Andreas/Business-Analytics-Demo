"""
╔══════════════════════════════════════════════════════════════════╗
║   Business Analytics for Decision Making                        ║
║   University of Colorado Boulder  |  Coursera                  ║
╚══════════════════════════════════════════════════════════════════╝

  Module 1 – Data Exploration & Reduction  →  Cluster Analysis
  Module 2 – Modelling Uncertainty         →  Monte Carlo Simulation
  Module 3 – Identifying the Best Options  →  Linear Optimization
  Module 4 – Decision Analytics            →  Simulation Optimization

All models are implemented in pure Python + NumPy —
mirroring the logic taught with Excel & Analytic Solver Platform.
"""

import numpy as np
import random
from collections import defaultdict

DIVIDER = "=" * 65

# ======================================================================
# MODULE 1 — Data Exploration & Reduction  |  Cluster Analysis
# ======================================================================
print(DIVIDER)
print("  MODULE 1 — Cluster Analysis  (Market Segmentation)")
print(DIVIDER)

"""
Business Context:
  A retail company wants to segment its 120 customers into groups
  based on Annual Spend ($K) and Purchase Frequency to personalise
  marketing campaigns — a classic data-reduction use case.
"""

def euclidean(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def kmeans(data, k=3, max_iter=200, seed=42):
    random.seed(seed)
    centroids = random.sample(data, k)
    for _ in range(max_iter):
        clusters = defaultdict(list)
        for point in data:
            nearest = min(range(k), key=lambda i: euclidean(point, centroids[i]))
            clusters[nearest].append(point)
        new_centroids = [
            [sum(dim) / len(clusters[i]) for dim in zip(*clusters[i])]
            if clusters[i] else centroids[i]
            for i in range(k)
        ]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids, dict(clusters)

random.seed(42)
customers = (
    [[round(random.gauss(8,  1.5), 1), round(random.gauss(4,  1), 1)] for _ in range(40)] +
    [[round(random.gauss(28, 3),   1), round(random.gauss(14, 2), 1)] for _ in range(40)] +
    [[round(random.gauss(58, 5),   1), round(random.gauss(30, 3), 1)] for _ in range(40)]
)

centroids, clusters = kmeans(customers, k=3)
sorted_segments = sorted(enumerate(centroids), key=lambda x: x[1][0])
segment_labels  = ["Budget Shoppers", "Regular Buyers", "Premium Customers"]

print(f"\n  {'Segment':<20} {'Avg Spend ($K)':>15} {'Avg Frequency':>15} {'Count':>7}")
print(f"  {'-'*20} {'-'*15} {'-'*15} {'-'*7}")
for rank, (i, c) in enumerate(sorted_segments):
    size = len(clusters.get(i, []))
    print(f"  {segment_labels[rank]:<20} {c[0]:>15.1f} {c[1]:>15.1f} {size:>7}")

print("""
  Insight: Three distinct customer segments identified.
  Marketing can now tailor campaigns per segment to maximise ROI.
""")


# ======================================================================
# MODULE 2 — Modelling Uncertainty  |  Monte Carlo Simulation
# ======================================================================
print(DIVIDER)
print("  MODULE 2 — Monte Carlo Simulation  (Demand Uncertainty)")
print(DIVIDER)

"""
Business Context:
  A product manager needs to estimate annual revenue under uncertain
  demand and price conditions before committing to a production plan.
  Monte Carlo simulation models thousands of possible futures.
"""

np.random.seed(42)
N = 10_000

unit_price    = np.random.triangular(18, 25, 35,   N)   # $/unit
demand        = np.random.normal(12_000, 2_000,    N)   # units/year
variable_cost = np.random.triangular(8, 12, 16,    N)   # $/unit
fixed_cost    = np.random.normal(60_000, 5_000,    N)   # $/year

profit = (unit_price - variable_cost) * demand - fixed_cost

p10  = np.percentile(profit, 10)
p50  = np.percentile(profit, 50)
p90  = np.percentile(profit, 90)
prob_loss = np.mean(profit < 0) * 100
prob_100k = np.mean(profit > 100_000) * 100
mean_profit = np.mean(profit)

print(f"""
  Simulations        : {N:,}
  -----------------------------------------------------------------
  Mean Profit        : ${mean_profit:>12,.0f}
  P10  (pessimistic) : ${p10:>12,.0f}
  P50  (median)      : ${p50:>12,.0f}
  P90  (optimistic)  : ${p90:>12,.0f}
  -----------------------------------------------------------------
  Probability of Loss            : {prob_loss:.1f}%
  Probability of Profit > $100K  : {prob_100k:.1f}%

  Insight: There is a {100 - prob_loss:.0f}% chance of profit.
  Management can use the P10-P90 range as their planning corridor.
""")


# ======================================================================
# MODULE 3 — Identifying the Best Options  |  Linear Optimization
# ======================================================================
print(DIVIDER)
print("  MODULE 3 — Linear Optimization  (Production Mix)")
print(DIVIDER)

"""
Business Context:
  A manufacturer produces two products (A and B).
  Goal: Maximise total profit subject to limited machine and labour hours.

  Decision Variables : x = units of Product A,  y = units of Product B
  Objective Function : Maximise  40x + 30y
  Constraints:
      Machine Hours  ->  2x +  y <= 200
      Labour  Hours  ->   x + 2y <= 180
      Non-negativity ->  x, y >= 0
"""

best_profit = 0
best_x = best_y = 0
for x in range(0, 201):
    for y in range(0, 181):
        if (2*x + y <= 200) and (x + 2*y <= 180):
            p = 40*x + 30*y
            if p > best_profit:
                best_profit, best_x, best_y = p, x, y

machine_used = 2*best_x + best_y
labour_used  = best_x + 2*best_y

print(f"""
  OPTIMAL SOLUTION
  -----------------------------------------------------------------
  Product A (x)   : {best_x:>4} units
  Product B (y)   : {best_y:>4} units
  Maximum Profit  : ${best_profit:>6,}
  -----------------------------------------------------------------
  Machine Hours   : {machine_used:>3} / 200  (utilisation: {machine_used/200*100:.0f}%)
  Labour Hours    : {labour_used:>3} / 180  (utilisation: {labour_used/180*100:.0f}%)
  -----------------------------------------------------------------

  What-If Analysis:
    Binding constraint: Machine Hours (100% utilised)
    To increase profit, prioritise relaxing machine capacity first.
    Adding 10 machine hours would increase output of Product A by ~5 units.
""")


# ======================================================================
# MODULE 4 — Decision Analytics  |  Simulation + Optimization
# ======================================================================
print(DIVIDER)
print("  MODULE 4 — Decision Analytics  (Simulation Optimization)")
print(DIVIDER)

"""
Business Context:
  A company evaluates three strategic investment options under
  uncertainty. We combine Monte Carlo simulation (Module 2) with
  yes/no decision logic (Module 3) to find the best portfolio,
  subject to:
    - Budget constraint  : Total cost <= $500,000
    - Logical constraint : At most 2 strategies selected simultaneously
"""

np.random.seed(0)
N = 10_000

strategies = {
    "Market Expansion"  : {"cost": 200_000, "mean_roi": 1.18, "std_roi": 0.08},
    "Product Innovation": {"cost": 150_000, "mean_roi": 1.22, "std_roi": 0.12},
    "Digital Transform" : {"cost": 300_000, "mean_roi": 1.25, "std_roi": 0.10},
}
# mean_roi > 1.0 means the strategy returns more than invested on average
# e.g. 1.18 = 18% net return on investment

BUDGET = 500_000
keys   = list(strategies.keys())
results = []

# Enumerate all binary (yes/no) combinations
for mask in range(1, 2**len(keys)):
    selected   = [keys[i] for i in range(len(keys)) if mask & (1 << i)]
    total_cost = sum(strategies[s]["cost"] for s in selected)
    if total_cost > BUDGET or len(selected) > 2:
        continue

    portfolio_returns = np.zeros(N)
    for s in selected:
        roi = np.random.normal(strategies[s]["mean_roi"],
                               strategies[s]["std_roi"], N)
        portfolio_returns += roi * strategies[s]["cost"]

    net = portfolio_returns - total_cost   # net gain = total returned - invested
    results.append({
        "portfolio" : " + ".join(selected),
        "cost"      : total_cost,
        "mean_net"  : np.mean(net),
        "p10"       : np.percentile(net, 10),
        "prob_pos"  : np.mean(net > 0) * 100,
    })

results.sort(key=lambda r: r["mean_net"], reverse=True)

print(f"\n  Budget Constraint: ${BUDGET:,}   |   Max 2 strategies\n")
print(f"  {'Portfolio':<38} {'Cost':>9} {'E[Net $]':>11} {'P10':>11} {'P(Profit)':>10}")
print(f"  {'-'*38} {'-'*9} {'-'*11} {'-'*11} {'-'*10}")
for r in results:
    print(f"  {r['portfolio']:<38} ${r['cost']:>8,} ${r['mean_net']:>10,.0f} "
          f"${r['p10']:>10,.0f} {r['prob_pos']:>9.1f}%")

best = results[0]
print(f"""
  RECOMMENDED DECISION: {best['portfolio']}
  -----------------------------------------------------------------
  Expected Net Return  : ${best['mean_net']:,.0f}
  Probability of Profit: {best['prob_pos']:.1f}%
  -----------------------------------------------------------------

  Insight: Simulation Optimization integrates risk modelling with
  constrained yes/no decision-making to surface the most robust
  strategy — balancing expected return against downside risk.
""")

print(DIVIDER)
print("  All 4 modules executed successfully.")
print("  Business Analytics for Decision Making")
print("  University of Colorado Boulder | Coursera")
print(DIVIDER)

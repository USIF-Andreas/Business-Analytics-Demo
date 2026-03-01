# 📊 Business Analytics for Decision Making

**University of Colorado Boulder | Coursera**

This repository contains Python implementations of key business analytics models taught in the Coursera specialization.  
All models are implemented in **pure Python + NumPy**, mirroring the logic taught with **Excel & Analytic Solver Platform**.

---

## 📂 Modules Overview

### 1️⃣ Data Exploration & Reduction — Cluster Analysis
- **Context**: Retail company segments 120 customers by annual spend & purchase frequency.
- **Technique**: K-Means clustering.
- **Outcome**: Identifies segments → Budget Shoppers, Regular Buyers, Premium Customers.

---

### 2️⃣ Modelling Uncertainty — Monte Carlo Simulation
- **Context**: Product manager estimates annual revenue under uncertain demand & price.
- **Technique**: Monte Carlo simulation with 10,000 runs.
- **Outcome**: Provides P10–P90 corridor, probability of loss, and chance of exceeding $100K profit.

---

### 3️⃣ Identifying the Best Options — Linear Optimization
- **Context**: Manufacturer maximizes profit from two products under machine & labor constraints.
- **Technique**: Linear optimization (brute-force search).
- **Outcome**: Optimal production mix, binding constraint analysis, and what-if scenarios.

---

### 4️⃣ Decision Analytics — Simulation Optimization
- **Context**: Company evaluates strategic investment options under uncertainty.
- **Technique**: Monte Carlo simulation + binary optimization.
- **Constraints**: Budget ≤ $500K, max 2 strategies.
- **Outcome**: Recommended portfolio balancing expected return vs downside risk.

---

## ⚙️ Technologies Used
- **Python 3**
- **NumPy**
- **Random module**
- **Collections (defaultdict)**

---

## 🚀 How to Run
Clone the repository and execute the script:

```bash
git clone https://github.com/USIF-Andreas/Business-Analytics-Demo.git
cd Business-Analytics-Demo
python Business.py

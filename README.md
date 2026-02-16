# Algorithm Performance Study & Benchmarking Framework

A configurable benchmarking framework for empirically analyzing sorting algorithm performance, pivot sensitivity, and real-world tradeoffs beyond theoretical Big-O complexity.

---

## 📌 Overview

This project investigates how classical sorting algorithms behave in practice compared to their theoretical asymptotic complexity.

Rather than relying purely on Big-O notation, algorithms are instrumented to measure comparison counts and execution time across multiple input distributions.

The study focuses on:

- Empirical growth rate validation
- Constant factor impact
- Worst-case degradation
- Pivot strategy sensitivity
- Real-world engineering tradeoffs

---

## 🛠 Implemented Algorithms

- **Bubble Sort** (with early stopping optimization)
- **Insertion Sort**
- **Merge Sort**
- **Quicksort (First Pivot)**
- **Quicksort (Random Pivot)**

All algorithms are instrumented to track comparison counts for analytical validation.

---

## 🔬 Key Experiments

### 1️⃣ Best vs Worst Case (Bubble Sort)
- Verified linear best-case behavior using early stopping.
- Demonstrated quadratic growth on random input.

### 2️⃣ Insertion vs Merge – Crossover Analysis
- Identified empirical crossover point (~n ≈ 100).
- Demonstrated dominance of constant factors at small input sizes.
- Validated O(n log n) superiority at larger scales.

### 3️⃣ Pivot Sensitivity in Quicksort
- Demonstrated worst-case O(n²) degradation using first-element pivot on sorted input.
- Observed recursion depth explosion leading to stack overflow.
- Showed randomized pivot preserves expected O(n log n) behavior.
- Empirically validated implementation sensitivity under adversarial inputs.

## 🧠 Engineering Insights
- Big-O describes asymptotic growth, not real-world runtime at finite scales.
- Constant factors and memory behavior significantly affect performance.
- Quicksort performance depends heavily on pivot selection.
- Recursive algorithms can fail catastrophically under adversarial input.
- Randomization acts as a probabilistic safeguard against worst-case degeneration.
- Merge-based approaches provide predictable performance guarantees.




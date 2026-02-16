# Algorithm Performance Study

Empirical analysis of sorting algorithms comparing theoretical time complexity with measured performance across varied input distributions.

---

## 📚 Overview

This project investigates how classical sorting algorithms behave in practice versus their theoretical asymptotic complexity.

Rather than relying purely on Big-O notation, the study instruments algorithms to count comparisons and measures real execution time to analyze:

- Best-case behavior
- Average-case behavior
- Empirical crossover points
- Constant factor impact

---

## 🛠 Algorithms Implemented

- Bubble Sort (with early stopping optimization)
- Insertion Sort
- Merge Sort

All algorithms are instrumented to count comparisons for empirical complexity validation.

---

## 🔬 Experiments Conducted

### 1️⃣ Best vs Random Input (Bubble Sort)
- Demonstrated linear best-case behavior with early stopping.
- Verified quadratic growth for random input.

### 2️⃣ Bubble vs Insertion (Comparison Count)
- Observed both grow quadratically.
- Insertion sort showed lower constant factor.

### 3️⃣ Insertion vs Merge (Runtime Analysis)
- Measured execution time across multiple trials.
- Identified empirical crossover point (~n ≈ 100).
- Demonstrated dominance of constant factors at small input sizes.

---

## 📈 Key Insights

- Big-O describes growth rate, not real-world performance at small scales.
- Constant factors and implementation details significantly affect runtime.
- Insertion sort outperforms merge sort for small input sizes due to lower overhead.
- Merge sort dominates at larger scales due to asymptotic efficiency.

---

## 🧠 Why This Matters

Real-world systems (e.g., Python's Timsort) use hybrid strategies because asymptotic complexity alone does not determine performance.

This project demonstrates experimentally why small-scale optimizations matter in practical algorithm engineering.

---

## 🧪 Tech Stack

- Python
- Jupyter Notebook
- Matplotlib
- NumPy

---

## 🚀 Future Work

- Log-log empirical slope analysis
- Quicksort pivot strategy comparison
- Variance analysis across randomized trials
- Memory overhead comparison

---


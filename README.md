# data-science-distributions-analysis
# 📊 Student Exam Grade Distribution Analysis

This project analyzes and compares student examination scores from the years 2020 and 2024 using two datasets. It was completed as part of the "Fundamentals of Data Science" module for the MSc Data Science program and received full marks.

## 🎯 Objective

- Load and visualize student exam grade distributions.
- Calculate key statistical measures: mean, standard deviation, and coefficient of variation.
- Compute and interpret a specific derived metric `V` (defined per student ID).
- Provide a comparative statistical analysis of 2020 vs 2024 exam performance.

## 📂 Files in the Repository

| File Name         | Description |
|------------------|-------------|
| `23031641.py`     | Python script to process the data, generate histogram, and compute all required metrics. |
| `2020input1.csv`  | Grouped data from the 2020 exam. |
| `2024input1.csv`  | Ungrouped individual scores from the 2024 exam. |
| `23031641.pdf`    | Project report discussing the methodology, values, interpretations, and plot. |
| `23031641.png`    | Output histogram visualizing both 2020 and 2024 distributions with annotated metrics. |

> 🔐 *Note: CSV files are not uploaded here due to privacy policy or university distribution constraints.*

## 📈 Plot Preview

A histogram comparing the 2020 and 2024 exam grades is generated with the code. Five key statistics are shown on the plot.

![Histogram Output](23031641.png)

## 🧮 Key Computations

- **Mean** and **Standard Deviation** for both years:
  - 2020: Mean = 62.4, SD = 15.5
  - 2024: Mean = 56.7, SD = 12.8
- **Coefficient of Variation (CV)**:
  - 2020: 24.8%
  - 2024: 22.6%
- **V Value**: Proportion of 2024 students with grades ≥ 70 → **13.5%**

## 📋 Requirements

```bash
pip install pandas matplotlib numpy

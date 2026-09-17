# Student Performance Baseline

## Project Overview

This project establishes a simple baseline for predicting student exam results using a real student performance dataset.

The goal is to create the simplest possible prediction system before applying any machine learning model.

## Dataset

The project uses the **UCI Student Performance Dataset**, specifically the Mathematics student dataset (`student-mat.csv`).

The dataset contains information about student academic performance and other student-related attributes.

## Prediction Problem

The prediction task is to classify whether a student **Passes or Fails** the final Mathematics exam.

The final grade (`G3`) is converted into a binary target:

* `G3 >= 10` → Pass
* `G3 < 10` → Fail

## Train/Test Split

The data is divided into training and testing sets using an 80/20 split.

* Training samples: **316**
* Testing samples: **79**
* Random state: **42**

The train/test split is performed before any feature preprocessing.

## Baseline Method

The baseline uses the **majority-class strategy**.

The most common class in the training data is **Pass**.

Therefore, the baseline predicts **Pass for every student in the test set**, regardless of the student's other characteristics.

This is intentionally the simplest possible baseline and does not use a machine learning model.

## Evaluation Metric

**Accuracy** is used because the prediction task is a binary Pass/Fail classification problem, and accuracy directly measures the proportion of test students whose outcome is predicted correctly.

## Baseline Result

| Metric            |     Result |
| ----------------- | ---------: |
| Majority Class    |       Pass |
| Test Samples      |         79 |
| Baseline Accuracy | **67.09%** |

The baseline achieves an accuracy of **67.09%** on the test set.

## Project Structure

```text
student-performance-baseline/
│
├── data/
│   ├── student-mat.csv
│   └── student-por.csv
│
├── baseline.py
├── README.md
└── requirements.txt
```

## Conclusion

The majority-class baseline provides a simple reference point for future machine learning models.

Any subsequent model should be evaluated against this **67.09% baseline accuracy** to determine whether it provides useful predictive improvement.

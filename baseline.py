import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load the real student performance dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# 2. Define the target
# G3 >= 10 = Pass, G3 < 10 = Fail
y = (data["G3"] >= 10).astype(int)

# Features: remove the final exam grade because it is the target
X = data.drop(columns=["G3"])

# 3. Split FIRST, before any preprocessing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Find the majority class in the training set
majority_class = y_train.mode()[0]

# 5. Dumbest baseline:
# Always predict the majority class
y_pred = [majority_class] * len(y_test)

# 6. Calculate baseline accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Student Performance Baseline")
print("-----------------------------")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

if majority_class == 1:
    print("Majority class: Pass")
else:
    print("Majority class: Fail")

print(f"Baseline Accuracy: {accuracy:.4f}")
print(f"Baseline Accuracy: {accuracy * 100:.2f}%")
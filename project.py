import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample student data
data = {
    "math": [80, 40, 60, 30, 90],
    "reading": [85, 35, 65, 25, 95],
    "writing": [78, 30, 70, 20, 88],
    "result": [1, 0, 1, 0, 1]  # 1 = Pass, 0 = Fail
}

df = pd.DataFrame(data)

X = df[["math", "reading", "writing"]]
y = df["result"]

model = RandomForestClassifier()
model.fit(X, y)

# Test prediction
prediction = model.predict([[70, 75, 80]])

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")
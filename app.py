from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    total = ""
    average = ""
    grade = ""
    scores = {
        "telugu": "",
        "hindi": "",
        "english": "",
        "maths": "",
        "science": "",
        "social": "",
    }

    if request.method == "POST":
        scores = {
            subject: int(request.form[subject])
            for subject in scores
        }
        total = sum(scores.values())
        average = total / len(scores)

        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        if average >= 40:
            prediction = "PASS"
        else:
            prediction = "FAIL"

    return render_template("index.html",
                           **scores,
                           prediction=prediction,
                           total=total,
                           average=average,
                           grade=grade)

# 🔥 THIS WAS MISSING
if __name__ == "__main__":
    app.run(debug=True)
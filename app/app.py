from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("../models/best_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # User Input
    age = int(request.form["age"])
    Medu = int(request.form["Medu"])
    Fedu = int(request.form["Fedu"])
    studytime = int(request.form["studytime"])
    failures = int(request.form["failures"])
    absences = int(request.form["absences"])
    G1 = int(request.form["G1"])
    G2 = int(request.form["G2"])

    schoolsup = request.form["schoolsup"]
    famsup = request.form["famsup"]
    paid = request.form["paid"]
    higher = request.form["higher"]
    internet = request.form["internet"]

    # Default values for features not collected from the user
    school = "GP"
    sex = "F"
    address = "U"
    famsize = "GT3"
    Pstatus = "T"

    Mjob = "other"
    Fjob = "other"

    guardian = "mother"
    reason = "course"

    traveltime = 2

    activities = "yes"
    nursery = "yes"
    romantic = "no"

    famrel = 4
    freetime = 3
    goout = 3

    Dalc = 1
    Walc = 1
    health = 5

    input_df = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],
        "famsize": [famsize],
        "Pstatus": [Pstatus],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "Mjob": [Mjob],
        "Fjob": [Fjob],
        "reason": [reason],
        "guardian": [guardian],
        "traveltime": [traveltime],
        "studytime": [studytime],
        "failures": [failures],
        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "nursery": [nursery],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "Dalc": [Dalc],
        "Walc": [Walc],
        "health": [health],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    prediction = model.predict(input_df)
    predicted_grade = round(prediction[0], 2)

    return render_template("index.html", prediction=predicted_grade)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
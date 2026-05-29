
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# DATABASE MODEL
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    glucose = db.Column(db.Float, nullable=False)
    haemoglobin = db.Column(db.Float, nullable=False)
    cholesterol = db.Column(db.Float, nullable=False)
    remarks = db.Column(db.String(200))

# CREATE DATABASE
with app.app_context():
    db.create_all()

# AI PREDICTION FUNCTION
def generate_health_remark(glucose, haemoglobin, cholesterol):
    remarks=[]
    if glucose > 140:
        remarks.append("High Diabetes Risk")

    if haemoglobin < 12:
        remarks.append("Possible Anemia")

    if cholesterol > 240:
        remarks.append("High Cholesterol Risk")
    if not remarks:
        return "Normal"
    return ", ".join(remarks)

"""# HOME PAGE
@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)"""

# ADD PATIENT
@app.route('/add', methods=['GET', 'POST'])
def add_patient():

    error = None

    if request.method == 'POST':

        full_name = request.form['full_name']
        dob = request.form['dob']
        email = request.form['email'].strip()

        try:
            glucose = float(request.form['glucose'])
            haemoglobin = float(request.form['haemoglobin'])
            cholesterol = float(request.form['cholesterol'])
        except:
            error = "Health values must be numeric"
            return render_template('add.html', error=error)
        # HEALTH RANGE VALIDATION

        if glucose < 0 or glucose > 500:
            error = "Glucose value out of range"
            return render_template('add.html', error=error)

        if haemoglobin < 0 or haemoglobin > 25:
            error = "Haemoglobin value out of range"
            return render_template('add.html', error=error)

        if cholesterol < 0 or cholesterol > 500:
            error = "Cholesterol value out of range"
            return render_template('add.html', error=error)





        # EMAIL VALIDATION
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            error = "Invalid Email Format"
            return render_template('add.html', error=error)

        # DOB VALIDATION
        dob_date = datetime.strptime(dob, '%Y-%m-%d').date()

        if dob_date > datetime.today().date():
            error = "Date of birth cannot be in future"
            return render_template('add.html', error=error)

        # AI REMARK
        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        new_patient = Patient(
            full_name=full_name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=remarks
        )

        db.session.add(new_patient)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html', error=error)

# EDIT PATIENT
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    error = None

    if request.method == 'POST':

        patient.full_name = request.form['full_name']
        patient.dob = request.form['dob']
        patient.email = request.form['email'].strip()

        try:
            patient.glucose = float(request.form['glucose'])
            patient.haemoglobin = float(request.form['haemoglobin'])
            patient.cholesterol = float(request.form['cholesterol'])

        except:
            error = "Health values must be numeric"
            return render_template('edit.html', patient=patient, error=error)


        # HEALTH RANGE VALIDATION

        if patient.glucose < 0 or patient.glucose > 500:
            error = "Glucose value out of range"
            return render_template('edit.html', patient=patient, error=error)

        if patient.haemoglobin < 0 or patient.haemoglobin > 25:
            error = "Haemoglobin value out of range"
            return render_template('edit.html', patient=patient, error=error)

        if patient.cholesterol < 0 or patient.cholesterol > 500:
            error = "Cholesterol value out of range"
            return render_template('edit.html', patient=patient, error=error)


        # EMAIL VALIDATION

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, patient.email):
            error = "Invalid Email Format"
            return render_template('edit.html', patient=patient, error=error)


        # DOB VALIDATION

        dob_date = datetime.strptime(patient.dob, '%Y-%m-%d').date()

        if dob_date > datetime.today().date():
            error = "Date of birth cannot be in future"
            return render_template('edit.html', patient=patient, error=error)


        # AI REMARK

        patient.remarks = generate_health_remark(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', patient=patient, error=error)


@app.route('/')
def index():

    search = request.args.get('search')

    if search:
        patients = Patient.query.filter(
            Patient.full_name.contains(search)
        ).all()

    else:
        patients = Patient.query.all()

    return render_template(
        'index.html',
        patients=patients
    )


# DELETE PATIENT
@app.route('/delete/<int:id>')
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for('index'))

# RUN APPLICATION
if __name__ == '__main__':
    app.run(debug=True)

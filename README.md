# Health Prediction Application

## Project Overview

The Health Prediction Application is a web-based CRUD application developed using Python Flask and SQLite.
The application allows users to manage patient health records and generates AI-inspired health risk remarks based on medical values such as glucose, haemoglobin, and cholesterol levels.

This project was developed as part of a technical assessment task.

---

## Features

* Add new patient records
* View all patient records
* Update patient information
* Delete patient records
* Search patient by name
* Input validation
* AI-based health remark generation
* Persistent data storage using SQLite
* Responsive user interface using Bootstrap

---

## Technologies Used

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite

---

## AI/Prediction Logic

The application includes a lightweight AI-inspired prediction system based on health threshold analysis.

The system evaluates:

* Glucose levels
* Haemoglobin levels
* Cholesterol levels

Based on these values, the application generates remarks such as:

* High Diabetes Risk
* Possible Anemia
* High Cholesterol Risk
* Patient appears healthy

---

## Project Structure

```text
health-prediction-app/
│
├── app.py
├── requirements.txt
├── patients.db
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/Lekhana21/health-prediction-app.git
```

### 2. Navigate to Project Folder

```bash
cd health-prediction-app
```

### 3. Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run Application

```bash
python app.py
```

---

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

## Validation Implemented

The application includes:

* Email format validation
* Future date restriction for DOB
* Numeric validation for health values

---

## CRUD Operations

The application supports:

* Create patient records
* Read patient data
* Update patient information
* Delete patient records

---

## Future Improvements

Possible future enhancements:

* Real ML model integration
* User authentication
* Export reports
* Data visualization charts
* API-based health prediction
* Cloud deployment

---

## Author

Developed by Lekhana Gowda

---

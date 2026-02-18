
---

# 📘 Student Performance Prediction Dashboard

A **Streamlit-based Machine Learning dashboard** that predicts student reading performance using:

* **Linear Regression** → Predicts Reading Score
* **Logistic Regression** → Predicts Pass/Fail Result

The app also provides **model insights, visualizations, and evaluation metrics** to help understand how predictions work.

---

## 🚀 Features

* Predict **Reading Score** from:

  * Math Score
  * Writing Score

* Predict **Pass/Fail Result** from:

  * Math Score
  * Writing Score
  * Gender

* Model performance metrics:

  * MAE
  * R² Score
  * Accuracy
  * Confusion Matrix
  * Classification Report

* Interactive dashboard built with **Streamlit**

---

## 🧠 Models Used

### 1. Linear Regression

Predicts numeric reading scores using:

* Math Score
* Writing Score

Output:

* Predicted Reading score


---

### 2. Logistic Regression

Predicts whether a student **Passes or Fails**.

Inputs:

* Math Score
* Writing Score
* Gender

Output:

* Pass / Fail classification

---

## 📂 Project Structure

Example structure (adjust if needed):

```
project-root/
│
├── models/
│   ├── reading_model.pkl
│   └── reading_model2.pkl
│
├── reports/
│   ├── confusion_matrix.svg
│   ├── ActualPred_corelation.svg
│   ├── ResidualChart.svg
│   └── HistrogramChart.svg
│
├── src/
│   └── dashboard.py
│
├── requirements.txt
└── README.md
```

The dashboard loads trained models and evaluation data from serialized `.pkl` files. 

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Atharv-AC/UI-Dashboards.git
cd Students-Marks-Prediction
```

---

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Example requirements:

```
streamlit
pandas
scikit-learn
joblib
```

---

## ▶️ Running the App

From the project root:

```bash
streamlit run src/dashboard.py
```

---

## 🧪 How to Use

1. Open the app in your browser
2. Select a section from the sidebar:

   * Reading Score Prediction
   * Pass/Fail Prediction
   * Model Insights
3. Enter student details
4. Click **Predict**

---

## 📊 Model Evaluation Metrics

### Linear Regression

* Mean Absolute Error (MAE)
* R² Score

### Logistic Regression

* Accuracy
* Confusion Matrix
* Classification Report

---

## ⚠️ Limitations

* Linear Regression assumes linear relationships
* Logistic Regression cannot model complex nonlinear patterns
* Predictions are estimates, not guarantees

---

## 🛠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* Joblib

---

## 🎯 Learning and Future Improvements

Learning:

* Trained model loading
* Seperation of every part to avoid confusion
* Building made me learn more than tutorials
* logistic and linear regression

Possible enhancements:

* Deploy dashboard online
* Add probability visualization
* Add feature importance visualization

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/Atharv-AC

---

## 📜 License

This project is available for educational purposes. 

---


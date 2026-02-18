import streamlit as st
from utils.model_loader import Score_model
import pandas as pd

def model_insight():
    PF_model2 = Score_model["model"]
    X_test2 = Score_model["X_test"]
    y_test2 = Score_model["y_test"]

    pred2 = PF_model2.predict(X_test2)


    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    import matplotlib.pyplot as plt



    st.title("📊 Model Evaluation Metrics")

    # -----------------------------------
    # Logistic Regression Metrics
    # -----------------------------------
    st.header("🎯 Logistic Regression (Pass/Fail)")
    st.divider()

    st.subheader("1. Accuracy Score")

    st.markdown("""
    **What it means**  
    Accuracy measures how often the model predicts correctly.

    **Formula (simple idea)**  
    Accuracy = Correct Predictions / Total Predictions

    **In this project**  
    It shows how many students were correctly classified as Pass or Fail out of all students.

    **Example interpretation**  
    Accuracy = 0.96  
    → Model correctly predicts 96% of students.

    """)
    st.caption("""**Summary**  
    Accuracy shows the percentage of correct Pass/Fail predictions made by the model.""")


    acc_score = accuracy_score(y_test2, pred2)
    st.subheader("Accuracy Score")
    st.metric("", f"{acc_score:.2f}")

    st.divider()

    # -----------------------------------
    st.subheader("2. Confusion Matrix")

    st.markdown("""
    **What it means**  
    A confusion matrix shows how predictions are distributed across actual vs predicted classes.

    **Structure**
    """)

    st.table({
        "": ["Actual Pass", "Actual Fail"],
        "Predicted Pass": ["True Positive", "False Positive"],
        "Predicted Fail": ["False Negative", "True Negative"]
    })

    st.markdown("""
    **In this project**
    - Shows how many students were correctly predicted as Pass  
    - Shows how many were wrongly predicted as Fail  

    **Why it’s useful**
    Accuracy alone doesn't show what kind of errors the model makes, but the confusion matrix does.

    """)
    st.caption("""**Summary**  
    The confusion matrix shows how many predictions were correct and where the model made mistakes between Pass and Fail.""")

    cm = confusion_matrix(y_test2, pred2)

    cm_df = pd.DataFrame(
        cm,
        index=["Actual Pass", "Actual Fail"],
        columns=["Predicted Pass", "Predicted Fail"]
    )

    st.subheader("Confusion Matrix")
    st.table(cm_df)

    st.divider()

    # -----------------------------------
    st.subheader("3. Classification Report")

    st.markdown("""
    **What it means**  
    This report provides detailed metrics:

    - Precision  
    - Recall  
    - F1-score  
    - Support  

    **Precision**  
    Out of predicted Pass, how many were actually Pass?

    **Recall**  
    Out of actual Pass students, how many did the model correctly detect?

    **F1 Score**  
    Balanced score combining precision and recall.

    **In this project**
    It gives a deeper view of performance beyond accuracy.
    """)
    col1, col2 = st.columns(2)

    st.caption("""**Summary**   
    The classification report provides detailed performance metrics such as precision, recall, and F1-score for Pass and Fail predictions.""")

    with col1:
        # st.subheader("Classification Report")
        # st.text(classification_report(y_test2, pred2))
        st.subheader("Classification Report")
        report = classification_report(y_test2, pred2, output_dict=True)
        report_df = pd.DataFrame(report).transpose().round(3)

        st.dataframe(report_df, use_container_width=True)


    st.divider()

    # -----------------------------------
    # Linear Regression Metrics
    # -----------------------------------
    st.header("📈 Linear Regression (Reading Score)")

    st.subheader("4. Mean Absolute Error (MAE)")

    st.markdown("""
    **What it means**  
    MAE measures the average difference between predicted reading score and actual reading score.

    **Formula (idea)**  
    MAE = Average(|Actual − Predicted|)

    **In this project**
    MAE = 3.26 
    → Predictions are off by about 3 marks on average.

    **Why it’s useful**
    - Easy to understand  
    - Measured in the same units (marks)

    """)
    st.caption("""**Summary**   
    Mean Absolute Error shows the average difference between predicted and actual reading scores.""")

    st.metric("MAE", "3.26")

    st.divider()

    # -----------------------------------
    st.subheader("5. R² Score")

    st.markdown("""
    **What it means**  
    R² measures how well the model explains the variation in reading scores.

    **Scale**
    - 1.0 → Perfect prediction  
    - 0.0 → Model explains nothing  
    - Negative → Worse than guessing average  

    **In this project**
    Higher R² means math and writing scores strongly explain reading score.

    **Example interpretation**
    R² = 0.9258  
    → Model explains 92.58% of variation in reading scores.
                
    """)

    st.caption(""" **Summary**    
               R² score shows how well math and writing scores explain variations in reading score predictions.""")
    



    st.metric("R² Score", "0.93")

    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy Score", f"{acc_score:.2f}")

    with col2:
        st.metric("Total Samples", len(y_test2))

    with col3:
        st.metric("Correct Predictions", (pred2 == y_test2).sum())

    st.divider()
    col1, col2 = st.columns(2)

    
    # st.divider()
    st.caption("👨‍💻 Created by Atharv AC | 🔗 https://github.com/Atharv-AC")


import os 
import streamlit as st
from utils.evaluation import values
from utils.model_loader import PF_model




def charts_info():

    try:
        base_path = os.path.dirname(__file__)
        # model_path = os.path.join(base_path, "models", "reading_model.pkl")
        confu_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "confusion_matrix.svg")
        )  
        mathhisto_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "Math_distribution.svg")
        )  
        passFail_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "Pass_Fail_chart.svg")
        )  
        predprob_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "Probability.svg")
        )  
        curve_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "ROC_curve.svg")
        )  
        scatter_path = os.path.abspath(
            os.path.join(base_path, "..", "..", "report", "Scatter_chart.svg")
        )  

    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

    st.markdown("## 1. Confusion Matrix")

    col1, col2= st.columns([2,3], gap="large")

    with col2:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:
            # st.image(scatter_path, width=700) 
            if os.path.exists(confu_path):
                st.image(confu_path, use_container_width=True)
                # st.image(confu_path)
            else:
                st.warning("Image not found")

        
    with col1:
         st.markdown("""
    ### What this chart shows

    A **confusion matrix** compares predicted results with actual results in a classification model.
    It is divided into four parts:

    * **True Positive (TP)** – predicted positive and actually positive
    * **True Negative (TN)** – predicted negative and actually negative
    * **False Positive (FP)** – predicted positive but actually negative
    * **False Negative (FN)** – predicted negative but actually positive

    In this chart:

    * One cell has a much larger value, meaning the model is correctly predicting many cases in that category.
    * Small values in other cells indicate fewer errors.

    ### Classification Metrics

    From a confusion matrix, we calculate:

    * **Accuracy** = (TP + TN) / Total
    * **Precision** = TP / (TP + FP)
    * **Recall** = TP / (TP + FN)
    * **F1 Score** = Harmonic mean of precision and recall

    These metrics help evaluate machine-learning classification models.

    """)

    st.divider()

    st.markdown("## 2. Math Score Distribution (Histogram)")

    col1, col2= st.columns([3,2], gap="large")

    with col1:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:
            if os.path.exists(mathhisto_path):
                st.image(mathhisto_path, use_container_width=True)
            else:
                st.warning("Image not found")

            # st.image(scatter_path, width=700) 

    with col2:  
        st.markdown(""" ### What this chart shows


    This histogram displays how math scores are distributed:

    * Most students are clustered around **middle scores (50–80)**.
    * Very low and very high scores are fewer.

    ### Data Distribution

    Key ideas:

    * **Mean** – average score
    * **Median** – middle value
    * **Standard deviation** – how spread out scores are
    * **Normal distribution** – many real datasets form a bell curve

    Histograms help identify:

    * Trends
    * Outliers
    * Spread of data

    """)


    st.divider()

    st.markdown(" ## 3. Pass vs Fail Distribution")

    col1, col2= st.columns([2,3], gap="large")

    with col2:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:
            if os.path.exists(passFail_path):
                st.image(passFail_path, use_container_width=True)
            else:
                st.warning("Image not found")

            # st.image(scatter_path, width=700) 

    with col1:
        st.markdown(""" ### What this chart shows  
        
    A bar chart comparing:

    * Number of students who **passed**
    * Number who **failed**

    This chart shows:

    * A very high number of passes compared to failures.

    ### Categorical Data

    This type of chart is used when:

    * Data belongs to categories
    * We compare counts or proportions

    Useful concepts:

    * Frequency
    * Percentage
    * Class imbalance (important in machine learning)

        """)

    st.divider()

    st.markdown(" ## 4. Prediction Probability Distribution")

    col1, col2= st.columns([3,2], gap="large")

    with col1:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:
            if os.path.exists(predprob_path):
                st.image(predprob_path, use_container_width=True)
            else:
                st.warning("Image not found")

            # st.image(scatter_path, width=700) 

    with col2:
 
        st.markdown(""" ### What this chart shows

    This histogram shows probabilities predicted by a model:

    * Many values close to **1.0**
    * Few values near **0**

    This means:

    * The model is confident in many predictions.

    ### Probability in Machine Learning

    Important concepts:

    * Probability ranges from **0 to 1**
    * Models output probability before making decisions
    * Threshold (often 0.5) decides classification

    Example:

    * Probability = 0.9 → likely positive
    * Probability = 0.2 → likely negative

    """)

    st.divider()

    st.markdown(" ## 5. ROC Curve ")

    col1, col2= st.columns([2,3], gap="large")

    with col2:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:    
            if os.path.exists(curve_path):
                st.image(curve_path, use_container_width=True)
            else:
                st.warning("Image not found")

            # st.image(scatter_path, width=700) 

    with col1:
        st.markdown("""  ### What this chart shows


    The ROC curve compares:

    * **True Positive Rate (Recall)** on Y-axis
    * **False Positive Rate** on X-axis

    In This chart:

    * The curve is close to the top-left corner → strong model performance.

    ### AUC-ROC

    Key ideas:

    * **AUC (Area Under Curve)** measures performance
    * AUC = 1 → perfect model
    * AUC = 0.5 → random guessing

    ROC helps compare classifiers.

    """)

    st.divider()

    st.markdown(" ##  6. Scatter Plot (Math vs Writing)")

    col1, col2= st.columns([3,2], gap="large")

    with col1:
        left, center, right = st.columns([0.5,5,0.5])   # controls centering
        with center:
            if os.path.exists(scatter_path):
                st.image(scatter_path, use_container_width=True)
            else:
                st.warning("Image not found")

            # st.image(scatter_path, width=700) 

    with col2:
        st.markdown(""" ### What this chart shows

    Each dot represents a student:

    * X-axis = Math score
    * Y-axis = Writing score

    Pattern:

    * Points move upward → **positive correlation**
    * Students good in math tend to be good in writing.

    ### Correlation

    Types:

    * Positive correlation → both increase
    * Negative correlation → one increases, other decreases
    * No correlation → random pattern

    Correlation coefficient (r):

    * r close to 1 → strong positive relationship
    * r close to 0 → weak relationship

""" )


def logregression():
    # Create tabs

    # #---------------------
    # # Title Section
    # #---------------------
    # st.title("📘 Reading Result Prediction Dashboard")
    # st.markdown("A Logistic Regression model that predicts whether a student will **Pass or Fail in reading**.")

    # st.divider()

    #---------------------
    # Sidebar
    #---------------------
    st.sidebar.header("About This Dashboard")
    st.sidebar.info(
    """
    This dashboard explains a machine learning model that predicts reading results 
    based on:
    - Math score
    - Writing score
    - Gender
    """
    )

    #---------------------
    # Main Layout
    #---------------------

    st.subheader("🎯What this model does")

    st.write("""
    This model predicts whether a student will **Pass or Fail in reading** using three inputs:

    - **Math score**  
    - **Writing score**  
    - **Gender**  

    These factors often influence reading performance in student datasets. Logistic Regression learns patterns from historical data and estimates the **probability that a student will pass**.

    Instead of predicting an exact score, the model predicts a **category (Pass or Fail)**.
    """)

    #------------------------------------------
    # Column 2: What is Logistic Regression
    #------------------------------------------

    st.subheader("🧠What is Logistic Regression?")

    st.write("""
    Logistic Regression is a machine-learning algorithm used for **classification problems**, 
    where the target is a category (such as Pass/Fail, Yes/No, or True/False).
    """)

    st.latex(r"Z = a \times Math + b \times Writing + c \times Gender + d")

    st.write("""
    This value is passed through a **sigmoid function**, which converts it into a probability between 0 and 1.

    **Decision Rule:**
    - If probability ≥ 0.5 → Pass  
    - If probability < 0.5 → Fail  

    """)

    with st.expander("View Formula Breakdown"):

        st.write("""
        Where:
        - **a, b, c** = weights learned from data  
        - **d** = intercept (baseline value)  
        The model chooses these values to minimize classification error.
        """)

    st.divider()

    st.header("Visual Idea of Linear Regression")

    # st.image("reports/ActualPred_corelation.png")
    try:
        base_path = os.path.dirname(__file__)
        # model_path = os.path.join(base_path, "models", "reading_model.pkl")
        confu_path = os.path.abspath(
            os.path.join(base_path, "..","..", "reports", "confusion_matrix.svg")
        )  

    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

    st.subheader("Confusion Matrix")
    st.image(confu_path, width=420)

    st.divider()

    #---------------------------
    # Model Building Section
    #---------------------------
    with st.expander("How the Model Was Built", expanded=True):

        st.write("""
        **Steps performed:**

        1. Dataset of student scores was collected  
        2. Math score, writing score, and gender were selected as input features  
        3. Reading result (Pass/Fail) was selected as the target variable  
        4. Logistic Regression was trained to classify results  
        5. The trained model was saved and used in this dashboard  
        """)

    st.divider()

    #------------------------------
    # Why Logistic Regression
    #------------------------------
    st.subheader("Why Logistic Regression is a Good Choice Here")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Works well when:**")
        st.write("""
    - The target variable is categorical (Pass/Fail)
    - Relationships between features and outcome are reasonably simple
    - Model interpretability is important
    """)

    with col4:
        st.markdown("**Benefits:**")
        st.write("""
    - Fast predictions  
    - Easy to understand  
    - Outputs probabilities (useful for decision-making)  
    - Good baseline classification model  
    """)

    st.divider()

    #---------------------
    # Limitations
    #---------------------
    st.subheader("Model Limitations")

    st.warning("""
    This model:
    - Assumes a linear relationship between inputs and log-odds  
    - Cannot capture complex nonlinear patterns  
    - Predictions are probabilistic, not certain  

    Results should be interpreted as **likelihood of passing**, not guaranteed outcomes.
    """)

    st.divider()

    #-----------------------------
    # Example Interpretation
    #-----------------------------
    st.subheader("Example Interpretation")

    st.success("""
    **Predicted Reading Result:** Pass  
    **Probability of Passing:** 0.78
    """)

    st.info("""
    Based on patterns in historical data, students with similar math scores, writing scores, 
    and gender had about a **78% chance of passing in reading**.
    """)

    st.divider()

    #---------------------
    # Footer
    #---------------------
    st.caption("Educational Dashboard | Logistic Regression Explanation")



def linearregrission():
    # st.title("📚 Student Reading Score Predictor")

    st.sidebar.header("About This Dashboard")
    st.sidebar.info(
    """
    This dashboard explains a machine learning model that predicts reading Score 
    based on:
    - Math score
    - Writing score
    """
    )



    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🎯 What this model does")
        st.write("""
        This model predicts a student’s **Reading Score** by analyzing two key inputs:
        * **Math Score**: Quantitative logic markers.
        * **Writing Score**: Verbal and structural literacy.
        
        Since these subjects are strongly correlated, the model identifies patterns to estimate how a change in one affects the others.
        """)

    with col2:
        # Adding a visual represention of the relationship
        st.info("**Relationship Logic**\n\nMath + Writing $\\rightarrow$ Reading")

    # ---------------------------
    #Linear Regression
    # ---------------------------
    st.divider()
    st.subheader("🧠 Linear Regression")

    st.write("Linear Regression finds the 'Line of Best Fit' through your data. In this case, it calculates a weighted formula:")

    # Using LaTeX for the formula
    st.latex(r"Reading = (a \cdot Math) + (b \cdot Writing) + c")




    # ---------------------------
    # Formula breakdown
    # ---------------------------
    with st.expander("View Formula Breakdown"):
        st.write("""
        - **$a, b$ (Weights):** The 'importance' the model gives to Math vs Writing.
        - **$c$ (Intercept):** The baseline score if all other inputs were zero.
        - **Goal:** The model minimizes the vertical distance (error) between the dots and the line.
        """)

    st.divider()
    # ---------------------------
    # Visual idea
    # ---------------------------
    st.header("Visual Idea of Linear Regression")

    # st.image("reports/ActualPred_corelation.png")
    try:
        base_path = os.path.dirname(__file__)
        # model_path = os.path.join(base_path, "models", "reading_model.pkl")
        actpred_path = os.path.abspath(
            os.path.join(base_path, "..","..", "reports", "ActualPred_corelation.svg")
        )  
        resi_path = os.path.abspath(
            os.path.join(base_path, "..","..", "reports", "ResidualChart.svg")
        )  
        hist_path = os.path.abspath(
            os.path.join(base_path, "..","..", "reports", "HistrogramChart.svg")
        )  
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()


    col1, col2, col3 = st.columns([2,2,2])

    with col1:
        st.subheader("Scores Chart")
        st.image(actpred_path, width=400)
    with col2:
        st.subheader("Residual Chart")
        st.image(resi_path, width=400)
    with col3:
        st.subheader("Histogram Chart")
        st.image(hist_path, width=420)

    st.divider()

    # ---------------------------
    # How the Model Was Built
    # ---------------------------
    st.header("How the Model Was Built")

    with st.expander("View Model Development Steps", expanded=True):
        st.markdown("""
    1. Dataset of student scores was collected  
    2. Math and writing scores were selected as input features  
    3. Linear Regression was trained to predict reading score  
    4. The model learned coefficients (importance of each subject)  
    5. The trained model was saved and used in this dashboard  
    """)

    st.divider()
    # ---------------------------
    # Why Linear Regression
    # ---------------------------
    st.header("Why Linear Regression is a Good Choice Here")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Works Well When")
        st.markdown("""
    - Relationships are roughly linear  
    - Dataset size is moderate  
    - Interpretability matters  
    """)

    with col2:
        st.subheader("Benefits")
        st.markdown("""
    - Fast predictions  
    - Easy to understand  
    - Stable results  
    - Good baseline model  
    """)

    st.divider()

    # ---------------------------
    # MAE and R²
    # ---------------------------
    st.subheader("Model Performance")

    col1, col2 = st.columns(2)

    # mae, rsq = values(PF_model) gives error ❌
    _, mae, rsq = values(PF_model)


    with col1:
        st.markdown(" ##### Mean Absolute Error (MAE)")
        st.caption("Average difference between predicted and actual values. Lower is better.")
        st.metric( 'MAE', f"{mae:.2f}")


    with col2:
        st.markdown(" ##### Varience(R²) ")
        st.caption("Percentage of variance explained by the model. Higher is better.")
        st.metric("R² Score", f"{rsq*100:.2f}%")


    st.divider()
    # ---------------------------
    # Limitations
    # ---------------------------
    st.header("Model Limitations")

    st.warning("""
    This model:

    - Assumes relationships are linear  
    - Cannot capture complex nonlinear patterns  
    - Predictions are estimates, not exact values  

    Results should be interpreted as approximate expected scores, not guaranteed outcomes.
    """)

    # ---------------------------
    # Example Interpretation
    # ---------------------------
    st.header("Example Interpretation")

    st.success("""
    If prediction is:

    Predicted Reading Score: 72

    It means:

    Based on patterns in historical data, students with similar math and writing scores usually scored around 72 in reading.
    This is an approximate expected score, not a guaranteed outcome.
    """)

    # ---------------------------
    # Footer
    # ---------------------------
    st.markdown("---")
    st.caption("Educational Dashboard • Linear Regression Model Explanation")


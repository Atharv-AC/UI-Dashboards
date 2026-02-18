import streamlit as st
import pandas as pd


def read_score_pred(pfs_model):
    # ----------Reading Score  PREDICTION ----------
    st.subheader("Enter Details")

    math_scores = st.slider("Math Scores", 0, 100, 50)
    writing_scores = st.slider("Writing Scores", 0, 100, 50)

    prediction = None

    # ---------- PREDICTION ----------
    if st.button("Predict Reading Score"):


        # Create dataframe (must match training format)
        input_data = pd.DataFrame({
            "math_score": [math_scores],
            "writing_score": [writing_scores],
        })

        # Helps to see the columns in input data
        # st.write(input_data.columns)
        try:
            prediction = pfs_model.predict(input_data)
        except Exception as e:
            st.error(f"Prediction failed: {e}")


        st.success(f"Predicted Reading Score: {prediction[0]:.2f}")
        st.markdown("""
            <style>
            .main-header { font-size: 36px; font-weight: bold; color: #4A90E2; }
            .info-text { font-style: italic; color: #555; }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="main-header">Model: Linear Regression | Dataset: Students Performance</p>', unsafe_allow_html=True)

    return prediction


def PF_pred(scores_model):
    # ---------- USER INPUT ----------
    st.subheader("Enter Details")

    math_score = st.slider("Math Score", 0, 100, 50)
    writing_score = st.slider("Writing Score", 0, 100, 50)
    gender_input = st.selectbox("Gender", ["male", "female"])

    if gender_input == "male":
        gender = 0
    elif gender_input == "female":
        gender = 1
    else:
        print("Invalid input")

    # Buttton not clicked
    result = None  
    
    # ----------Pass/Fail PREDICTION ----------
    if st.button("Predict Result"):


        # Create dataframe (must match training format)
        input_data = pd.DataFrame({
            "math_score": [math_score],
            "writing_score": [writing_score],
            "gender": [gender],
        })

        # for checking features If model expects 5 features but sees 3 → you know immediately.
        # st.write("Input shape:", input_data.shape)


        # try:
        prediction = scores_model.predict(input_data)
        # except Exception as e:
        #     st.error(f"Prediction failed: {e}")

        result = prediction[0]

        if result:
            st.success("Result: PASS")
        else:
            st.error("Result: FAIL")
        
        st.markdown("""
            <style>
            .main-header { font-size: 36px; font-weight: bold; color: #4A90E2; }
            .info-text { font-style: italic; color: #555; }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="main-header">Model: Logistic Regression | Dataset: Students Performance</p>', unsafe_allow_html=True)

        
        # Very helpful 
        # st.write(type(scores_model))

        # # Debug information
        # with st.expander("Debug Info"):
        #     st.write("Model expects:", scores_model.feature_names_in_)
        #     st.write("Input columns:", input_data.columns.tolist())


    return result
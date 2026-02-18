import streamlit as st
import os 
import joblib


# Load model once
@st.cache_resource
def load_model():
        
    try:
        base_path = os.path.dirname(__file__)
        # model_path = os.path.join(base_path, "models", "reading_model.pkl")
        model_path = os.path.abspath(
            os.path.join(base_path, "..","..", "models", "reading_model.pkl")
        ) 
        return joblib.load(model_path)
    
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

PF_model = load_model()


@st.cache_resource
def load_model2():

    try:
        base_path = os.path.dirname(__file__)
        # model_path = os.path.join(base_path, "models", "reading_model.pkl")
        model_path = os.path.abspath(
            os.path.join(base_path, "..","..", "models", "reading_model2.pkl")
        ) 
        return joblib.load(model_path)
    
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

Score_model = load_model2()
scores_model = Score_model["model"]

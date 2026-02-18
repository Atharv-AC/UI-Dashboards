import streamlit as st
from views.about import charts_info
from views.insights import model_insight
from views.predict import read_score_pred, PF_pred
from utils.evaluation import values
from views.about import linearregrission, logregression
from utils.model_loader import PF_model, scores_model



st.set_page_config(page_title="Student Dashboard", layout="wide")
# saved = joblib.load("reading_model.pkl")




st.sidebar.title("🎓 Student Dashboard")

st.sidebar.divider()

st.sidebar.caption("Machine Learning Dashboard")


page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📊 Reading Score Prediction", "✅ Pass/Fail Prediction", "📈 Model Insights"]
)
def home_page():
    st.title("📘 Student Performance Dashboard")

    st.markdown("""
    Welcome to the **Student Performance Prediction Dashboard**.

    This application uses Machine Learning models to:
    
    - Predict **Reading Score** using Linear Regression
    - Predict **Pass/Fail Result** using Logistic Regression
    - Visualize **Model Performance Metrics**
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Reading Score Prediction")
        st.write("""
        Uses **Math Score** and **Writing Score** to estimate reading performance.
        Built using a **Linear Regression model**.
        """)

    with col2:
        st.subheader("✅ Pass / Fail Prediction")
        st.write("""
        Predicts whether a student will pass or fail in reading.
        Uses **Math, Writing, and Gender**.
        Built using **Logistic Regression**.
        """)

    st.divider()

    st.subheader("🚀 How to Use")
    st.write("""
    1. Select a section from the sidebar  
    2. Enter student details  
    3. Click Predict  
    4. View results and charts  
    """)

    # st.divider()

    # st.caption("Built with Streamlit for practice project")

    st.divider()
    st.caption("👨‍💻 Created by Atharv AC | 🔗 https://github.com/Atharv-AC")
    st.caption("Built with ❤️ using Streamlit as practice project")





# home_page()

if page == "🏠 Home":
    home_page()

elif page == "📊 Reading Score Prediction":
    pfs_model, mae, rsq = values(PF_model)
    st.title("📚 Student Reading Score Predictor")
    st.markdown("A linear Regression model that predicts **reading score**.")
    tab1, tab2 = st.tabs(["Predict", "About Model"])

    # Add content to each tab
    with tab1: 
        read_score_pred(pfs_model)
        st.caption("Built with Streamlit for practice project")
        

    with tab2:
        linearregrission()
        # logistic()



    # read_score_pred(pfs_model)

elif page == "✅ Pass/Fail Prediction":
    
    #---------------------
    # Title Section
    #---------------------
    st.title("📘 Reading Result Prediction Dashboard")
    st.markdown("A Logistic Regression model that predicts whether a student will **Pass or Fail in reading**.")

    tab1, tab2 = st.tabs(["Predict", "About Model"])

    # Add content to each tab
    with tab1:
        PF_pred(scores_model)
        st.caption("Built with Streamlit for practice project")
        


    with tab2:
        logregression()


elif page == "📈 Model Insights":
    tab1, tab2 = st.tabs(["Insights", "Charts info"])

    with tab1:
        model_insight()

    with tab2:
        charts_info()  
        st.divider()
        st.caption("👨‍💻 Created by Atharv AC | 🔗 https://github.com/Atharv-AC")
        st.caption("Built with ❤️ using Streamlit as practice project")





# st.caption("Built with Streamlit for practice project")

# Tabs layout
# tab1, tab2 = st.tabs(["Predict", "About Model"])
# st.write(input_data.columns)
# st.write(PF_model.feature_names_in_)
# st.write(df.feature_names_in_[0])


# Tab 1 → prediction
# Tab 2 → model explanation


# for debuggind\g
# expected = list(model.feature_names_in_)
# expected = list(df.feature_names_in_)
# actual = list(input_data.columns)

# if expected != actual:
#     st.error(f"Feature mismatch\nExpected: {expected}\nGot: {actual}")
#     st.stop()


# To see model type
# st.write(type(model))

# Select Model in U
# model_choice = st.selectbox(
#     "Select Model",
#     ["Reading Predictor", "Score Predictor"]
# )

# model = PF_model if model_choice == "Reading Predictor" else Score_model



#  streamlit run "/home/yash/projects/dsai/mini_projects/UI-Dashboards/Students Marks Prediction/src/dashboard.py"

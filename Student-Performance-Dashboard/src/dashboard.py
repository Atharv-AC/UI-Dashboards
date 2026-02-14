import streamlit as st
from loader import csv_path, load_csv
from analytics import average, Gender_analysis, top_10_students
from charts import Chart, Mcharts, Rcharts, Wcharts, distributions, Box_plots
import pandas as pd

load_csv()

st.set_page_config(page_title="Student Dashboard", layout="wide")


st.markdown('''# 📊 Student Performance Analysis

> A comprehensive data analysis tool that provides insights into student academic performance using Python-based analytics and visualization.
> 
''')

# Creates a sidebar for navigation
menu = st.sidebar.selectbox(
    "Navigation",
    [   
        "Home",
        "Data preview",
        "Averages",
        "Gender Analysis",
        "Charts",
        "Distribution",
        "Box Plot",
        "Top Students"
    ]
)

# Displays content based on the selected menu option
if menu == "Home":


    st.markdown("---")

    # Overview section
    st.subheader("📋 Overview")

    st.write("""
This project analyzes student performance data to uncover patterns and trends in academic achievement.  
Using Python, SQLite, Pandas, and Matplotlib, it performs statistical analysis and generates visual reports.
""")

    st.markdown("---")

    # Feature cards
    st.subheader("🚀 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
**Database Management**
- SQLite backend  
- Efficient data storage  
- Fast queries  
""")

    with col2:
        st.success("""
**Analytics**
- Averages  
- Gender comparison  
- Top performers  
""")

    with col3:
        st.warning("""
**Visualizations**
- Charts  
- Histograms  
- Box plots  
""")

    st.markdown("---")

    # How to use section
    st.subheader("""🧭 How to Use
> Click on the sidebar [>>] to navigate through different sections of the dashboard.
>                  
""")

    st.write("""
1. View the Data in Data preview  
2. Explore averages and gender analysis  
3. View charts and distributions  
4. Identify top-performing students  
""")

    st.subheader("Key Insights")

    st.write("""
    - Reading scores are generally higher than math scores.
    - Gender differences are visible across subjects.
    - Score distributions are approximately normal.
    """)

    st.markdown("---")

    # Footer
    st.caption("Built with Streamlit • Python • SQLite • Matplotlib")



elif menu == "Data preview":
   
    df = pd.read_csv(csv_path)
    # df = pd.read_csv("../Dataset/StudentsPerformance_cleaned.csv")
    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Summary Stats")
    st.write(df.describe())

    gender = df["gender"].unique()
    st.subheader("Filter By gender")
    selected_gen = st.selectbox("", gender)
    filter_data = df[df["gender"] == selected_gen]
    st.dataframe(filter_data)

    groups  = df["race/ethnicity"].unique()
    st.subheader("Filter By Groups")
    selected_grp = st.selectbox("", groups)
    filter_data = df[df["race/ethnicity"] == selected_grp]
    st.dataframe(filter_data)


elif menu == "Averages":
    st.write("Average Scores")

    @st.cache_data
    def get_average_cached():
        return average()

    datas = get_average_cached()
    df = pd.DataFrame(
        datas,
        columns=["avg_math", "avg_reading", "avg_writing"]
    )
    st.dataframe(df)
    avg_Math = datas[0][0]
    avg_Read = datas[0][1]
    avg_Write = datas[0][2]

    st.metric("Average Math Score", round(avg_Math,2))
    st.metric("Average Reading Score", round(avg_Read,2))
    st.metric("Average Writing Score", round(avg_Write,2))


elif menu == "Gender Analysis":
    st.write("Gender Analysis")

    @st.cache_data
    def get_gender_cached():
        return Gender_analysis()
    
    gendata = get_gender_cached()
    st.dataframe(gendata)

    df = pd.DataFrame(
        gendata,
        columns=["gender", "avg_math", "avg_reading", "avg_writing"]
    )
    gender_list = df["gender"].unique()
    selected_gen = st.selectbox("Select Gender", ["All"] + list(df["gender"].unique())) 

    if selected_gen == "All":
        filter_data = df 
    else:
        filter_data = df[df["gender"] == selected_gen]
    
    st.dataframe(filter_data)


elif menu == "Charts":
    st.subheader("Average Chart")

    col1, col2 = st.columns([1,2])  

    with col1:
        fig = Chart()
        st.pyplot(fig)


    st.subheader("Math Gender Chart")
    col1, col2 = st.columns([1,2])  

    with col1:
        fig = Mcharts()
        st.pyplot(fig)

    st.subheader("Reading Gender Chart")
    col1, col2 = st.columns([1,2])  
    with col1:
        figs = Rcharts()
        st.pyplot(figs)

    st.subheader("Writing Gender Chart")
    col1, col2 = st.columns([1,2])  
    with col1:
        fig2 = Wcharts()
        st.pyplot(fig2)

    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.subheader("Reading Gender Chart")
    #     st.pyplot(fig1)

    # with col2:
    #     st.subheader("Writing Gender Chart")
    #     st.pyplot(fig2)

    # with col3:
    #     st.subheader("Math Gender Chart")
    #     st.pyplot(figs)


elif menu == "Distribution":
    st.subheader("Distribution chart")
    # to adjust the position of the chart in the center of the page
    col1, col2, col3 = st.columns([1,2,1])

    try:
      figss = distributions()
      with col2:
       st.pyplot(figss)

    except Exception as e:
      st.error(f"Error: {e}")


elif menu == "Box Plot":
    st.subheader("Box Plot Chart")
    col1, col2, col3 = st.columns([1,2,1])

    # try:
    #   figsss = Box_plot()
    #   with col2:
    #    st.pyplot(figsss)

    # except Exception as e:
    #   st.error(f"Error: {e}")
    with col2:
        figss = Box_plots()
        st.pyplot(figss)

elif menu == "Top Students":
    st.write("Top 10 Students")
    top = top_10_students()
    df = pd.DataFrame(
        top,
        columns=["Gender", "Math Score", "Reading Score", "Writing Score", "Total score"]
    )
    st.dataframe(df)


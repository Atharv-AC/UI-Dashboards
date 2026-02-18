import streamlit as st
from sklearn.metrics import mean_absolute_error


def values(PF_model):
    model =  PF_model["model"]
    X_test = PF_model["X_test"]
    y_test = PF_model["y_test"]

    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    rsq = model.score(X_test, y_test)

    return model, mae, rsq



@st.cache_data
def evaluate(model, pred, X_test, y_test):

    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    rsq = model.score(X_test, y_test)


    # mean_absolute_error is a metric that measures the average absolute error 
    # between the predicted values and the actual values.
    mae = mean_absolute_error(y_test, pred)
    st.metric("Mean absolute error:", f"{mae:<10.2f}")


    rsq = model.score(X_test, y_test) 

    # R² = 0.9 → 90% of the variance in the reading scores can be explained by the math and writing scores.
    st.metric("Varience(R²):", f"{rsq * 100:.2f}% ")

    return pred, mae, rsq



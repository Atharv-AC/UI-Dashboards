import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


# -----------------------------
# Pass / Fail Distribution
# -----------------------------
def pass_fail_chart(df):

    fig, ax = plt.subplots()

    df["pass"].value_counts().plot(kind="bar", ax=ax)

    fig.patch.set_facecolor("#CAFA8F")
    ax.set_facecolor("#D4FFB3")

    ax.set_title("Pass vs Fail Distribution")
    ax.set_xlabel("Result")
    ax.set_ylabel("Count")

    return fig

# -----------------------------
# Math Score Distribution
# -----------------------------
def score_distribution(df):

    fig, ax = plt.subplots()

    ax.hist(df["math_score"], bins=20)

    fig.patch.set_facecolor("#FABFFF")
    ax.set_facecolor("#F0C6FD")

    ax.set_title("Math Score Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Number of Students")

    return fig



# -----------------------------
# Scatter Plot (Math vs Writing)
# -----------------------------
def scatter_chart(df):

    fig, ax = plt.subplots()

    ax.scatter(df["math_score"], df["writing_score"])

    fig.patch.set_facecolor("#FFEBD7")
    ax.set_facecolor("#FFE2E2")

    ax.set_title("Math vs Writing Relationship")
    ax.set_xlabel("Math Score")
    ax.set_ylabel("Writing Score")

    return fig


# -----------------------------
# Probability Distribution
# -----------------------------
def histo(model, X_test):

    probs = model.predict_proba(X_test)[:, 1]

    fig, ax = plt.subplots()

    ax.hist(probs, bins=20)

    fig.patch.set_facecolor("#FFDEEB")
    ax.set_facecolor("#FEDEDE")

    ax.set_title("Prediction Probability Distribution")
    ax.set_xlabel("Probability of Pass")
    ax.set_ylabel("Frequency")

    return fig



# -----------------------------
# ROC Curve
# -----------------------------
def curve(model, X_test, y_test):

    probs = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, probs)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots()

    ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax.plot([0, 1], [0, 1], linestyle="--")  # random baseline

    fig.patch.set_facecolor("#FFDEEB")
    ax.set_facecolor("#FEDEDE")

    ax.set_title("ROC Curve")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()


    return fig

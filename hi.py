import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv("student-por.csv", sep=";")

st.set_page_config(page_title="🎓 Student Risk Dashboard", layout="wide")
st.title("🎓 Student's Real Time Performance Insights Dashboard")

# ---------------------------
# Define target variable
# ---------------------------
if "G3" in df.columns:
    y = (df["G3"] < 10).astype(int)   # dropout risk if final grade < 10
    X = df.drop(columns=["G3"])
elif "G1" in df.columns and "G2" in df.columns:
    avg_grade = (df["G1"] + df["G2"]) / 2
    y = (avg_grade < 10).astype(int)
    X = df.drop(columns=["G1", "G2"])
else:
    st.error("❌ No suitable grade columns (G3 or G1/G2) found in dataset.")
    st.stop()

# ---------------------------
# Preprocessing (encode categorical)
# ---------------------------
categorical_cols = X.select_dtypes(include=["object"]).columns
numeric_cols = X.select_dtypes(exclude=["object"]).columns

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# ---------------------------
# Train model
# ---------------------------
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", GradientBoostingClassifier())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

st.sidebar.header("⚙️ Dashboard Controls")
student_idx = st.sidebar.number_input(
    "Select student index", min_value=0, max_value=len(df)-1, step=1
)

# ---------------------------
# Recent Alerts & Recommendations
# ---------------------------
st.subheader("🚨 Recent Alerts & Recommendations")

student_data = X.iloc[student_idx:student_idx+1]
prediction = model.predict(student_data)[0]
probability = model.predict_proba(student_data)[0][1]

if prediction == 1:
    st.error(f"Student {student_idx} is **at risk** of dropout (probability {probability:.2f}).")
    st.write("**Recommendation:** Provide personalized mentoring, track attendance, and involve parents.")
else:
    st.success(f"Student {student_idx} is **not at risk** (probability {probability:.2f}).")
    st.write("**Recommendation:** Continue encouraging and providing growth opportunities.")

st.markdown("---")

# ---------------------------
# Dashboard Layout
# ---------------------------
col1, col2 = st.columns(2)

# Pie chart: Dropout Risk Distribution
with col1:
    st.subheader("📊 Dropout Risk Distribution")
    risk_counts = pd.Series(y).value_counts().rename({0: "Not at Risk", 1: "At Risk"})
    fig_pie = px.pie(
        names=risk_counts.index,
        values=risk_counts.values,
        title="Distribution of Students by Dropout Risk",
        color=risk_counts.index,
        color_discrete_map={"At Risk": "red", "Not at Risk": "green"}
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Line chart: Academic Performance Trends
with col2:
    st.subheader("📈 Academic Performance Trends")
    if {"G1", "G2", "G3"}.issubset(df.columns):
        avg_scores = df[["G1", "G2", "G3"]].mean()
        fig_line = px.line(
            x=["1st Period", "2nd Period", "Final Exam"],
            y=avg_scores.values,
            markers=True,
            title="Average Grades Over Time"
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No G1/G2/G3 data available for trends.")

# Bar chart: Absences vs Risk
st.subheader("📉 Absences vs Dropout Risk")
if "absences" in df.columns:
    df_temp = df.copy()
    df_temp["Risk"] = y.map({0: "Not at Risk", 1: "At Risk"})
    fig_bar = px.bar(
        df_temp, x="Risk", y="absences", color="Risk", 
        barmode="group", title="Average Absences by Risk Group",
        labels={"absences": "Number of Absences"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------
# Academic Insights
# ---------------------------
st.subheader("📚 Academic Insights Summary")
st.write(f"- ✅ Model Accuracy: **{accuracy*100:.2f}%**")
st.write("- 🚨 Higher absences strongly correlate with dropout risk.")
st.write("- 📉 Low first/second period grades often predict final failure.")
st.write("- 🎯 Teachers should focus on early interventions.")

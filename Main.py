import streamlit as st
import pandas as pd

st.set_page_config(page_title="Goal Tracker", layout="centered")

st.title("🎯 Life Progress Tracker")
st.write("Track how close you are to your goals based on your daily log CSV.")

# File uploader
uploaded_file = st.file_uploader("Upload your daily log CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # --- Sports Section ---
        st.header("🏅 Sports Progress")

        sports_goals = {
            "Salle": 48,
            "Course": 32,
            "Autre_sport": 16
        }

        for activity, goal in sports_goals.items():
            if activity not in df.columns:
                st.warning(f"Missing column in CSV: {activity}")
                continue

            count = df[activity].sum()
            progress = min(count / goal, 1.0)
            percent = round(progress * 100, 1)

            st.subheader(f"• {activity}")
            st.write(f"{int(count)} / {goal} — **{percent}% achieved**")
            st.progress(progress)

            # --- Food Section ---
        st.header("🏅 Food Progress")

        food_goals = {
            "Petit_dej": 13,
            "Regime_alimentaire": 42
        }

        for activity, goal in food_goals.items():
            if activity not in df.columns:
                st.warning(f"Missing column in CSV: {activity}")
                continue

            count = df[activity].sum()
            progress = min(count / goal, 1.0)
            percent = round(progress * 100, 1)

            st.subheader(f"• {activity}")
            st.write(f"{int(count)} / {goal} — **{percent}% failed**")
            st.progress(progress)

            # --- Formation Section ---
        st.header("🏅 Skills Progress")

        skills_goals = {
            "Formation_crypto": 112,
            "Formation_LLM": 48
        }

        for activity, goal in skills_goals.items():
            if activity not in df.columns:
                st.warning(f"Missing column in CSV: {activity}")
                continue

            count = df[activity].sum()
            progress = min(count / goal, 1.0)
            percent = round(progress * 100, 1)

            st.subheader(f"• {activity}")
            st.write(f"{int(count)} / {goal} — **{percent}% achieved**")
            st.progress(progress)

            # --- Money Section ---
        st.header("🏅 Skills Progress")

        money_goals = {
            "Argent": 3200
        }

        for activity, goal in money_goals.items():
            if activity not in df.columns:
                st.warning(f"Missing column in CSV: {activity}")
                continue

            count = df[activity].sum()
            progress = min(count / goal, 1.0)
            percent = round(progress * 100, 1)

            st.subheader(f"• {activity}")
            st.write(f"{int(count)} / {goal} — **{percent}% achieved**")
            st.progress(progress)

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload your CSV file to get started.")

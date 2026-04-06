import streamlit as st
import pandas as pd
from utils.validators import validate_telemetry

class TelemetryAgent:

    def run(self):
        st.title("📊 Telemetry Agent")

        file = st.file_uploader("Upload CSV Telemetry", type=["csv"])

        if not file:
            st.warning("Upload telemetry CSV to proceed.")
            return

        df = pd.read_csv(file)

        valid, msg = validate_telemetry(df)
        if not valid:
            st.error(msg)
            return

        insights, warnings, recs = self.analyze(df)

        st.subheader("Insights")
        st.write(insights)

        st.subheader("Warnings")
        st.write(warnings)

        st.subheader("Recommendations")
        st.write(recs)

    def analyze(self, df):
        insights = []
        warnings = []
        recs = []

        if "speed" in df.columns and "throttle" in df.columns:
            corr = df["speed"].corr(df["throttle"])
            insights.append(f"Throttle-speed correlation: {corr:.2f}")

        if "brake" in df.columns:
            hard_brakes = (df["brake"] > df["brake"].quantile(0.9)).sum()
            warnings.append(f"High braking events: {hard_brakes}")

        if "throttle" in df.columns:
            smoothness = df["throttle"].diff().abs().mean()
            insights.append(f"Throttle smoothness score: {smoothness:.3f}")
            if smoothness > df["throttle"].std():
                recs.append("Improve throttle modulation for stability")

        return insights, warnings, recs
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

        # --- Correlation ---
        if "speed" in df.columns and "throttle" in df.columns:
            corr = df["speed"].corr(df["throttle"])
            insights.append(f"Throttle-speed correlation: {corr:.2f}")

            if corr < 0.6:
                recs.append("Throttle application is not efficiently translating into speed. Review traction and power delivery.")

        # --- Braking ---
        if "brake" in df.columns:
            threshold = df["brake"].quantile(0.9)
            hard_brakes = (df["brake"] > threshold).sum()
            warnings.append(f"High braking events: {hard_brakes}")

            if hard_brakes > len(df) * 0.15:
                recs.append("Frequent aggressive braking detected. Consider optimizing braking zones and trail braking technique.")
            else:
                recs.append("Braking is generally controlled. Fine-tune entry speeds for marginal gains.")

        # --- Throttle smoothness ---
        if "throttle" in df.columns:
            smoothness = df["throttle"].diff().abs().mean()
            std = df["throttle"].std()

            insights.append(f"Throttle smoothness score: {smoothness:.3f}")

            if smoothness > std:
                recs.append("Throttle inputs are too abrupt. Improve modulation for better traction.")
            else:
                recs.append("Throttle control is smooth. You can push more aggressively on corner exits.")

        # --- Temperature analysis ---
        if "engine_temp" in df.columns:
            max_temp = df["engine_temp"].max()
            insights.append(f"Max engine temp: {max_temp}")

            if max_temp > df["engine_temp"].mean() * 1.1:
                warnings.append("Engine temperature spike detected.")
                recs.append("Review cooling efficiency or airflow management.")

        # --- Guarantee output ---
        if len(recs) == 0:
            recs.append("No major issues detected. Focus on incremental improvements in consistency and lap optimization.")

        return insights, warnings, recs

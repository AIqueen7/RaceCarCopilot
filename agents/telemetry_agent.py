import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from utils.validators import validate_telemetry


class TelemetryAgent:
    import matplotlib.pyplot as plt
    import streamlit as st
    def run(self):
        st.title("📊 Telemetry Agent")

        file = st.file_uploader("Upload CSV Telemetry", type=["csv"])

        if file is None:
            st.warning("Upload telemetry CSV to proceed.")
            return

        try:
            df = pd.read_csv(file)
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            return

        valid, msg = validate_telemetry(df)
        if not valid:
            st.error(msg)
            return

        insights, warnings, recs = self.analyze(df)

        st.subheader("Insights")
        for i in insights:
            st.write(f"- {i}")

        st.subheader("Warnings")
        for w in warnings:
            st.write(f"- {w}")

        st.subheader("Recommendations")
        for r in recs:
            st.write(f"- {r}")
    def plot_telemetry(df):
    
        fig1, ax1 = plt.subplots()
        ax1.plot(df["time"], df["speed"])
        ax1.set_title("Speed vs Time")
        st.pyplot(fig1)
    
        fig2, ax2 = plt.subplots()
        ax2.plot(df["time"], df["throttle"], label="Throttle")
        ax2.plot(df["time"], df["brake"], label="Brake")
        ax2.legend()
        ax2.set_title("Throttle vs Brake")
        st.pyplot(fig2)
    
        if "engine_temp" in df.columns:
            fig3, ax3 = plt.subplots()
            ax3.plot(df["time"], df["engine_temp"])
            ax3.set_title("Engine Temperature Trend")
            st.pyplot(fig3)
    def analyze(self, df):
        insights = []
        warnings = []
        recs = []

        # --- Correlation ---
        if "speed" in df.columns and "throttle" in df.columns:
            corr = df["speed"].corr(df["throttle"])
            insights.append(f"Throttle-speed correlation: {corr:.2f}")

            if corr < 0.6:
                recs.append(
                    "Throttle application is not efficiently translating into speed. Review traction and power delivery."
                )

        # --- Braking ---
        if "brake" in df.columns:
            threshold = df["brake"].quantile(0.9)
            hard_brakes = (df["brake"] > threshold).sum()
            warnings.append(f"High braking events: {hard_brakes}")

            if hard_brakes > len(df) * 0.15:
                recs.append(
                    "Frequent aggressive braking detected. Optimize braking zones and trail braking."
                )
            else:
                recs.append(
                    "Braking is controlled. Fine-tune entry speeds for marginal gains."
                )

        # --- Throttle smoothness ---
        if "throttle" in df.columns:
            smoothness = df["throttle"].diff().abs().mean()
            std = df["throttle"].std()

            insights.append(f"Throttle smoothness score: {smoothness:.3f}")

            if smoothness > std:
                recs.append(
                    "Throttle inputs are abrupt. Improve modulation for better traction."
                )
            else:
                recs.append(
                    "Throttle control is smooth. You can push harder on corner exits."
                )

        # --- Temperature ---
        if "engine_temp" in df.columns:
            max_temp = df["engine_temp"].max()
            insights.append(f"Max engine temp: {max_temp}")

            if max_temp > df["engine_temp"].mean() * 1.1:
                warnings.append("Engine temperature spike detected.")
                recs.append("Check cooling system or airflow.")

        # --- Fallback ---
        if len(recs) == 0:
            recs.append(
                "No major issues detected. Focus on consistency and lap time optimization."
            )

        return insights, warnings, recs = self.analyze(df), self.plot_telemetry(df)

import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go


class TelemetryAgent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run(self):
        st.title("🏎️ Telemetry Intelligence Dashboard")

        if self.df is None or self.df.empty:
            st.warning("No telemetry data loaded.")
            return

        self.clean_data()
        insights, warnings, recs = self.analyze(self.df)

        self.render_summary(insights, warnings, recs)
        self.render_graphs()

    def clean_data(self):
        self.df = self.df.copy()

        # normalize column names
        self.df.columns = [c.strip().lower() for c in self.df.columns]

        # common safety fill
        self.df = self.df.replace([np.inf, -np.inf], np.nan)
        self.df = self.df.fillna(method="ffill")

    def analyze(self, df):
        insights = []
        warnings = []
        recs = []

        if "speed" in df.columns:
            insights.append(f"Max speed: {df['speed'].max():.2f}")
            if df["speed"].max() > 300:
                warnings.append("Very high speed detected")
                recs.append("Check aerodynamics setup")

        if "throttle" in df.columns and "brake" in df.columns:
            overlap = ((df["throttle"] > 0) & (df["brake"] > 0)).sum()
            if overlap > 0:
                warnings.append("Throttle + brake overlap detected")
                recs.append("Adjust pedal mapping / driver input smoothing")

        if not warnings:
            warnings.append("No critical issues detected")

        return insights, warnings, recs

    def render_summary(self, insights, warnings, recs):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Insights", len(insights))
            for i in insights:
                st.write("•", i)

        with col2:
            st.metric("Warnings", len(warnings))
            for w in warnings:
                st.write("⚠️", w)

        with col3:
            st.metric("Recommendations", len(recs))
            for r in recs:
                st.write("💡", r)

    def render_graphs(self):
        st.subheader("📊 Telemetry Graphs")

        # SPEED GRAPH
        if "speed" in self.df.columns:
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                y=self.df["speed"],
                mode="lines",
                name="Speed"
            ))
            fig.update_layout(title="Speed Over Time")
            st.plotly_chart(fig, use_container_width=True)

        # THROTTLE vs BRAKE
        if "throttle" in self.df.columns and "brake" in self.df.columns:
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=self.df["throttle"], name="Throttle"))
            fig.add_trace(go.Scatter(y=self.df["brake"], name="Brake"))
            fig.update_layout(title="Throttle vs Brake")
            st.plotly_chart(fig, use_container_width=True)

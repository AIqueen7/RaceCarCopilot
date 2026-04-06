import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go


class TelemetryAgent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run(self):
        st.subheader("Telemetry Dashboard")

        if self.df is None or self.df.empty:
            st.error("No telemetry data available")
            return

        self.clean()

        insights, warnings, recs = self.analyze()

        self.render(insights, warnings, recs)
        self.graphs()

    def clean(self):
        self.df.columns = [c.lower().strip() for c in self.df.columns]
        self.df = self.df.replace([np.inf, -np.inf], np.nan)
        self.df = self.df.fillna(method="ffill")

    def analyze(self):
        insights, warnings, recs = [], [], []

        if "speed" in self.df.columns:
            max_speed = self.df["speed"].max()
            insights.append(f"Max speed: {max_speed:.2f}")

            if max_speed > 300:
                warnings.append("High speed detected")
                recs.append("Review aerodynamics / gearing")

        if "throttle" in self.df.columns and "brake" in self.df.columns:
            overlap = ((self.df["throttle"] > 0) & (self.df["brake"] > 0)).sum()
            if overlap > 0:
                warnings.append("Throttle + brake overlap detected")
                recs.append("Fix pedal mapping / driver input")

        if not warnings:
            warnings.append("No critical issues detected")

        return insights, warnings, recs

    def render(self, insights, warnings, recs):
        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Insights", len(insights))
            for i in insights:
                st.write("•", i)

        with c2:
            st.metric("Warnings", len(warnings))
            for w in warnings:
                st.write("⚠️", w)

        with c3:
            st.metric("Recommendations", len(recs))
            for r in recs:
                st.write("💡", r)

    def graphs(self):
        st.subheader("Live Telemetry Graphs")

        if "speed" in self.df.columns:
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=self.df["speed"], mode="lines", name="Speed"))
            fig.update_layout(title="Speed Over Time")
            st.plotly_chart(fig, use_container_width=True)

        if "throttle" in self.df.columns and "brake" in self.df.columns:
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=self.df["throttle"], name="Throttle"))
            fig.add_trace(go.Scatter(y=self.df["brake"], name="Brake"))
            fig.update_layout(title="Throttle vs Brake")
            st.plotly_chart(fig, use_container_width=True)

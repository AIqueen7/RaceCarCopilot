import streamlit as st

class MaintenanceAgent:

    def run(self):
        st.title("🔧 Maintenance Agent")

        logs = st.text_area("Enter maintenance logs")

        if st.button("Analyze"):
            if not logs:
                st.warning("Enter logs")
                return

            st.write(self.analyze(logs))

    def analyze(self, logs):
        issues = []
        if "overheat" in logs.lower():
            issues.append("Cooling system check required")

        return {
            "issues": issues,
            "recommendations": ["Schedule inspection"]
        }
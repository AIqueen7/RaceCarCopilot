import streamlit as st

class StrategyAgent:

    def run(self):
        st.title("🧠 Strategy Agent")

        stint = st.number_input("Stint Length")
        tire = st.number_input("Tire Wear Rate")
        fuel = st.number_input("Fuel Usage per lap")

        if st.button("Generate Strategy"):
            if stint == 0 or tire == 0 or fuel == 0:
                st.warning("Provide valid inputs")
                return

            result = self.compute(stint, tire, fuel)
            st.write(result)

    def compute(self, stint, tire, fuel):
        return {
            "pit": f"Pit after {stint/2:.1f} laps",
            "tires": f"Monitor degradation at {tire}",
            "risk": f"Fuel criticality at {fuel}"
        }
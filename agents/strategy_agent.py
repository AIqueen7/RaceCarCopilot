import streamlit as st


class StrategyAgent:

    def run(self):
        st.title("🧠 Strategy Agent")

        # ---------------- INPUTS ----------------
        col1, col2 = st.columns(2)

        with col1:
            stint_length = st.number_input(
                "Planned Stint Length (laps)",
                min_value=1,
                step=1
            )

            tire_wear = st.number_input(
                "Tire Wear Rate (% per lap)",
                min_value=0.0,
                max_value=100.0,
                step=0.1
            )

            fuel_per_lap = st.number_input(
                "Fuel Usage per Lap (L)",
                min_value=0.0,
                step=0.1
            )

        with col2:
            tire_compound = st.selectbox(
                "Tire Compound",
                ["Select...", "Soft", "Medium", "Hard", "Unknown"]
            )

            track_type = st.selectbox(
                "Track Type",
                ["Select...", "Street", "High Speed", "Technical", "Endurance"]
            )

            race_condition = st.selectbox(
                "Race Condition",
                ["Select...", "Clear", "Wet", "Changing", "Safety Car Likely"]
            )

        push_mode = st.toggle("Aggressive Push Strategy")
        tire_save_mode = st.toggle("Tire Saving Mode")

        # ---------------- RUN ----------------
        if st.button("Generate Strategy"):
            if "Select..." in [tire_compound, track_type, race_condition]:
                st.warning("Please complete all dropdown selections.")
                return

            result = self.compute(
                stint_length,
                tire_wear,
                fuel_per_lap,
                tire_compound,
                track_type,
                race_condition,
                push_mode,
                tire_save_mode
            )

            # ---------------- OUTPUT ----------------
            st.subheader("📊 Strategy Summary")

            st.write("### 🟡 Pit Strategy")
            for p in result["pit_strategy"]:
                st.write(f"- {p}")

            st.write("### 🟢 Tire Strategy")
            for t in result["tire_strategy"]:
                st.write(f"- {t}")

            st.write("### 🔵 Fuel Strategy")
            for f in result["fuel_strategy"]:
                st.write(f"- {f}")

            st.write("### ⚠️ Risk Analysis")
            for r in result["risk"]:
                st.write(f"- {r}")

    # ---------------- CORE LOGIC ----------------
    def compute(
        self,
        stint_length,
        tire_wear,
        fuel_per_lap,
        tire_compound,
        track_type,
        race_condition,
        push_mode,
        tire_save_mode
    ):

        pit_strategy = []
        tire_strategy = []
        fuel_strategy = []
        risk = []

        # --- PIT WINDOW ---
        effective_wear = tire_wear

        if tire_save_mode:
            effective_wear *= 0.85

        if push_mode:
            effective_wear *= 1.15

        tire_life = 100 / max(effective_wear, 0.1)
        optimal_pit = min(stint_length, int(tire_life))

        pit_strategy.append(f"Estimated optimal pit window: Lap {optimal_pit}")

        if race_condition == "Safety Car Likely":
            pit_strategy.append("Prepare early pit flexibility due to SC probability")

        # --- TIRE STRATEGY ---
        if tire_compound == "Soft":
            tire_strategy.append("High grip, high degradation strategy required")
        elif tire_compound == "Medium":
            tire_strategy.append("Balanced performance and longevity")
        elif tire_compound == "Hard":
            tire_strategy.append("Long stint stability prioritized")

        if tire_save_mode:
            tire_strategy.append("Tire conservation mode active: smooth inputs required")

        if push_mode:
            tire_strategy.append("Aggressive push enabled: expect accelerated degradation")

        # --- FUEL STRATEGY ---
        total_fuel = fuel_per_lap * stint_length

        fuel_strategy.append(f"Total fuel required: {total_fuel:.2f} L")

        if push_mode:
            fuel_strategy.append("Fuel burn rate may increase under aggressive driving")

        if track_type == "High Speed":
            fuel_strategy.append("High-speed circuit: expect elevated fuel consumption")

        # --- RISK ANALYSIS ---
        if effective_wear > 15:
            risk.append("High tire degradation risk detected")

        if race_condition == "Wet":
            risk.append("Weather instability increases strategy variability")

        if push_mode and tire_save_mode:
            risk.append("Conflicting modes selected (push vs conservation)")

        if stint_length > tire_life:
            risk.append("Stint exceeds tire life expectancy")

        if not risk:
            risk.append("Strategy is stable under current inputs")

        return {
            "pit_strategy": pit_strategy,
            "tire_strategy": tire_strategy,
            "fuel_strategy": fuel_strategy,
            "risk": risk
        }

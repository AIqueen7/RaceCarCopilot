import streamlit as st


class SetupAgent:

    def run(self):
        st.title("⚙️ Setup Agent")

        # --- Dropdown Inputs ---
        track_type = st.selectbox(
            "Track Type",
            ["Select...", "Street Circuit", "High-Speed Circuit", "Technical Circuit", "Mixed"]
        )

        weather = st.selectbox(
            "Weather Conditions",
            ["Select...", "Dry", "Wet", "Mixed"]
        )

        temperature = st.number_input("Track Temperature (°C)", min_value=-10.0, max_value=60.0)

        car_type = st.selectbox(
            "Car Type",
            ["Select...", "GT3", "Formula", "Prototype", "Touring Car", "Custom"]
        )

        driver_goal = st.selectbox(
            "Driver Goal",
            ["Select...", "Maximum Grip", "Top Speed", "Tire Preservation", "Balanced Setup"]
        )

        # --- Generate ---
        if st.button("Generate Setup"):
            if "Select..." in [track_type, weather, car_type, driver_goal]:
                st.warning("Please select all dropdown values.")
                return

            result = self.generate(
                track_type, weather, temperature, car_type, driver_goal
            )

            # --- Output ---
            st.subheader("Recommendations")

            st.write("**Suspension**")
            st.write(result["suspension"])

            st.write("**Tires**")
            st.write(result["tires"])

            st.write("**Aero**")
            st.write(result["aero"])

            st.write("**Gearing**")
            st.write(result["gearing"])

    def generate(self, track, weather, temp, car, goal):
        return {
            "suspension": f"Adjust suspension stiffness based on {track} characteristics to support {goal.lower()}",
            "tires": f"Set tire pressures considering {weather.lower()} conditions and {temp}°C track temperature",
            "aero": f"Optimize aerodynamic balance to achieve {goal.lower()} performance target",
            "gearing": f"Configure gear ratios appropriate for {track.lower()} demands"
        }

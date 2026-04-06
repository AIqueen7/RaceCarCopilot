import streamlit as st

class SetupAgent:

    def run(self):
        st.title("⚙️ Setup Agent")

        track = st.text_input("Track Type")
        weather = st.text_input("Weather")
        temp = st.number_input("Temperature")
        car = st.text_input("Car Type")
        goal = st.text_input("Driver Goal")

        if st.button("Generate Setup"):
            if not all([track, weather, temp, car, goal]):
                st.warning("Fill all fields")
                return

            insights = self.generate(track, weather, temp, car, goal)

            st.write(insights)

    def generate(self, track, weather, temp, car, goal):
        return {
            "suspension": f"Adjust suspension for {track} with focus on {goal}",
            "tires": f"Optimize tire pressure for {temp}°C and {weather}",
            "aero": f"Balance aero for {goal}",
            "gearing": f"Adjust gearing for {track}"
        }
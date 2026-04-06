import streamlit as st

class CopilotAgent:

    def run(self):
        st.title("🤖 Race Copilot")

        if "chat" not in st.session_state:
            st.session_state.chat = []

        user = st.text_input("Ask Copilot")

        if user:
            response = self.respond(user)
            st.session_state.chat.append((user, response))

        for u, r in st.session_state.chat:
            st.write(f"**You:** {u}")
            st.write(f"**Copilot:** {r}")

    def respond(self, query):
        return f"Analyzing: {query}"
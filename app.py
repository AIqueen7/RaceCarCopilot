import streamlit as st
from agents.telemetry_agent import TelemetryAgent
from agents.setup_agent import SetupAgent
from agents.strategy_agent import StrategyAgent
from agents.document_agent import DocumentAgent
from agents.maintenance_agent import MaintenanceAgent
from agents.copilot_agent import CopilotAgent

st.set_page_config(page_title="AI Race Copilot", layout="wide")

# Initialize agents
telemetry_agent = TelemetryAgent()
setup_agent = SetupAgent()
strategy_agent = StrategyAgent()
document_agent = DocumentAgent()
maintenance_agent = MaintenanceAgent()
copilot_agent = CopilotAgent()

st.sidebar.title("🏎️ Race Copilot")
page = st.sidebar.radio("Navigation", [
    "Copilot Chat",
    "Telemetry Agent",
    "Setup Agent",
    "Strategy Agent",
    "Document Agent",
    "Maintenance Agent",
    "Reports"
])

if page == "Telemetry Agent":
    telemetry_agent.run()

elif page == "Setup Agent":
    setup_agent.run()

elif page == "Strategy Agent":
    strategy_agent.run()

elif page == "Document Agent":
    document_agent.run()

elif page == "Maintenance Agent":
    maintenance_agent.run()

elif page == "Copilot Chat":
    copilot_agent.run()

elif page == "Reports":
    st.title("Reports")
    st.write("Download session outputs from agents")

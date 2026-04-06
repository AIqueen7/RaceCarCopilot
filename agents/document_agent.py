import streamlit as st
from services.embeddings import embed_text
from services.vector_store import VectorStore

class DocumentAgent:

    def __init__(self):
        self.store = VectorStore()

    def run(self):
        st.title("📚 Document Agent")

        files = st.file_uploader("Upload Docs", accept_multiple_files=True)

        if files:
            for f in files:
                text = f.read().decode("utf-8", errors="ignore")
                self.store.add(text)

        query = st.text_input("Ask question")

        if query:
            result = self.store.search(query)
            st.write(result)
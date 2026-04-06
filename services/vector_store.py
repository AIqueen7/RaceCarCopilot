import numpy as np
from services.embeddings import embed_text

class VectorStore:

    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text):
        self.texts.append(text)
        self.vectors.append(embed_text(text))

    def search(self, query):
        q_vec = embed_text(query)
        sims = [np.dot(q_vec, v) for v in self.vectors]
        idx = int(np.argmax(sims))
        return self.texts[idx]
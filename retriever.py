import wikipedia
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from transformers import pipeline

class RAGRetriever:
    def __init__(self):
        # Embedding model
        self.embed_model = SentenceTransformer('all-MiniLM-L6-v2')
        # QA model
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        self.index = None
        self.text_chunks = []

    def get_wikipedia_content(self, topic):
        try:
            return wikipedia.page(topic).content
        except wikipedia.exceptions.DisambiguationError as e:
            return wikipedia.page(e.options[0]).content
        except wikipedia.exceptions.PageError:
            return None

    def chunk_text(self, text, max_len=200):
        words = text.split()
        chunks = []
        for i in range(0, len(words), max_len):
            chunks.append(" ".join(words[i:i+max_len]))
        return chunks

    def load_topic(self, topic):
        text = self.get_wikipedia_content(topic)
        if not text:
            raise ValueError("Topic not found on Wikipedia.")
        self.text_chunks = self.chunk_text(text)
        embeddings = self.embed_model.encode(self.text_chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings).astype('float32'))

    def ask(self, question, top_k=3):
        if not self.index:
            raise ValueError("Load a topic first!")
        q_embed = self.embed_model.encode([question]).astype('float32')
        D, I = self.index.search(q_embed, top_k)
        context = " ".join([self.text_chunks[i] for i in I[0]])
        answer = self.qa_pipeline(question=question, context=context)
        return answer['answer']

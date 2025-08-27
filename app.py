import streamlit as st
from retriever import RAGRetriever

st.set_page_config(page_title="RAG Assistant", page_icon="🤖", layout="wide")

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 RAG Assistant")
st.write("Ask questions about any topic (Wikipedia-based).")

retriever = RAGRetriever()

topic = st.text_input("Enter topic:", "")
if topic:
    try:
        with st.spinner("Loading topic..."):
            retriever.load_topic(topic)
        st.success("Topic loaded! Ask your questions below.")
    except Exception as e:
        st.error(f"Error: {e}")

query = st.text_input("Ask a question:", "")
if query and topic:
    try:
        with st.spinner("Fetching answer..."):
            answer = retriever.ask(query)
        st.markdown(f"**Answer:** {answer}")
    except Exception as e:
        st.error(f"Error: {e}")

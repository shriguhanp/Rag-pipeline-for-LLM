# 🤖 RAG Assistant – AI-Powered Question Answering

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.27.0-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)](https://github.com/<your-username>/rag-assistant)

**RAG Assistant** is a **professional Retrieval-Augmented Generation (RAG)** app built with **Python, FAISS, and Streamlit**.  
It allows users to ask **any question on Wikipedia topics** and get **precise AI-generated answers instantly**.

---

## ✨ Features

- 🌐 Search **any Wikipedia topic** dynamically  
- 🧠 **RAG-powered semantic QA**  
- ⚡ **Fast retrieval** with FAISS  
- 🎨 **Sleek Apple-like UI/UX**  
- 💻 Easy to **run locally or deploy**  
- 📦 Modular & scalable  

---

## 🎬 Demo / Screenshots

### Home Page
<img width="1919" height="892" alt="Screenshot 2025-08-27 090801" src="https://github.com/user-attachments/assets/01179048-31ca-44f2-9e42-2b0046b1ba63" />


### Ask a Question
<img width="1919" height="894" alt="Screenshot 2025-08-27 090953" src="https://github.com/user-attachments/assets/465fb9a8-fd33-42d9-9f95-d4d9008b2802" />


### AI Answer
<img width="1915" height="895" alt="Screenshot 2025-08-27 083746" src="https://github.com/user-attachments/assets/ef48aebd-f249-4f56-b2d6-ff50a762e4d9" />
  

## 🗂 Folder Structure
rag-assistant/
│── app.py # Streamlit entry point
│── retriever.py # RAG logic: embeddings + FAISS + QA
│── style.css # Custom CSS for UI/UX
│── requirements.txt # Dependencies
│── images/ # Screenshots & demo GIFs
│── .gitignore
│── README.md


---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/rag-assistant.git
cd rag-assistant

2. Create & activate virtual environment:

python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux / Mac


3. Install dependencies:

pip install -r requirements.txt

🚀 Usage

Run the app:

python -m streamlit run app.py


Open in browser:

http://localhost:8501


Enter a topic, ask a question, get instant AI answers.

🔧 How It Works

User inputs a topic → Wikipedia content fetched

Content is chunked → embeddings generated

FAISS vector search finds relevant chunks

Transformers QA pipeline extracts answers

Displayed on a sleek UI

📝 Contributing

Fork the repo

Create branch: git checkout -b feature-name

Commit: git commit -m "Add feature"

Push: git push origin feature-name

Open Pull Request

📌 License

MIT License © 2025 [Your Name]

📫 Contact

GitHub: https://github.com/shriguhanp

Email: shriguhan7@gmail.com


---

If you want, I can **also make the `images/` folder with ready-made demo screenshots** so you literally just push it to GitHub and it looks like a **premium AI project**.  

Do you want me to do that next?

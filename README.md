# 🎓 Smart College Query / FAQ Resolver (AI Assistant)

## 📌 Project Overview

The **Smart College Query / FAQ Resolver** is an AI-assisted chatbot designed to answer common college-related questions instantly.
It reduces repetitive workload on administrative staff by providing automated responses to frequently asked student queries.

The system is built using a **privacy-safe, generic dataset**, making it reusable and secure for deployment across different institutions.

---

## ❓ Problem Statement

In colleges, students repeatedly ask similar questions related to:

* Admissions
* Fees
* Timings
* Scholarships
* Hostels
* Placements

This results in:

* Increased administrative workload
* Delayed responses
* Inefficient communication

---

## 💡 Proposed Solution

An **AI-powered FAQ chatbot** that:

* Instantly answers common student queries
* Uses a structured knowledge base
* Works without external APIs
* Can be easily customized for any college

---

## 🧠 Key Features

* 📄 Generic college FAQ dataset
* 🤖 Automated question answering
* 🔒 No sensitive or real college data used
* 🎨 Modern and responsive chat UI
* ⚙️ Flask-based backend
* 🔌 Easy integration with ML / RAG models

---

## ❔ Sample Questions Handled by the System

The chatbot is capable of answering common student queries such as:

1. **What is the admission process?**
2. **Are scholarships available?**
3. **Does the college provide hostel facilities?**

These questions demonstrate how the system efficiently resolves frequently asked queries using its built-in knowledge base.

---

## 🛠️ Technology Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Data Storage:** JSON
* **Architecture:** Modular & Scalable

---

## 🏗️ System Architecture

1. User enters a question through the chat interface
2. The request is sent to the Flask backend
3. Backend processes the query using keyword-based matching
4. Relevant answer is fetched from the knowledge base
5. Response is displayed instantly on the UI

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install flask
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open Browser

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
collegegpt/
├── app.py
├── data/
│   └── college_data.json
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## 🔐 Data Privacy & Security

* No real college or student data is used
* Dataset is fully generic and safe
* System supports private deployment for institutions

---

## 🚀 Future Enhancements

* NLP-based similarity matching (TF-IDF / cosine similarity)
* RAG integration with PDFs (notices, prospectus)
* Urgent query detection
* Admin dashboard for managing FAQs
* Multi-language support

---

## 🏆 Hackathon Use Case

This project demonstrates how AI can:

* Improve student experience
* Automate administrative support
* Maintain data privacy
* Be customized for different colleges

---

## ✅ Conclusion

The **Smart College Query / FAQ Resolver** is a scalable, secure, and efficient AI assistant that helps colleges streamline communication while ensuring privacy and ease of deployment.

Just say 👍

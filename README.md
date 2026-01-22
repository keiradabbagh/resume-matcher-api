# Resume Matcher API

A backend API that scores resumes against job descriptions using NLP and tracks job applications.  
Built to demonstrate backend engineering, data modeling, and explainable machine learning.

---

## 🚀 Features

- **Resume ↔ Job Description Matching**
  - TF-IDF vectorization
  - Cosine similarity scoring
  - Missing keyword extraction

- **Job Application Tracker**
  - Create, list, update, and delete applications
  - Persistent storage with SQLite
  - Clean RESTful design

- **Production-style Backend**
  - FastAPI
  - SQLAlchemy ORM
  - Pydantic validation
  - Dependency injection
  - Auto-generated API docs (Swagger)

---

## 🧠 How It Works

### Resume Matching
1. Resume text and job description text are vectorized using **TF-IDF**
2. **Cosine similarity** is used to compute a match score
3. Keywords present in the job description but missing from the resume are extracted

This approach is:
- fast
- explainable
- easy to extend with embeddings in future versions

### Job Tracking
Job applications are stored in a relational database and exposed through CRUD endpoints following REST best practices.

---

## 📦 Tech Stack

- **Language:** Python 3
- **API Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **ML / NLP:** scikit-learn
- **Server:** Uvicorn

---

## ▶️ Run Locally

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload

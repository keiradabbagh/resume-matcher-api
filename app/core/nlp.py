from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match(resume_text: str, job_text: str):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([resume_text, job_text])

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())

    missing_keywords = list(job_words - resume_words)

    return round(float(score), 3), missing_keywords[:15]

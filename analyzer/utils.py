import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skills_list = ["python", "java", "sql", "machine learning", "django", "html", "css"]

def extract_text(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()


def extract_skills(text):
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return found
def match_score(resume_text, job_desc):
    cv = CountVectorizer()
    matrix = cv.fit_transform([resume_text, job_desc])
    score = cosine_similarity(matrix)[0][1]
    return round(score * 100, 2)

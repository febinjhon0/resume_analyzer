from django.shortcuts import render
from .models import Resume
from .utils import extract_text, extract_skills, match_score


def index(request):
    if request.method == 'POST':
        file = request.FILES['resume']
        job_desc = request.POST['job_desc']

        resume_obj = Resume.objects.create(file=file)
        file_path = resume_obj.file.path

        text = extract_text(file_path)
        skills = extract_skills(text)
        score = match_score(text, job_desc)

        missing_skills = [s for s in ["python","java","sql","django"] if s not in skills]

        return render(request, 'result.html', {
            'score': score,
            'skills': skills,
            'missing': missing_skills
        })

    return render(request, 'index.html')
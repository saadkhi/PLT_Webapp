from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from . import models

def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def careers(request):
    jobs = models.Job.objects.all().order_by('-posted_at')
    return render(request, 'careers.html', {'jobs': jobs})

def services(request):
    return render(request, 'services.html')

def industries(request):
    return render(request, 'industries.html')

def insights(request):
    return render(request, 'insights.html')

# Job Detail + Application Form
def job_detail(request, job_id):
    job = get_object_or_404(models.Job, id=job_id)

    if request.method == "POST":
        form = forms.ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('careers')  # After submission, go back to job list
    else:
        form = forms.ApplicationForm()

    return render(request, 'job_detail.html', {'job': job, 'form': form})

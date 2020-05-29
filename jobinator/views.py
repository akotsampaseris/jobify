from django.shortcuts import render, HttpResponseRedirect
from .forms import JobinatorForm
from .models import Jobinator

# Create your views here.
def my_jobs(request):
    jobs = Jobinator.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'jobinator/my_jobs.html', context)


def create(request):
    if request.method == 'POST':
        form = JobinatorForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position']
            location = form.cleaned_data['location']
            Jobinator.objects.create(
                position=position,
                location=location
            )
            return HttpResponseRedirect('/jobinator/my-jobs')
    else:
        form = JobinatorForm()

    context = {
        'form': form
    }
    return render(request, 'jobinator/create_job.html', context)


def activate(request, id):
    current_active = Jobinator.objects.filter(active=True)
    for job in current_active:
        job.active = False
        job.save()

    new_active = Jobinator.objects.get(pk=id)
    new_active.active = True
    new_active.save()

    return HttpResponseRedirect('/jobinator/my-jobs')


def deactivate(request, id):
    current_active = Jobinator.objects.get(pk=id)
    current_active.active = False
    current_active.save()

    return HttpResponseRedirect('/jobinator/my-jobs')


def delete(request, id):
    job_to_be_deleted = Jobinator.objects.get(pk=id)
    job_to_be_deleted.delete()

    return HttpResponseRedirect('/jobinator/my-jobs')

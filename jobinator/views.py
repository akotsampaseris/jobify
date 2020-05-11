from django.shortcuts import render, HttpResponseRedirect
from .forms import JobinatorForm
from .models import Jobinator

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = JobinatorForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position']
            location = form.cleaned_data['location']
            Jobinator.objects.create(
                position=position,
                location=location
            )
            return HttpResponseRedirect('/jobinator/results')
    else:
        form = JobinatorForm()

    context = {
        'form': form
    }
    return render(request, 'jobinator/index.html', context)

def test(request):
    jobs = Jobinator.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'jobinator/test.html', context)

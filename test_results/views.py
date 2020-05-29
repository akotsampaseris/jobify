from django.shortcuts import render
from webscraper.models import Job
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 4)
    page = request.GET.get('page', 1)

    jobs = paginator.page(page)

    context = {
        "jobs": jobs
    }

    return render(request, 'test_results/index.html', context)

from django.shortcuts import render, redirect
from webscraper.models import Job, Website
from django.core.paginator import Paginator
from .forms import WebsiteForm

# Create your views here.
def index(request):
    job_list = Job.objects.all().order_by('-created_at')

    paginator = Paginator(job_list, 10)
    page = request.GET.get('page', 1)

    jobs = paginator.page(page)

    context = {
        "jobs": jobs
    }

    return render(request, 'test_results/index.html', context)


def delete_all(request):
    jobs = Job.objects.all()
    for job in jobs:
        job.delete()

    return redirect('jobs:index')


def select_websites(request):
    websites = Website.objects.all().order_by('title')

    context = {
        "websites": websites
    }

    return render(request, 'test_results/select_websites.html', context)

def create_website(request):
    if request.method == 'POST':
        website_form = WebsiteForm(request.POST)
        if website_form.is_valid():
            title = website_form.cleaned_data["title"]
            url = website_form.cleaned_data["url"]
            query_prefix = website_form.cleaned_data["query_prefix"]
            position_query = website_form.cleaned_data["position_query"]
            location_query = website_form.cleaned_data["location_query"]
            postings_element = website_form.cleaned_data["postings_element"]
            postings_class_or_id = website_form.cleaned_data["postings_class_or_id"]
            posting_url_element = website_form.cleaned_data["posting_url_element"]
            posting_url_class_or_id = website_form.cleaned_data["posting_url_class_or_id"]
            posting_title_element = website_form.cleaned_data["posting_title_element"]
            posting_title_class_or_id = website_form.cleaned_data["posting_title_class_or_id"]
            posting_company_element = website_form.cleaned_data["posting_company_element"]
            posting_company_class_or_id = website_form.cleaned_data["posting_company_class_or_id"]
            posting_location_element = website_form.cleaned_data["posting_location_element"]
            posting_location_class_or_id = website_form.cleaned_data["posting_location_class_or_id"]
            Website.objects.create(
                title=title,
                url=url,
                query_prefix=query_prefix,
                position_query=position_query,
                location_query=location_query,
                postings_element=postings_element,
                postings_class_or_id=postings_class_or_id,
                posting_url_element=posting_url_element,
                posting_url_class_or_id=posting_url_class_or_id,
                posting_title_element=posting_title_element,
                posting_title_class_or_id=posting_title_class_or_id,
                posting_company_element=posting_company_element,
                posting_company_class_or_id=posting_company_class_or_id,
                posting_location_element=posting_location_element,
                posting_location_class_or_id=posting_location_class_or_id
            )
            return redirect('jobs:select_websites')
    else:
        website_form = WebsiteForm()

    context = {
        "website_form": website_form
    }

    return render(request, 'test_results/create_website.html', context)

def update_website(request, id):
    website = Website.objects.get(pk=id)

    if request.method == 'POST':
        website_form = WebsiteForm(request.POST, instance=website)
        if website_form.is_valid():
            website.save()
    else:
        website_form = WebsiteForm(instance=website)

    context = {
        "website": website,
        "website_form": website_form
    }

    return render(request, 'test_results/update_website.html', context)


def delete_website(request, id):
    website = Website.objects.get(pk=id)
    website.delete()

    return redirect('jobs:select_websites')

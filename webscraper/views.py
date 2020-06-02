from django.shortcuts import render
from .models import Job
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from webscraper.models import Job, Website
from jobinator.models import Jobinator

# Create your views here.
def index(request):
    def search_websites(website, fn_position, fn_location):
        website_url = website.url
        query_prefix = website.query_prefix
        position_query = website.position_query + fn_position.replace(' ','-')
        location_query = website.location_query + fn_location.replace(' ','-')
        query = query_prefix + position_query + location_query
        complete_url = website_url + query

        # open url
        html = urlopen(complete_url)

        # convert to soup
        soup = BeautifulSoup(html, 'html.parser')

        # grab all postings
        postings = soup.find_all(website.postings_element,
                                class_=website.postings_class_or_id)

        print(website.title)
        for p in postings:
            try:
                url = p.find(website.posting_url_element,
                        class_=website.posting_url_class_or_id).find('a')['href']
                if "https" not in url:
                    url = website.url + url
            except:
                url = ''
            try:
                title = p.find(website.posting_title_element,
                        class_=website.posting_title_class_or_id).text
            except:
                title = ''
            try:
                company = p.find(website.posting_company_element,
                        class_=website.posting_company_class_or_id).text
            except:
                company = ''
            try:
                location = p.find(website.posting_location_element,
                        class_=website.posting_location_class_or_id).text
            except:
                location = ''
            try:
                salary = p.find('span', class_='salaryText').text
            except:
                salary = ""
            try:
                remote = p.find('span', class_='remote').text
            except:
                remote = ""
            try:
                summary = p.find('div', class_='summary').text
            except:
                summary = ""
            print(title)
            # check if url in db
            try:
                # save in db
                Job.objects.create(
                url=url,
                website_title=website.title,
                title=title,
                company=company,
                location=location,
                salary=salary,
                remote=remote,
                summary=summary
                )
            except:
                pass

    if request.method == 'POST':
        job_alerts = Jobinator.objects.filter(active=True)
        websites = Website.objects.all()
        for job_alert in job_alerts:
            for website in websites:
                search_websites(website, job_alert.position, job_alert.location)

    return render(request, 'webscraper/index.html')

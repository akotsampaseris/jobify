from django.shortcuts import render
from .models import Job
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from webscraper.models import Job
from jobinator.models import Jobinator

# Create your views here.
def index(request):
    def search_indeed(fn_position, fn_location):
        url = 'https://indeed.com/'
        query = 'jobs?q='
        position_keywords = fn_position.replace(' ','-')
        query += position_keywords
        query += '&l='
        location_query = fn_location.replace(' ','-')
        query += location_query
        complete_url = url + query

        # open url
        html = urlopen(complete_url)

        # convert to soup
        soup = BeautifulSoup(html, 'html.parser')

        # grab all postings
        postings = soup.find_all("div", class_="jobsearch-SerpJobCard")


        for p in postings:
            url = p.find('a', class_='jobtitle')['href']
            title = p.find('a', class_='jobtitle').text
            company = p.find('span', class_='company').text
            location = p.find('span', class_='location').text
            try:
                salary = p.find('span', class_='salaryText').text
            except:
                salary = ""
            try:
                remote = p.find('span', class_='remote').text
            except:
                remote = ""
            summary = p.find('div', class_='summary').text
            print(title)
            # check if url in db
            try:
                # save in db
                Job.objects.create(
                url=url,
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
        if len(job_alerts)<1:
            print("No job alerts!")
        else:
            for job_alert in job_alerts:
                search_indeed(job_alert.position, job_alert.location)

    return render(request, 'webscraper/index.html')

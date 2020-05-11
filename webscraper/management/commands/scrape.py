from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from webscraper.models import Job

class Command(BaseCommand):
    help = "collect jobs"

    # define logic of command

    def handle(self, *args, **options):
        # collect html

        url = 'https://indeed.com/'
        query = 'jobs?q='
        position_keywords = 'python'
        query += position_keywords
        query += '&l='
        location_query = 'california'
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
            print(summary)

            # check if url in db
            try:
                Job.objects.create(
                url=url,
                title=title,
                company=company,
                location=location,
                salary=salary,
                remote=remote,
                summary=summary
                )
                # save in db
                print('%s added' % (title,))
            except:
                print('error')

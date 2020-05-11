from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#from models import Job

#def find_indeed_postings(position_query, location_query):
# collect html
website = 'https://indeed.com'
query = '/jobs?q='
position_keywords = 'python+developer'
query += position_keywords
query += '&l='
#location_query = location_query.lower()
location_query = 'california'
query += location_query
complete_url = website + query

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

    # check if url in db
    try:
        # save in db
        Job.objects.create(
            url=url,
            title=title,
            company=company,
            location=location
        )
    except:
        print(title)
        print(website+url)
        print(company)
        print(location)

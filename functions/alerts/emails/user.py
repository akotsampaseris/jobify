from django.core.mail import EmailMessage

def job_notification_alert():
    email =  EmailMessage('New notifications!',
              'There are several jobs relevant to your search!',
              '"Jobify | Find your dream job" <a.kotsampaseris@technologic.gr>',
              ['a.kotsampaseris@gmail.com'])
    email.send()

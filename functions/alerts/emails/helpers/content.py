from django.core.mail import EmailMultiAlternatives


# Helper Functions
def read_content(template, filename):
    html = open(template + 'html/' + filename + '.html', 'r').read()
    text = open(template + 'text/' + filename + '.txt', 'r').read()

    content = {
        "html": html,
        "text": text
    }

    return content


def send_message(subject, content, from_email, to, subject_prefix=''):
    if subject_prefix != '':
        subject = subject_prefix + ' ' + subject

    message = EmailMultiAlternatives(subject, content["text"], from_email, to)
    message.attach_alternative(content["html"], "text/html")
    message.send(fail_silently=False)

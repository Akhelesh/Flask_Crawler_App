import sendgrid
import os
from sendgrid.helpers.mail import *
from flask import url_for
from pycrawler import app


def send_email(email, name):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("noreply@pycrawler.com")
    subject = 'Crawl Complete View the Results'
    to_email = Email(email)
    with app.test_request_context():
        url = url_for('results.show_results', domain_name=name,
                      _external=True)
    content = Content("text/plain", 'The crawl for your requested domain is complete. To view the results visit the following link:' +
                      url + '''
                         If you did not make this request please ignore this email.''')

    mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=mail.get())
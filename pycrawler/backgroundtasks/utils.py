from flask import render_template, url_for
from flask_mail import Message
from pycrawler import mail, app


def send_email(email, name):
    print(name)
    with app.test_request_context():
        msg = Message('Crawl Complete View the Results',
                      sender='noreply@pycrawler.com',
                      recipients=[email])
        msg.body = f'''The crawl for your requested domain is complete. To view the results visit the following link:
{url_for('results.show_results', domain_name=name, _external=True)}

If you did not make this request please ignore this email.
'''
        mail.send(msg)

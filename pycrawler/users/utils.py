import os
import sendgrid
from sendgrid.helpers.mail import *
import secrets
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
    rand_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = rand_hex + f_ext
    picture_path = os.path.join(current_app.root_path,
                                'static/profile_pics', picture_fn)
    output_size = [125, 125]
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("noreply@pycrawler.com")
    subject = 'Password Reset Request'
    to_email = Email(user.email)
    url = url_for('users.reset_token', token=token, _external=True)
    content = Content("text/plain", 'To reset your password visit the following link:' +
                      url + '''
                         If you did not make this request please ignore this email.''')

    mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=mail.get())

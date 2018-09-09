import re
from urllib.parse import urlparse
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class SubmitDomainForm(FlaskForm):
    domain = StringField('Domain', validators=[DataRequired()])
    submit = SubmitField('Crawl')

    def validate_domain(self, domain):
        url_regex = r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
        regex = re.compile(url_regex)
        try:
            url = regex.match(domain.data).group()
            parsed_url = urlparse(url)
            if parsed_url.netloc:
                domain.data = 'http://' + parsed_url.netloc + '/'
            else:
                domain.data = 'http://' + parsed_url.path.split('/')[0]\
                              + '/'
        except AttributeError:
            raise ValidationError('Please enter a valid URL.')

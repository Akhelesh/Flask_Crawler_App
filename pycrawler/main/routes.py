from tldextract import extract
from flask import flash, url_for, redirect, render_template, Blueprint
from flask_login import current_user
from pycrawler.forms import SubmitDomainForm
from pycrawler.models import Domain
from pycrawler.backgroundtasks.tasks import run_crawler

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = SubmitDomainForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You must login to crawl a website. Please ' +
                  'register if you do not have an account.', 'warning')
            return redirect(url_for('users.login'))
        submitted_domain = extract(form.domain.data).domain
        domain = Domain.query.filter_by(domain_name=submitted_domain)\
            .first()
        if domain:
            flash('The requested domain has already been crawled.',
                  'info')
            return redirect(url_for('results.show_results',
                            domain_name=submitted_domain))
        flash('The website is being crawled. You will get an email ' +
              'when the crawl is complete.', 'info')
        run_crawler.delay(current_user.email, form.domain.data,
                          extract(form.domain.data).domain.lower())
    return render_template('home.html', title='Crawler', form=form,
                           legend='Enter a Domain to Crawl')

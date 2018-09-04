from flask import flash, render_template, Blueprint
from pycrawler.forms import SubmitDomainForm
from backgroundtasks.tasks import run_crawler

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = SubmitDomainForm()
    if form.validate_on_submit():
        flash(f'You entered {form.domain.data}', 'info')
        run_crawler.delay(form.domain.data, form.crawler_name.data)
    return render_template('home.html', title='Crawler', form=form,
                           legend='Enter a Domain to Crawl')

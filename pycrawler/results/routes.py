from flask import flash, redirect, url_for, render_template, Blueprint
import pygal
from pygal.style import LightColorizedStyle
from pycrawler.models import Domain
from pycrawler.results.utils import *

results = Blueprint('results', __name__)


@results.route("/crawled/<domain_name>")
def show_results(domain_name):
    domain = Domain.query.filter_by(domain_name=domain_name).first()
    if domain is None:
        flash('The website has not been crawled yet. Please enter ' +
              'the domain to crawl.', 'warning')
        return redirect(url_for('main.home'))
    crawled, external = get_links(domain.domain_name)
    ext_domains = get_unique_domains(external)
    pie_chart = pygal.Pie(inner_radius=.70, style=LightColorizedStyle)
    pie_chart.title = 'Internal vs External'
    pie_chart.add('Internal', len(crawled))
    pie_chart.add('External', len(external))
    chart_data = pie_chart.render_data_uri()
    return render_template('results.html', title='Results',
                           chart_data=chart_data, crawled=crawled,
                           external=external, ext_domains=ext_domains)

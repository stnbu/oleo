import time
import datetime
import pytz
import coincharts

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Page, Content

from gitbored.views import get_grouped_commits
import svg_graph
from coincharts import config as coincharts_config
from coincharts import data as coincharts_data

coincharts_config = coincharts_config.get_config()

def get_coincharts_graph():
    one_week_ago = datetime.datetime.fromtimestamp(
        time.time() - 7 * 24 * 60 * 60,
        tz=pytz.UTC).strftime(coincharts_data.date_format_template)
    symbols = coincharts_config['history_symbols']
    comparison = coincharts_data.SymbolComparison()
    for symbol in symbols:
        comparison[symbol] = coincharts_data.SymbolInfo(symbol, since=one_week_ago)
    average_historical_price_generator = comparison.normalized_history_averages()
    eth = comparison.pop('BITSTAMP_SPOT_ETH_USD')
    eth_points = svg_graph.Points(eth.normalized_history)
    eth_points.color = 'green'  # cannot Points(foo, color='bar') with py < 3.7
    average_points = svg_graph.Points(average_historical_price_generator)
    average_points.color = 'black'
    graph = svg_graph.LineGraph(
        title='Price history average comparison',
        height=420,
        width=1000,
        points_set=[
            eth_points,
            average_points,
        ],
    )
    return graph.to_xml()

def page(request, current_page_name):
    
    pages = Page.objects.order_by('weight')
    current_page = Page.objects.get(name=current_page_name)
    content = get_object_or_404(Content, page=current_page)
    context = {
        'current_page': current_page,
        'content': content,
        'pages': pages,
    }

    # a one-off... TBD
    if current_page_name == 'portfolio':
        repos_list = get_grouped_commits()
        context['repos_list'] = repos_list

    # two-off
    if current_page_name == 'coincharts':
        print('yes at coincharts')
        context['coin_chart'] = get_coincharts_graph()

    return render(request, 'main/index.html', context)

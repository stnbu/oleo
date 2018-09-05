from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Page, Content

from gitbored.views import get_grouped_commits

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

    return render(request, 'main/index.html', context)

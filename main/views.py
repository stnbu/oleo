from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Page, Content

def page(request, current_page_name):
    pages = Page.objects.order_by('weight')
    current_page = Page.objects.get(name=current_page_name)
    content = get_object_or_404(Content, page=current_page)
    context = {}
    return render(request, 'main/index.html', context)

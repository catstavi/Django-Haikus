from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from syllabize_db.models import Word

def index(request):
    line1 = Word.buildLine(5)
    line2 = Word.buildLine(7)
    line3 = Word.buildLine(5)
    template = loader.get_template('syllabize_db/index.html')
    context = RequestContext(request, {
        'line1': line1,
        'line2': line2,
        'line3': line3,
    })
    return HttpResponse(template.render(context))

# Create your views here.

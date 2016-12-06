from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.template import loader

from django.template.context import RequestContext

from django.views.generic import TemplateView
# Create your views here.


def index(request):
    template = loader.get_template('alpha/index.html')
    return HttpResponse(template.render(request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def profile_photo_page(request, user_id_name):
    return HttpResponse("Hello, %s" % user_id_name)


# def home(request):
#     context = RequestContext(request,
#                              {'user': request.user})
#     return render_to_response('templates/alpha/home.html',
#                               context_instance=context)


class HomePageView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'alpha/index.html', context=None)
    template_name = 'alpha/index.html'


class AboutPageView(TemplateView):
    template_name = 'alpha/about.html'


def post_list(request):
    return render(request, 'alpha/post_list.html')

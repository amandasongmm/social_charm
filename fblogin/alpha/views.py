from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.template import loader

from django.template.context import RequestContext
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Post

from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from django.shortcuts import redirect

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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'alpha/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'alpha/post_detail.html', {'post': post})


def profile(request):
    return render_to_response('alpha/profile_view.html', RequestContext(request))


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'alpha/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'alpha/post_edit.html', {'form': form})


def result_display(request):
    return render(request, 'alpha/result_analysis.html', context=None)


# def rate_display(request):
#     return render(request, 'alpha/rate_people.html', context=None)


def home_page(request):
    return render(request, 'alpha/home.html', context=None)


def self_rate(request):
    return render(request, 'alpha/rate_self.html', context=None)


def rate_other(request):
    return render(request, 'alpha/rate_others.html', context=None)


def rate_other2(request):
    return render(request, 'alpha/rate_others2.html', context=None)


def rate_other3(request):
    return render(request, 'alpha/rate_others3.html', context=None)


def rate_other4(request):
    return render(request, 'alpha/rate_others4.html', context=None)


def rate_other5(request):
    return render(request, 'alpha/rate_others5.html', context=None)



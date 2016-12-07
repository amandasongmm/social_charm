from django.conf.urls import url
from . import views

__author__ = 'amanda'

urlpatterns = [
    # ex: /alpha/
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about/', views.AboutPageView.as_view()),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^profile/', views.profile, name='profile_page'),
    # url(r'index/$', views.index, name='index'),
    # # ex: /alpha/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /alpha/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /alpha/5/vote/
    # url(r'^(P<questio_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
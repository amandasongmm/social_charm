from django.conf.urls import url
from . import views

__author__ = 'amanda'

urlpatterns = [
    # ex: /alpha/
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^$', views.post_list, name='post_list'),

    # Home page: starting page
    url(r'^$', views.home_page, name='home_page'),

    # After login in, first page, rate your self
    url(r'^self_rate/$', views.self_rate, name='self_rate'),

    # After rated yourself, jump to rate others' page.
    url(r'^rate_others/1/$', views.rate_other, name='rate_other'),
    url(r'^rate_others/2/$', views.rate_other2, name='rate_other2'),
    url(r'^rate_others/3/$', views.rate_other3, name='rate_other3'),
    url(r'^rate_others/4/$', views.rate_other4, name='rate_other4'),
    url(r'^rate_others/5/$', views.rate_other5, name='rate_other5'),


    url(r'^about/', views.AboutPageView.as_view()),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^profile/', views.profile, name='profile_page'),
    url(r'^result/', views.result_display, name='result_show'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    # url(r'^rate/', views.rate_display, name='rate_page'),

    # url(r'index/$', views.index, name='index'),
    # # ex: /alpha/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /alpha/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /alpha/5/vote/
    # url(r'^(P<questio_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

from django.conf.urls import url
from posts import views

# SET THE NAMESPACE!
app_name = 'posts'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^hirek/$',views.HirekListView.as_view(),name='hirek'),
    url(r'^programok/$',views.ProgramListView.as_view(),name='programok'),
    url(r'^tamogatok/$',views.TamogatokListView.as_view(),name='tamogatok'),
    url(r'^programok/(?P<pk>[-\w]+)/$',views.ProgramokDetailView.as_view(),name = 'program_detail'),
    url(r'^hirek/(?P<pk>[-\w]+)/$',views.HirekDetailView.as_view(),name = 'hirek_detail'),
    ]

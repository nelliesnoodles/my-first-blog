from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('language', views.language, name='SET_language'),  #<-- session change 6
    path('blog', views.blog_list, name='blogger'),
    path('wiwa', views.wiwa_page, name='wiwa'),
    path('wiwa_respond', views.wiwa_answer, name='responses'),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language, name="re-matchSETlanguage"), #<---session change 10
]

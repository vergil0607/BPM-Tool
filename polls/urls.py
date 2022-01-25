from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    path('base/', views.base, name="home"),
    path('processes/', views.processes, name="processes"),
    path('data/', views.data, name="data"),
    path('newdata/', views.newData, name="newdata"),
    path('home/', views.home, name="home"),
    path('analytics/', views.analytics, name="analytics"),
    path('dev/', views.dev, name="dev")
]

from portfolio_app import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('facts', views.facts),
    path('facts_submit', views.factsSubmit)
]

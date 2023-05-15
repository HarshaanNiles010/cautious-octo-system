from django.urls import path
from . import views

#url config module
urlpatterns = [
    path('',views.trial_messaage,name="Trial")
]
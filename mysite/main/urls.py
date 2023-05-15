from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_hello,name="render_hello")
]

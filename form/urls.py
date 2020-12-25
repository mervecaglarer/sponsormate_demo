from django.urls import path
from form import views as form_views

urlpatterns = [
    path('', form_views.responseform)
]


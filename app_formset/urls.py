# -*- coding: utf-8 -*-

from django.urls import path

from .views import FormSetView

app_name = 'app_formset'

urlpatterns = [
    path('', FormSetView.as_view(), name='formset')
]

# -*- coding: utf-8 -*-


from django import forms


class TestForm(forms.Form):
    title = forms.CharField(label='Title', min_length=5)
    description = forms.CharField(label='Description', max_length=10)

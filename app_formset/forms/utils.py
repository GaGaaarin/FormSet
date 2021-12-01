# -*- coding: utf-8 -*-

from django.forms.utils import ErrorList


class EmptyErrorList(ErrorList):
    def __str__(self):
        return ''

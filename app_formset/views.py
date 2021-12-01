# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.forms.formsets import formset_factory
from django.forms.utils import ErrorList

from .forms.forms import TestForm
from .forms.formsets import TestFormSet
from .forms.utils import EmptyErrorList


class FormSetView(TemplateView):
    template_name = 'app_formset/formset.html'

    FORMSET = formset_factory(form=TestForm,
                              formset=TestFormSet,
                              extra=0,
                              min_num=1,
                              validate_min=True,
                              can_delete=True,
                              can_delete_extra=True)

    def get_context_data(self, request=None, initial=None, error_class=ErrorList, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.FORMSET(request, initial=initial, error_class=error_class)
        return context

    def post(self, request):

        if 'send_form' in request.POST:
            formset = self.FORMSET(request.POST)
            if formset.is_valid():
                # Do something with data.
                pass
            else:
                context = self.get_context_data(request=request.POST)

        elif 'field_add' in request.POST:
            request_post = request.POST.copy()
            request_post['form-TOTAL_FORMS'] = int(request_post['form-TOTAL_FORMS']) + 1
            context = self.get_context_data(request=request_post, error_class=EmptyErrorList)

        elif 'delete' in request.POST:
            formset = self.FORMSET(request.POST, error_class=EmptyErrorList)
            initial = [form.cleaned_data for form in formset.not_deleted_forms]
            context = self.get_context_data(initial=initial)

        return render(request, self.template_name, context)

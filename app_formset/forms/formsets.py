# -*- coding: utf-8 -*-

from django.forms.formsets import BaseFormSet


class TestFormSet(BaseFormSet):

    def __init__(self, *args, **kwargs):
        super(TestFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    @property
    def not_deleted_forms(self):
        """Return a list of forms that have not been marked for deletion."""
        self.is_valid()

        if not hasattr(self, '_not_deleted_form_indexes'):
            self._not_deleted_form_indexes = []
            for i, form in enumerate(self.forms):
                if i >= self.initial_form_count() and not form.has_changed():
                    self._not_deleted_form_indexes.append(i)
                elif self._should_delete_form(form):
                    continue
                else:
                    self._not_deleted_form_indexes.append(i)

        return [self.forms[i] for i in self._not_deleted_form_indexes]
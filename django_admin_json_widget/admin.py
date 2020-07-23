from django.contrib import admin
from django import forms

from .widgets import SimpleJSONEditorWidget
from .models import *


class TestModelAdminForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
        widgets = {
            'json_field': SimpleJSONEditorWidget(),
        }


@admin.register(TestModel)
class TestModelModelAdmin(admin.ModelAdmin):
    form = TestModelAdminForm

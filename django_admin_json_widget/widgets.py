from json import loads, dumps

from django.forms import widgets


class BaseJSONEditorWidget(widgets.Textarea):

    def format_value(self, value):
        if isinstance(value, dict):
            return value

        try:
            while isinstance(value, str):
                value = loads(value)
        except Exception:
            return {}
        else:
            return value


class SimpleJSONEditorWidget(BaseJSONEditorWidget):

    template_name = 'django_admin_json_widget/json_editor.html'

    def __init__(self, attrs=None):
        import ipdb;ipdb.set_trace()
        self.input_name_str = ''
        self.input_id_str = ''
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        value = context['widget']['value']

        # context['values'] = {i: (f'id_{i}', f'id_source_{i}', value.get(i, {})) for i, _ in organisationImageType}
        return context

    def value_from_datadict(self, data, files, name):
        formatted_data = {}
        # for i, _ in organisationImageType:
        #     if data.get(f'name_{i}', '') and data.get(f'name_source_{i}', ''):
        #         formatted_data[i] = {'id': data[f'name_{i}'], 'source': data[f'name_source_{i}']}
        return formatted_data

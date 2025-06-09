from django import forms
from .models import Config, ConfigLog

class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'  # Include all fields of the Contract model

class ConfigLogForm(forms.ModelForm):
    class Meta:
        model = ConfigLog
        fields = '__all__'  # Include all fields of the Contract model

    def __init__(self, *args, **kwargs):
        super(ConfigLogForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
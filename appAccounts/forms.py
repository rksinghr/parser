from django import forms
# from .models import Lead
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# class LeadForm(forms.ModelForm):
#     class Meta:
#         model = Lead
#         fields = '__all__'

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(email=username)
            self.cleaned_data['username'] = user.username
        except User.DoesNotExist:
            pass
        return super().clean()

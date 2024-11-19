from django import forms
from .models import Profile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_telegram(value):
    regex = r'^@[a-zA-Z0-9]+(_?[a-zA-Z0-9]+)*$'
    if not re.match(regex, value):
        raise ValidationError(
            _("Поле Telegram должно начинаться с '@', содержать только латинские буквы и цифры, может содержать символ '_', но не сразу после '@'."),
            params={'value': value},
        )

class ProfileForm(forms.ModelForm):
    telegram = forms.CharField(
        validators=[validate_telegram]
    )

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'photo': 'Фото',
            'telegram': 'Телеграм',
            'city': 'Город',
            'profession': 'Профессия',
            'bio': 'О себе',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


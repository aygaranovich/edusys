from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
from django.core.files.images import get_image_dimensions
from django import forms
from .models import Students, Teachers


class RenewDeadlineForm(forms.Form):
    ddline = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_ddline(self):
        data = self.cleaned_data['ddline']

        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        #except AttributeError:

            #pass

        return avatar
"""
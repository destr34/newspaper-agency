from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from news_agency.models import Redactor, Newspaper


class CreateRedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CreateNewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Newspaper
        fields = (
            "title",
            "topic",
            "publishers",
            "content",
        )


from django.forms import ModelForm, Form, CharField, ChoiceField
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]


class NoteSearchForm(Form):
    SEARCH_BY_CHOICES = [
        ('contains', 'contains'),
        ('exact match', 'exact match'),
    ]

    title = CharField(required=False)
    title_search_by = ChoiceField(choices=SEARCH_BY_CHOICES)
    body = CharField(required=False)
    body_search_by = ChoiceField(choices=SEARCH_BY_CHOICES)

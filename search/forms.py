from django import forms

class SearchForm(forms.Form):

    SEARCH_FILTERS = (
        ('id', 'id'),
        ('title', 'title'),
        ('user', 'user')
    )

    search = forms.CharField(
        max_length = 100
    )

    filters = forms.ChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = SEARCH_FILTERS
    )



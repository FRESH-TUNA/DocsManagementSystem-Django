from django import forms

class DocumentForm(forms.Form):
    class Meta:
        model = Document
        field = ('category', 'content', 'url')
        
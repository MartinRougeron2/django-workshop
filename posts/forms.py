from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(label="My thoughts")


class BirddyForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField()

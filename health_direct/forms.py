from django import forms

class QuestionForm(forms.Form):
	question = forms.CharField(widget=forms.Textarea)
	response1 = forms.CharField()
	response2 = forms.CharField()
	response3 = forms.CharField(required=False)
	response4 = forms.CharField(required=False)

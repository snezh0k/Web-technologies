from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 200)
    text = forms.CharField(widget = forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("No title.")
        return title
        
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError("No text.")
        return text
    
    def clean(self):
        if not self.cleaned_data:
            raise forms.ValidationError("Can't submit.")
        return self.cleaned_data

    def save(self):
        return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField()
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError("You need to write something.")
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise forms.ValidationError("Question ID error - No such question.")
        return question

    def clean(self):
        if not self.cleaned_data:
            raise forms.ValidationError("You can`t write empty answer.")
        return self.cleaned_data

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question'])
        return Answer.objects.create(**self.cleaned_data)

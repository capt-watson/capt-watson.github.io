from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:                 ## meta class is an inner class ued for modifying model fields behavior
        model = Topic           ## Tells django which model to base the forms on and which fields to include in form.
        fields = ['text']
        labels = {'text': ''}   ## Empty string tells django not to generate a label for the text field.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}  ## Its an HTML form element such as a single-line text box, multiline text area or drop-down list
        
        ## by including widget's attributes, one can override Django's default widget choices. Here the text area width is set to 80 iso default 40.

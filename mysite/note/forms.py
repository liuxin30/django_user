from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Note

class NoteForm(forms.Form):
    title = forms.CharField(label="标题", max_length=128)
    content = forms.CharField(label="内容", widget=CKEditorWidget(config_name='note_ckeditor'),)
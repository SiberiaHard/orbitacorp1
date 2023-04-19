from django import forms

class AppealForm(forms.Form):
    from_field = forms.CharField(label='От кого', max_length=100)
    to_field = forms.CharField(label='Кому', max_length=100)
    appeal_field = forms.CharField(label='Суть обращения', widget=forms.Textarea)
    legal_reference = forms.BooleanField(label='Ссылаться на законодательство Российской Федерации', required=False)
    document_reference = forms.BooleanField(label='Ссылаться на документ', required=False)
    document_text = forms.CharField(label='Текст документа', required=False, widget=forms.Textarea)
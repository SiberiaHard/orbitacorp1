from django.shortcuts import render
from django.http import HttpResponse
import openai
from .forms import AppealForm
import requests
from django.views import View


class GenerateAppealView(View):
    def get(self, request):
        form = AppealForm()
        return render(request, 'generate_appeal.html', {'form': form})

    def post(self, request):
        form = AppealForm(request.POST)
        if form.is_valid():
            from_field = form.cleaned_data['from_field']
            to_field = form.cleaned_data['to_field']
            appeal_field = form.cleaned_data['appeal_field']
            legal_reference = form.cleaned_data['legal_reference']
            document_reference = form.cleaned_data['document_reference']
            document_text = form.cleaned_data['document_text']

            prompt = f"Создай текст обращения длиной 2c500 символов на русском языке, от \"{from_field}\", к \"{to_field}\""
            if legal_reference:
                prompt += " ссылаясь на законодательство России с конкретными ссылками на законы"
            prompt += f", {appeal_field}"
            if document_reference and document_text:
                prompt += f", ссылаясь на документ \"{document_text}\""

            # Запрос к API chat GPT
            openai.api_key = "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"
            completions = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            generated_appeal = completions['choices'][0]['message']['content']

            return render(request, 'generate_appeal.html', {'form': form, 'generated_appeal': generated_appeal})
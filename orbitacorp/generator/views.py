import openai
from django.shortcuts import render

openai.api_key = "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"


def generator(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_info = request.POST['product_info']
        prompt = f'Создайте описание товара для интернет-магазина на русском языке длиной 750 символов, удобное для пользователей и SEO: {product_name} {product_info}'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        description = response['choices'][0]['message']['content']
        return render(request, 'generator.html', {'description': description})
    return render(request, 'generator.html')

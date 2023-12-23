from django.shortcuts import render, redirect
import requests
from .models import History


def home(request):
    if request.method == "GET":
        try:
            transfer_from = request.GET.get("TransferFrom")
            transfer_to = request.GET.get("TransferTo")
            amount = request.GET.get("amount")

            if not all([transfer_from, transfer_to, amount]):
                return render(request, 'exchange/home.html', {'error': 'Invalid input'})

            response = requests.get(
                f'https://v6.exchangerate-api.com/v6/e748db8ea98c1fdfb84567dc/pair/{transfer_from}/{transfer_to}/{amount}'
            )

            if response.status_code == 200:
                data = response.json()
                trfrom_flag = f"https://flagsapi.com/{transfer_from[:-1]}/flat/64.png"
                trto_flag = f"https://flagsapi.com/{transfer_to[:-1]}/flat/64.png"

                History.objects.create(
                    amount=amount,
                    TransferFrom=transfer_from,
                    conversion_result=data['conversion_result'],
                    TransferTo=transfer_to,
                )

                return render(request, 'exchange/home.html', {
                    'response': data['conversion_rate'],
                    'amount': data['conversion_result'],
                    'tr_from': trfrom_flag,
                    'tr_to': trto_flag,
                    'transfer_to': transfer_to,
                    'transfer_from': transfer_from
                })

            return render(request, 'exchange/home.html', {'error': 'API request failed'})

        except Exception as e:
            # Лучше логгировать ошибку для дальнейшей отладки
            print(f"Error: {e}")
            return render(request, 'exchange/home.html', {'error': 'An error occurred'})

    return redirect('home-page')


def exchange_history(request):
    return render(request, 'exchange/history.html', {'exchange':History.objects.all()})
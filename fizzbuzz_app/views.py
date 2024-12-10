from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


# Verificação do CRSF desativada para facilitar testes no curl
@csrf_exempt
@require_http_methods(["POST"])
def fizzbuzz_view(request):
    try:
        body = json.loads(request.body)
        if 'n' not in body:
            return JsonResponse({
                "error": "O parâmetro 'n' é obrigatório"
            }, status=400)

        try:
            n = int(body['n'])
        except (ValueError, TypeError):
            return JsonResponse({
                "error": "O valor de 'n' deve ser um número inteiro válido"
            }, status=400)

        if n < 0:
            return JsonResponse({
                "error": "O valor de 'n' deve ser maior ou igual a zero"
            }, status=400)

        fizzbuzz_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz_list.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz_list.append("Buzz")
            else:
                fizzbuzz_list.append(i)

        return JsonResponse({
            "resultado": fizzbuzz_list
        })

    except json.JSONDecodeError:
        return JsonResponse({
            "error": "JSON inválido ou malformado"
        }, status=400)

    except Exception as e:
        return JsonResponse({
            "error": f"Erro interno do servidor: {str(e)}"
        }, status=500)

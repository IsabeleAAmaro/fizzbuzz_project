from django.http import JsonResponse


def fizzbuzz_view(request):
    if request.method == "POST":
        import json
        # Extrair o valor de 'n' do corpo da requisição
        body = json.loads(request.body)
        n = body.get("n", 0)

        # Gerar a lista FizzBuzz
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

        # Retornar o resultado como JSON
        return JsonResponse({"resultado": fizzbuzz_list})

    # Caso não seja POST, retornar erro 405
    return JsonResponse({"error": "Method not allowed"}, status=405)

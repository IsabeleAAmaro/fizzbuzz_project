from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def fizzbuzz(request):
    try:
        n = int(request.data.get('n', 0))
        if n <= 0:
            return Response({"Erro": "O número deve ser um inteiro positivo."}, status=status.HTTP_400_BAD_REQUEST)

        result = [
            "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
            "Fizz" if i % 3 == 0 else
            "Buzz" if i % 5 == 0 else
            i
            for i in range(1, n + 1)
        ]
        return Response({"Resultado": result}, status=status.HTTP_200_OK)
    except (ValueError, TypeError):
        return Response({"Erro": "Entrada inválida. Envie um número inteiro positivo."},
                        status=status.HTTP_400_BAD_REQUEST)

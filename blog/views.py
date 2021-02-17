from django.shortcuts import render

# entendendo modelo de view e resposta em rotas
from django.http import HttpResponse


# função básica para primeira View
# http://127.0.0.1:8000/rotateste/
def Home(request):
    html = '<h1>Primeiro teste de Rota e View</h1>'
    return HttpResponse(html)


# entendendo modelo de view e resposta em rotas
from django.http import HttpResponse

from django.shortcuts import render
from .models import Post

# função básica para primeira View
# http://127.0.0.1:8000/rotateste/
def Home(request):
    html = '<h1>Primeiro teste de Rota e View</h1>'
    return HttpResponse(html)


# função que retorna a lista de postagens com status publish
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


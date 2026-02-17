from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

def home(request):
    busca = request.GET.get('busca', '')
    categoria_slug = request.GET.get('categoria', '')

    posts = Post.objects.all().order_by('-criado_em')

    if busca:
        posts = posts.filter(titulo__icontains=busca)

    if categoria_slug:
        posts = posts.filter(categoria__slug=categoria_slug)

    categorias = Categoria.objects.all()

    context = {
        'posts': posts,
        'categorias': categorias,
        'busca': busca,
    }

    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
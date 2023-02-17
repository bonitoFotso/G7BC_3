from .models import Category

# para utilizar no frontend o filtro de categorias
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
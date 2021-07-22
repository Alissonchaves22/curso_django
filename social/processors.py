from .models import Link

def cxt_social(request):
    cxt_dict = {}
    links = Link.objects.all()
    for link in links:
        cxt_dict[link.chave] = link.url
    return cxt_dict
    
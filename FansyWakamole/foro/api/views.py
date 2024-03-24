from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..models import Posts

def routes(request):
    routes = [
        'GET /api/posts',
        'GET /api/post/:id'
    ]
    
    return JsonResponse(routes, safe = False)

def posts(request):
    posts = Posts.objects.all()
    post_list = []
    for p in posts:
        post_dict = {
            
            'title': p.title,
            'Comentario': p.Comentario,
           
        }
        post_list.append(post_dict)

    return JsonResponse(post_list, safe=False)

def post(request, id):
    post = get_object_or_404(Posts, id=id)
    post_dict = {
        'title': post.title,
        'Comentario': post.Comentario,
        # Puedes agregar más campos según sea necesario
    }
    return JsonResponse(post_dict)
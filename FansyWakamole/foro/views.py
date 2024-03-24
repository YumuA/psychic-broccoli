from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Posts, Comentario
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Succes')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Login error')
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect("/")

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso')
            return redirect('/register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.name = name
            user.save()
            return redirect('/login')
        except IntegrityError:
            messages.error(request, 'Error al registrar el usuario')
            return redirect('/register')

    return render(request, 'registerPage.html')

def home(request):
    posts = Posts.objects.order_by('-created')
    return render(request, 'home.html', { 'posts' : posts })

def post(request, id = None):
    if request.method == 'POST':
        id = request.POST.get("id")
        if (id is None):
            title = request.POST.get('title')
            Comentario = request.POST.get('Comentario')
            image = request.FILES.get('image')  # Usa request.FILES para manejar archivos
            
            
            

        # Asegúrate de validar que image no sea None antes de crear el objeto
            if title and Comentario:
                Posts.objects.create(
                    title=title,
                    Comentario=Comentario,
                    image=image,
                    user=request.user
                )
            messages.success(request, 'Post creado correctamente')
            return redirect('/')
        
        else:
            p = Posts.objects.get(id = id)
            if (p.user == request.user):
                p.title = request.POST.get('title')
                p.Comentario = request.POST.get('Comentario')
                p.image = request.FILES.get('image') 
            p.save()
            return HttpResponseRedirect('/')
    
    context = {}

    if id is not None:
        p = Posts.objects.get(id = id)
        context['posts'] = p    

    return render(request, 'ej.html', context)



def editar_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    # Lógica para editar el post
    # ...

def borrar_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return redirect('/')


def comment(request):
    
    p = Posts.objects.get(id = request.POST.get('id'))
    Comentario.objects.create(
        text=request.POST.get('text'),
        user=request.user,
        post=p
    )
    return redirect('/')
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from .views import comment

urlpatterns = [
    path('', views.home),
    path('posts/', views.post),
    path('posts/<int:id>/', views.post),
    path('borrar_post/<int:post_id>/', views.borrar_post, name='borrar_post'),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('register/', views.registerPage),
    path('comment/', comment, name='comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
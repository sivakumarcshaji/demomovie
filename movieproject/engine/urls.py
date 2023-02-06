from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name = 'engine'

urlpatterns = [
    path('', views.movie, name='movie'),
    path('movie/<int:det>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('add/', views.addmovie, name='addmovie'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

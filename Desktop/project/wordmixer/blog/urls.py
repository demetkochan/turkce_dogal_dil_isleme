from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='kaydol'),
    path('anasayfa/', views.home, name='anasayfa'),
    path('duyguanalizi/', views.link1, name='duyguanalizi'),
    path('anahtarkelime/', views.link2, name='anahtarkelime'),
    path('özetleme/', views.link3, name='özetleme'),
    path('advarlık/', views.link4, name='advarlık'),
    path('sorucevap/', views.link5, name='sorucevap'),
    path('konutanım/', views.link6, name='konutanım'),
]

urlpatterns += staticfiles_urlpatterns()

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='kaydol'),
    path('anasayfa/', views.home, name='anasayfa'),
    path('duyguanalizi/', views.link1, name='duyguanalizi'),
    path('duyguanalizi/sonuc', views.sentiment, name='da_sonuc'),
    path('anahtarkelime/', views.link2, name='anahtarkelime'),
    path('anahtarkelime/sonuc', views.keywordExtraction, name='ke_sonuc'),
    path('özetleme/', views.link3, name='özetleme'),
    path('özetleme/sonuc', views.summarization, name='sum_sonuc'),
    path('advarlık/', views.link4, name='advarlık'),
    path('advarlık/sonuc', views.ner, name='ner_sonuc'),
    path('sorucevap/', views.link5, name='sorucevap'),
    path('sorucevap/sonuc', views.questionAnswer, name='qa_sonuc'),
    path('konutanım/', views.link6, name='konutanım'),
    path('konutanım/sonuc', views.categorization, name='cat_sonuc')
]

urlpatterns += staticfiles_urlpatterns()

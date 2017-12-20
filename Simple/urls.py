from django.urls import path
from Simple import views

app_name = 'Simple'

urlpatterns = [
    path('', views.home, name='index'),
    path('vigenere/', views.vigenere, name='vigenere'),
    # path('vigenere/<int:pk>/encrypt/results/',
    #      views.EncryptionResultsView.as_view(),
    #      name='vigenere_encrypt_results'),
    path('fizzbuzz/', views.fizzbuzz, name='fizzbuzz'),
    path('change/', views.change_machine, name='change_machine'),
]
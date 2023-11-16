from django.urls import path
from Account import views
urlpatterns = [
    path('payment/', views.payment)
]
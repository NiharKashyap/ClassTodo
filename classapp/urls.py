from django.urls import path
from .views import health_check, TodoView, LoginView



urlpatterns = [
    path('', health_check),
    path('form/', TodoView.as_view()),
    path('login/', LoginView.as_view())
    
]

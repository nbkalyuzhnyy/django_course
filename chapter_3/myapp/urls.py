from django.urls import path
from .views import ProfileFormView, SuccessView

urlpatterns = [
    path('profile/', ProfileFormView.as_view(), name='profile'),
     path('success/', SuccessView.as_view(), name='success'),
]


from django.urls import path
from .views import ResetPinRequestView

urlpatterns = [
    path('reset-pin/', ResetPinRequestView.as_view(), name='reset-pin'),
]
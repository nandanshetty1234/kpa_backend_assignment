# forms/urls.py
from django.urls import path
from .views import WheelSpecificationCreateView,WheelSpecificationListView

urlpatterns = [
    path('wheel-specifications', WheelSpecificationCreateView.as_view(), name='wheel-specifications'),
    path('wheel-specifications/list', WheelSpecificationListView.as_view(), name='wheel-specifications-list'),
]

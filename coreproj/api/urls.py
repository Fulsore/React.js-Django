from django.urls import path
from .views import FormView

urlpatterns = [
    path('form/',FormView.as_view(),name='form'),
    path('form/<int:id>/', FormView.as_view(), name='form_update'),
]
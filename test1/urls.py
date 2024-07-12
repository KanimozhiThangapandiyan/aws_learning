from django.urls import path
from .views import CountryListCreateView, CountryRetrieveUpdateDestroyView

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
]
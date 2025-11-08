from django.urls import path
from .views import get_accounts, create_account, account_detail

urlpatterns = [
    path('accounts/', get_accounts, name='get_accounts'),
    path('accounts/create/', create_account, name='create_account'),
    path('accounts/<int:pk>/', account_detail, name='account_detail')
]
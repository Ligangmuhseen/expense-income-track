from django.urls import path
from . import views
from .views import TransactionListAPIView



urlpatterns = [
    path('',views.index, name='index'),
    path('home', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('al/', views.viewitems, name='view-items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
    path('expense',views.expense, name='expense'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('api/transactions/', TransactionListAPIView.as_view(), name='transaction-list')


]












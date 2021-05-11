from django.urls import path
from . import views

urlpatterns = [
    path('<int:word_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('delete/<int:word_id>', views.delete, name="delete"),
    path('edit/<int:word_id>', views.edit, name="edit"),
    path('update/<int:word_id>', views.update, name="update"),
    path('search/', views.search, name="search"),
    path('filter/', views.filter, name="filter"),
]
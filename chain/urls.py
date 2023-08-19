from django.urls import path

from chain import views

app_name = "chain"

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('add-price', views.add_price, name="add_price"),
    path('add', views.add, name="add"),
    path('get_model_by_manufacture', views.get_model_by_manufacture, name="get_model_by_manufacture"),
    path('get_price_by_model', views.get_price_by_model, name="get_price_by_model")
]
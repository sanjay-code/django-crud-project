from django.urls import path
from crud import views
urlpatterns = [
    path('',views.HomeView,name="home"),
    path('add/',views.Add_Item,name="add"),
    path('count/',views.count_total,name="count"),
    path('edit/<int:id>',views.Edit_item,name="edit"),
    path('delete/<int:id>/',views.Delete_item,name="delete"),
    path('search/',views.Find_data,name="delete"),
]
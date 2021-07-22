from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    
    path('',views.IndexClassView.as_view(),name='index'),

    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
#to add items
    path('add',views.CreateItem.as_view(),name='create_item'),
#to update item
    path('update/<int:id>/',views.update_item,name='update_item'),
#to delete item
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

   
]

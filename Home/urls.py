from django.urls import path
from . import views
urlpatterns =[
    path('',views.index, name="index"),
    path('dhurba/',views.admin_index, name="admin_index"),
    path('add_item/',views.add_item, name="add_items"),
    path('update_item/<int:id>/',views.update_items, name="update_items"),
    path('delete_item/<int:id>/',views.delete_items, name="delete_items"),
    path('add_accessories/',views.add_accessories, name="add_accessories"),
    path('update_accessories/<int:id>/',views.update_accessories, name="update_accessories"),
    path('delete_accessories/<int:id>/',views.delete_accessories, name="delete_accessories"),
]
from django.urls import path
from apis.v1 import views

urlpatterns = [
    path('get_details',views.Rail_Details),
    path('get_data',views.Train_Table),
    path('update',views.update_Table),
    path('put',views.put_Table),
    path('delete',views.delete_rail),
    path('get_one/<int:T_Num>',views.Rail_Data)
]

# Railway_Details

## apis/v1/urls.py [folder]

|Route                  |   Views Function Names|
|-----------------------|----------------------:|
| 'get_details'         |  Rail_Details         |
| 'get_data'            |  Train_Table          |
| 'update'              |  update_Table         |
| 'put'                 |  put_Table            |
| 'delete'              |  delete_rail          |
| 'get_one/<int:T_Num>' |  Rail_Data            |

## apis/v1/views.py [folder]

##### Rail_Details
##### Train_Table
##### update_Table
##### put_Table
##### delete_rail
##### Rail_Data

## apis/v1/serilizers.py [folder]

#### from rest_framework.serializers import ModelSerializer
#### from Details.models import Train_Details

##### Trains (class name )
###### model=Train_Details
###### fields='__all__'

## Details --> models [APP]

| Attributes  | Models Fields  | Constraints     |
| ------------|:--------------:|----------------:|
| Train_No    | IntegerField   |          ()     |
|Train_Name   | CharField      | (max_length=50) |
| Source      | CharField      | (max_length=50) |
| Destination | CharField      | (max_length=50) |


## Root folder Main urls.py

##### from django.contrib import admin
##### from django.urls import path,include

##### urlpatterns = [
     path('admin/', admin.site.urls),
     path('apis/v1/',include('apis.v1.urls'))
     ]

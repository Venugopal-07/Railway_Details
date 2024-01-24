import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from Details.models import Train_Details
from apis.v1.serilizers import Trains


@csrf_exempt
def Rail_Details(request):
    if request.method=='GET':
        rail_data=Train_Details.objects.all()
        Trains_data=Trains(rail_data,many=True)
        if Trains_data.is_valid:
            return JsonResponse(Trains_data.data,safe=False)
        else:
            return JsonResponse('Error Occur')
    return HttpResponse('Invalid Tranis Data ') 

@csrf_exempt
def Train_Table(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        Trains_records=Trains(data=data)
        if Trains_records.is_valid():
            Trains_records.save()
            return JsonResponse(Trains_records.data,status=201)
        return JsonResponse(Trains_records.errors,status=400)
    return HttpResponse('Invalid Request Method')

@csrf_exempt
def update_Table(request):
    if request.method=='PATCH':
        table=JSONParser().parse(request)
        id=table.get('id')
        obj=Train_Details.objects.get(id=id)
        Trains_records=Trains(obj,data=table,partial=True)
        if Trains_records.is_valid():
            Trains_records.save()
            return JsonResponse(Trains_records.data,status=201)
        return JsonResponse(Trains_records.errors,status=400)
    return HttpResponse('Invalid Request Method')

@csrf_exempt
def put_Table(request):
    if request.method=='PUT':
        table=JSONParser().parse(request)
        PrimaryKey=table.get('id')
        obj=Train_Details.objects.get(id=PrimaryKey)
        Trains_records=Trains(obj,data=table)
        if Trains_records.is_valid():
            Trains_records.save()
            return JsonResponse(Trains_records.data,status=201)
        return JsonResponse(Trains_records.errors,status=400)
    return HttpResponse('Invalid Request Method')

@csrf_exempt
def delete_rail(request):
    if request.method=='DELETE':
        table=JSONParser().parse(request)
        PrimaryKey=table.get('id')
        obj=Train_Details.objects.get(id=PrimaryKey)
        obj.delete()
    return HttpResponse("Deleted Successfully")

@csrf_exempt
def Rail_Data(request,T_Num):
    if request.method=='GET':
        train_records=Train_Details.objects.get(Train_No=T_Num)
        train_data=Trains(train_records)
        if train_data.is_valid:
            return JsonResponse(train_data.data,status=201)
        return JsonResponse(train_data.errors,status=400)
    return HttpResponse('Invalid Data..')
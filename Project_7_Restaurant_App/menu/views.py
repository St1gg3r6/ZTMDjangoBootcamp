from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
# def item_list(request):
#     items = Item.objects.all()
#     item_list = [{'name': item.name, 'price': item.price, 'description': item.description} for item in items]
#     return JsonResponse({'menu_items': item_list})
@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

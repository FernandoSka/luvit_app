from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .serializers import ProductSerializer, ProductBulkSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Product

class ProductListCreate(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.all()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductBulkCreate(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductBulkSerializer
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        ser = ProductBulkSerializer(data=request.data)
        if ser.is_valid():
            return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
        ret_dict = {
            "status": "ERROR",
            "products_report": ser.errors,
            "number_of_products_unable_to_parse": 0
        }
        if ser.errors["products"] == ["This field is required."]:
            return Response(ret_dict, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        ret_dict["products_report"] = []
        counter = 0
        for error in ser.errors["products"]:
            counter+=1
            if error != {}:
                err_dic = {
                    "product_id": counter,
                    "errors": error
                }
                ret_dict["products_report"].append(err_dic)
                ret_dict["number_of_products_unable_to_parse"] += 1
        return Response(ret_dict, status=status.HTTP_422_UNPROCESSABLE_ENTITY)



# Create your views here.

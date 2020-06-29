from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'value', 'stock', 'discount_value']
    
    def validate(self, data):
        """
        Check that start is before finish.
        """
        if'discount_value' in data:
            if data['discount_value'] > data['value']:
                raise serializers.ValidationError("The discount value should be lower than value")
        return super(ProductSerializer, self).validate(data)


class ProductBulkSerializer(serializers.Serializer):

    products = ProductSerializer(many=True)

    def create(self, validated_data):
        products = [Product(**item) for item in validated_data["products"]]
        print(products)
        return Product.objects.bulk_create(products)

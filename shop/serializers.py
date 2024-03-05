from rest_framework import serializers

from shop.models import Category, Subcategory, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.Serializer):
    product_title = serializers.CharField()
    quantity = serializers.IntegerField()

    def validate(self, validated_data):
        try:
            product = Product.objects.get(title=validated_data['product_title'])
            return validated_data
        except Product.DoesNotExist:
            raise serializers.ValidationError('Такого продукта нет')

    def create(self, validated_data):
        product = Product.objects.get(title=validated_data['product_title'])
        return {
            'product': product,
            'quantity': validated_data['quantity']
        }



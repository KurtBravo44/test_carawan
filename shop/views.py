import json

from django.core.exceptions import ObjectDoesNotExist
from pytils.templatetags.pytils_translit import slugify
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category, Subcategory, Product
from shop.paginators import DefaultPaginator
from shop.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer, BasketSerializer
from users.models import User


# __Category Views__
class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_cat = serializer.save()
        new_cat.slug = slugify(new_cat.title)
        new_cat.save()


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = DefaultPaginator  # pagesize = 10


class CategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self, **kwargs):
        slug = self.kwargs['slug']
        obj = Category.objects.get(slug=slug)
        return obj


class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        slug = self.kwargs['slug']
        obj = Category.objects.get(slug=slug)
        return obj


# __Subcategory Views__
class SubcategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = SubcategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subcat = serializer.save()
        new_subcat.slug = slugify(new_subcat.title)
        new_subcat.save()


class SubcategoryListAPIView(generics.ListAPIView):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    pagination_class = DefaultPaginator  # pagesize = 10


class SubcategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    permission_classes = [IsAuthenticated]


    def get_object(self, **kwargs):
        slug = self.kwargs['slug']
        obj = Category.objects.get(slug=slug)
        return obj


class SubcategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Subcategory.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        slug = self.kwargs['slug']
        obj = Subcategory.objects.get(slug=slug)
        return obj


# __Product Views__
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        new_prod = serializer.save()
        new_prod.slug = slugify(new_prod.title)
        new_prod.save()


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = DefaultPaginator


# __Basket Views__
class BasketAddAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = str(request.data.get('product_id'))
        quantity = request.data.get('quantity')
        user_id = self.request.user.id
        user = User.objects.get(pk=user_id)
        basket_items = user.basket

        if product_id in basket_items.keys():
            basket_items[product_id] += quantity
        else:
            basket_items[product_id] = quantity

        user.basket = basket_items
        user.save()

        return Response(status=status.HTTP_201_CREATED)


class BasketRemoveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        product_id_request = data.get('product_id')
        user_id = self.request.user.id
        user = User.objects.get(pk=user_id)

        if not product_id_request:
            return Response({'error': 'Укажите id продукта'},
                            status=status.HTTP_400_BAD_REQUEST)

        basket_items = user.basket

        if str(product_id_request) in basket_items.keys():
            del basket_items[str(product_id_request)]
            user.basket = basket_items
            user.save()

            return Response({'message': 'Продукт удален из корзины'})

        return Response({'error': 'Продукт не найден в корзине'}, status=status.HTTP_404_NOT_FOUND)


class BasketListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        basket_items = self.request.user.basket
        products_in_basket = []
        total_price = 0
        for product_id, quantity in basket_items.items():
            product = Product.objects.get(id=product_id)
            products_in_basket.append({
                'product_id': product_id,
                'quantity': quantity,
            })
            if product.price:
                total_price += product.price
        return Response({'products': products_in_basket, 'total_price': total_price})

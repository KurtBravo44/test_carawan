from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryCreateAPIView, SubcategoryCreateAPIView, CategoryUpdateAPIView, CategoryListAPIView, \
    SubcategoryListAPIView, SubcategoryUpdateAPIView, CategoryDeleteAPIView, SubcategoryDeleteAPIView, \
    ProductCreateAPIView, ProductListAPIView, BasketRemoveAPIView, \
    BasketAddAPIView, BasketListAPIView

app_name = ShopConfig.name

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='list_category'),
    path('subcategory/', SubcategoryListAPIView.as_view(), name='list_subcategory'),
    path('products/', ProductListAPIView.as_view(), name='list_product'),

    path('create/category/', CategoryCreateAPIView.as_view(), name='create_category'),
    path('create/subcategory/', SubcategoryCreateAPIView.as_view(), name='create_subcategory'),

    path('update/category/<slug:slug>/', CategoryUpdateAPIView.as_view(), name='update_category'),
    path('update/subcategory/<slug:slug>/', SubcategoryUpdateAPIView.as_view(), name='update_subcategory'),

    path('delete/category/<slug:slug>/', CategoryDeleteAPIView.as_view(), name='delete_category'),
    path('delete/subcategory/<slug:slug>/', SubcategoryDeleteAPIView.as_view(), name='delete_subcategory'),

    path('create/product/', ProductCreateAPIView.as_view(), name='create_product'),

    path('basket/add/', BasketAddAPIView.as_view(), name='add_basket'),
    path('basket/remove/', BasketRemoveAPIView.as_view(), name='remove_basket'),
    path('basket/', BasketListAPIView.as_view(), name='list_basket')
]
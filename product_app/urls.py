from .views import add_product, view_all_product, delete_by_id, update_by_id, add_to_cart, view_cart, remove_from_cart
from django.urls import path,include

urlpatterns = [
    path("add_product", add_product),
    path("view_all_product",view_all_product),
    path("delete_by_id/<int:id>",delete_by_id),
    path("update_by_id/<int:id>",update_by_id),
    path("add_to_cart/<int:id>", add_to_cart),
    path("view_cart", view_cart),
    path("remove_from_cart/<int:id>", remove_from_cart),
]

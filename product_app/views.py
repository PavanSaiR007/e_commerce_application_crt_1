from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ProductModel,Cart

def add_product(request):
    # This function will take the data from the client and save in the db
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_price = request.POST.get('p_price')
        p_type = request.POST.get('p_type')
        p_quantity = request.POST.get('p_quantity')

        obj=ProductModel.objects.create(
            p_name=p_name,
            p_price=p_price,
            p_type=p_type,
            p_quantity=p_quantity
        )
        return render(request, 'success.html',
                  {"message": "Product added successfully"})
    return render(request, 'product_form.html')

def view_all_product(request):
    data = ProductModel.objects.all()
    print(list(data))
    return render(request, 'product_list.html', {'product_data': list(data)})


def delete_by_id(request, id):
    if request.method == "POST":
        data = ProductModel.objects.get(id=id)
        data.delete()
        return render(request, 'success.html', {'message': 'Product deleted successfully'})
    return render(request, 'product_list.html')

def update_by_id(request, id):
    product= ProductModel.objects.get(id=id)
    if request.method == "POST":
        product.p_name = request.POST.get('p_name')
        product.p_price = request.POST.get('p_price')
        product.p_type = request.POST.get('p_type')
        product.p_quantity = request.POST.get('p_quantity')
        product.save()
        return render(request, 'success.html', {'message': 'Product updated successfully'})
    return render(request, 'product_form.html')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ProductModel,Cart

def add_product(request):
    # This function will take the data from the client and save in the db
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_price = request.POST.get('p_price')
        p_type = request.POST.get('p_type')
        p_quantity = request.POST.get('p_quantity')

        obj=ProductModel.objects.create(
            p_name=p_name,
            p_price=p_price,
            p_type=p_type,
            p_quantity=p_quantity
        )
        return render(request, 'success.html',
                  {"message": "Product added successfully"})
    return render(request, 'product_form.html')

def view_all_product(request):
    data = ProductModel.objects.all()
    print(list(data))
    return render(request, 'product_list.html', {'product_data': list(data)})


def delete_by_id(request, id):
    if request.method == "POST":
        data = ProductModel.objects.get(id=id)
        data.delete()
        return render(request, 'success.html', {'message': 'Product deleted successfully'})
    return render(request, 'product_list.html')

def update_by_id(request, id):
    product= ProductModel.objects.get(id=id)
    if request.method == "POST":
        product.p_name = request.POST.get('p_name')
        product.p_price = request.POST.get('p_price')
        product.p_type = request.POST.get('p_type')
        product.p_quantity = request.POST.get('p_quantity')
        product.save()
        return render(request, 'success.html', {'message': 'Product updated successfully'})
    return render(request, 'product_form.html')


# ... (keep your add_product, view_all_product, delete_by_id, update_by_id exactly the same) ...

def add_to_cart(request, id):
    if request.method == "POST":
        product = ProductModel.objects.get(id=id)
        Cart.objects.create(
            product_id=product.id,
            p_price=product.p_price
        )
        return render(request, 'success.html', {'message': 'Product added to cart successfully!'})
    return HttpResponseRedirect('/product/view_all_product')


def view_cart(request):
    # Fetch all items in the cart
    cart_items = Cart.objects.all()
    valid_cart_items = []  # We will only send valid items to the HTML page

    for item in cart_items:
        try:
            # Try to find the matching product
            matching_product = ProductModel.objects.get(id=item.product_id)
            item.product_name = matching_product.p_name
            valid_cart_items.append(item)

        except ProductModel.DoesNotExist:
            # If the product was deleted from the main store,
            # delete it from the cart too so it stops crashing!
            item.delete()

    return render(request, 'cart_list.html', {'cart_data': valid_cart_items})


def remove_from_cart(request, id):
    if request.method == "POST":
        cart_item = Cart.objects.get(cart_id=id)
        cart_item.delete()
        return render(request, 'success.html', {'message': 'Product removed from cart successfully!'})
    return HttpResponseRedirect('/product/view_cart')
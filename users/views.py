from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from shop.models import Product
from users.models import Cart, Wishlist, Orders, Profile
from django.http import HttpResponseRedirect
import smtplib
from email.message import EmailMessage


def register(request):
    carx = None
    if request.user.is_authenticated:
	    carx = len(Cart.objects.filter(user=request.user))
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created. Log In to continue')
            return redirect('login')
    else:
        forms = UserRegisterForm()
    return render(request, 'users/register.html', {'form': forms, 'cart': carx})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form, 
        'cart': len(Cart.objects.filter(user=request.user))
    }
    return render(request, 'users/profile.html', context)


@login_required
def cart(request, idz, typer):
    mode = str(typer)
    id1 = int(idz)
    if mode == 'add':
        cart4 = Cart.objects.filter(product_id=id1, user=request.user)
        wish4 = Wishlist.objects.filter(product_id=id1, user=request.user)
        if not cart4:
            prod = Product.objects.get(pk=id1)
            cart1 = Cart()
            cart1.product_name = prod.product_name
            cart1.product_id = id1
            cart1.user = request.user
            cart1.image = prod.image
            cart1.price = prod.price
            cart1.quantity = 1
            cart1.category = prod.category
            cart1.subcategory = prod.subcategory
            cart1.save()
        else:
            cart1 = cart4.first()
            quan = cart1.quantity
            quan = quan + 1
            cart4.update(quantity=quan)
        if wish4:
            wish4.delete()
    elif mode == 'delete':
        cart3 = Cart.objects.filter(product_id=id1).first()
        if cart3:
            cart3.delete()
    elif mode == 'none':
        print('none')
        cart2 = Cart.objects.filter(user=request.user)
        sum1 = 0
        for car in cart2:
            sum1 = sum1 + car.price * car.quantity
        return render(request, 'users/cart.html', {'cart1': cart2, 'sum': sum1, 'cart':len(Cart.objects.filter(user=request.user))})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist(request, idz, typer):
    mode = str(typer)
    id1 = int(idz)
    if mode == 'add':
        wishlist4 = Wishlist.objects.filter(product_id=id1, user=request.user)
        if not wishlist4:
            prod = Product.objects.get(pk=id1)
            cart1 = Wishlist()
            cart1.product_name = prod.product_name
            cart1.product_id = id1
            cart1.user = request.user
            cart1.image = prod.image
            cart1.price = prod.price
            cart1.quantity = 1
            cart1.category = prod.category
            cart1.subcategory = prod.subcategory
            cart1.save()
        else:
            cart1 = wishlist4.first()
            quan = cart1.quantity
            quan = quan + 1
            wishlist4.update(quantity=quan)
    elif mode == 'delete':
        cart3 = Wishlist.objects.filter(product_id=id1).first()
        if cart3:
            cart3.delete()
    elif mode == 'none':
        print('none')
        cart2 = Wishlist.objects.filter(user=request.user)
        return render(request, 'users/wishlist.html', {'cart1': cart2, 'cart':len(Cart.objects.filter(user=request.user))})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def history(request):
    orders = Orders.objects.filter(user=request.user)
    sum = 0
    for order in orders:
        if order.product_name == 'default':
            order.price = sum
            sum = 0
        else:
            if not order.iscancelled:
                sum = sum + order.price
    return render(request, 'users/history.html', {'orders': orders})


@login_required
def cancel_order(request, idz):
    id1 = int(idz)
    order = Orders.objects.get(user=request.user, product_id=id1, iscancelled = False)
    order.iscancelled = True
    order.save()
    orders = Orders.objects.filter(user=request.user)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("myawesomecart@gmail.com", "MyAwesomeCart@123")
    msg = EmailMessage()
    subject = "The Stocked Pantry:Order Cancelled"
    message = "Dear " + str(request.user) + ", Your Order For the following Products is cancelled: "
    message = message + "\n"
    message = message + "Order:"
    message = message + "\n"
    message = message + f"Product : {order.product_name}\tQuantity: {order.quantity}\tPrice: {order.price}\n"
    message = message + '\n'
    message = message + "Total Price: " + str(order.price)
    message = message + "\n"
    message = message + " Thank you for using MyAwesomeCart.\n"
    msg.set_content(message)
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "myawesomecart@gmail.com"
    msg['To'] = request.user.email
    s.send_message(msg)
    s.quit()
    sum = 0
    for order in orders:
        if order.product_name == 'default':
            order.price = sum
            sum = 0
        else:
            if not order.iscancelled:
                sum = sum + order.price
    return render(request, 'users/history.html', {'orders': orders})


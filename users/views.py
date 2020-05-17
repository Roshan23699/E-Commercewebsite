from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from shop.models import Product
from users.models import Cart
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created. Log In to continue')
            return redirect('login')
    else:
        forms = UserRegisterForm()
    return render(request, 'users/register.html', {'form': forms})


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
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def cart(request, idz, typer):
    mode = str(typer)
    id1 = int(idz)
    if mode == 'add':
        cart4 = Cart.objects.filter(product_id=id1)
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
    elif mode == 'delete':
        cart3 = Cart.objects.filter(product_id=id1).first()
        if cart3:
            cart3.delete()
    elif mode == 'none':
        cart2 = Cart.objects.filter(user=request.user)
        sum1 = 0
        for car in cart2:
            sum1 = sum1 + car.price * car.quantity
        return render(request, 'users/cart.html', {'cart1': cart2, 'sum': sum1})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

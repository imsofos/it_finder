from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login, \
    logout as django_logout

from .forms import editProductForm


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return HttpResponse({
                    'msg':'You are logged in Will Redirect You To Admin Page',
                    'status':'1'
                    })
            else:
                return HttpResponse({
                    'msg':'invalid username and password',
                    'status':'0'
                    })
        return render(request, 'finder/login.html')
    return redirect('index')


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return redirect('login')


@login_required
def index(request):
    return render(request, 'finder/index.html')


@login_required
def search(request):
    if request.method == "POST" and request.is_ajax():
        searchInput = request.POST.get('searchInput')
        if len(searchInput) > 0:
            qs = Product.objects.filter(name__icontains=searchInput)
            #just select name and price
            qs_json = serializers.serialize('json', qs)
            return HttpResponse(qs_json, content_type='application/json')
        return HttpResponse({'code':'0'}, content_type='application/json')
    else:
        return HttpResponse('Please make sure the request method is POST and ajax')


@login_required
def getProduct(request, pk):
    if request.method == "POST" and request.is_ajax():
        product = Product.objects.filter(pk=pk)
        product_json = serializers.serialize('json', product)
        return HttpResponse(product_json, content_type='application/json')

@login_required
def editProduct(request, pk):
    context = {}
    product = get_object_or_404(Product, pk=pk)
    form = editProductForm(request.POST or None, instance = product)
    context["form"] = form
    if form.is_valid(): 
        form.save()
        return redirect('index')
    return render(request, "finder/editProduct.html", context)
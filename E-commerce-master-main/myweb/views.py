from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):
    
    my_products=Products.objects.all()
    print(my_products)
    n=len(my_products)
    
    # differentiating accorf=ding to the product category
    all_prod_lis=[]
    cat_prod=Products.objects.values('category')
    cats={item['category'] for item in cat_prod}
    for cat in cats:
        prod=Products.objects.filter(category=cat)
        n=len(prod)
        print("------",prod,"--------")
        all_prod_lis.append([prod,range(1,n)])
    
    paras={'to_pass_products':my_products,'range':range(n),'prod_lis':all_prod_lis}

    return render(request,'index.html',paras)

def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def tracker(request):
    return render(request,'tracker.html')
def search(request):
    return render(request,'search.html')
def checkout(request):
    return render(request,'checkout.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def login_merchant(request):
    return render(request,'login_merchant.html')
def login_customer(request):
    return render(request,'login_customer.html')
def Become_Seller(request):
    return render(request,'Become_Seller.html')
def reviews(request):
    return render(request,'reviews.html')
def trys(request):
    return render(request,'try.html')
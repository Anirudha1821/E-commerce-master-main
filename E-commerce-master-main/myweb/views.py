from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Products,Contact,Merchant
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform,productsform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# sign up view function 
# def sign_up(request):
#     if(request.method == 'POST'):
#         fm=signupform(request.POST)
#         if fm.is_valid():
#             messages.success(request,"Account created succesfully!!!!!!!")
#             fm.save()
#     else: 
#         fm=signupform()
#     return render(request,'sign_up.html',{'form':fm})

# # sign in view function 
# def login(request):
#     if(request.method == 'POST'):
#         fm=AuthenticationForm(request=request,data=request.POST)
#         if fm.is_valid():
#             uname=fm.cleaned_data['username']
#             upass=fm.cleaned_data['password']
#             user=authenticate(username='uname',password='upass')
#             if user is not None:
#                 login(request,user)
#                 return HttpResponseRedirect('/index/')

#             messages.success(request,"Login succesfully!!!!!!!")
#             fm.save()
#     else: 
#         fm=AuthenticationForm()
#     return render(request,'login.html',{'form':fm})
 
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
def Product(request,myid):
    product=Products.objects.filter(product_id=myid)
    print(product)
    # as product is the list ...product will not give you anything.....use product[0]
    return render(request,'Product.html',{'myproduct':product[0]})
def contact(request):
    if(request.method == 'POST'):
        print(request)
        name=request.POST.get('name','default_values')
        email=request.POST.get('email','default_values')
        phoneno=request.POST.get('phoneno','default_values')
        desc=request.POST.get('desc','default_values')
        print(name,email,phoneno,desc)
        # saving the contact 
        my_contact=Contact(name=name,email=email,phoneno=phoneno,desc=desc)
        my_contact.save()
    return render(request,'contact.html')

def multistepformexample_save(request):
    if request.method!='POST' :
        return render(request,'login_merchant.html')
        # return HttpResponseRedirect(reverse("login_merchant"))
    else:
        mdname = (request.POST.get('dname'))
        mdsurname = (request.POST.get('dsurname'))
        mdphoneno = (request.POST.get('dphoneno'))
        mdemail = (request.POST.get('demail'))
        mdesc = (request.POST.get('desc'))
        mdcountry = (request.POST.get('dcountry'))
        mdcity = (request.POST.get('dcity'))
        mdpincode = (request.POST.get('dpincode'))
        mdschool = (request.POST.get('dschool'))
        mdcollege = (request.POST.get('dcollege'))
        mddegree = (request.POST.get('ddegree'))
        mdmonth = (request.POST.get('dmonth'))
        mdposition = (request.POST.get('dposition'))
        mdcompany = (request.POST.get('dcompany'))
        mdc1 = (request.POST.get('dc1'))
        mdcc1 = (request.POST.get('dcc1'))
        mdm1 = (request.POST.get('dm1'))
        mdm2 = (request.POST.get('dm2'))
        mdata = {
            'mdname': mdname,
            'mdsurname': mdsurname,
            'mdphoneno': mdphoneno,
            'mdemail': mdemail,
            'mdcountry': mdcountry,
            'mdcity': mdcity,
            'mdesc': mdesc,
            'mdpincode': mdpincode,
            'mdcompany': mdcompany,
            'mdschool': mdschool,
            'mdcollege': mdcollege,
            'mddegree': mddegree,
            'mdmonth': mdmonth,
            'mdposition': mdposition,
            'mdc1': mdc1,
            'mdcc1': mdcc1,
            'mdm1': mdm1,
            'mdm2': mdm2,
        }
        return render(request,'login_merchant.html')
        # return HttpResponseRedirect(reverse('login_merchant'))

def tracker(request):
    return render(request,'tracker.html')
def search(request):
    return render(request,'search.html')
def checkout_page(request):
    return render(request,'checkout_page.html')
def register(request):
    return render(request,'register.html')
def login_merchant(request):
    mdata={}
    if request.method=='POST' :
        mname = request.POST.get('name')
        msurname = request.POST.get('surname')
        mphoneno = request.POST.get('phoneno')
        memail = request.POST.get('email')
        mdesc = request.POST.get('desc')
        mcountry = request.POST.get('country')
        mcity = request.POST.get('city')
        mbillingadd = request.POST.get('billingadd')
        mshippingadd = request.POST.get('shippingadd')
        mpincode = request.POST.get('pincode')

        mdata = {
                'mname': mname,
                'msurname': msurname,
                'mphoneno': mphoneno,
                'memail': memail,
                'mcountry': mcountry,
                'mcity': mcity,
                'mdesc': mdesc,
                'mpincode': mpincode,
                'mshippingadd': mshippingadd,
                'mbillingadd': mbillingadd,
        }
        myobj=Merchant(name=mname,surname=msurname,phoneno=mphoneno,email=memail,desc=mdesc,country=mcountry,city=mcity,pincode=mpincode,shippingadd=mshippingadd,billingadd=mbillingadd)
        myobj.save()
    return render(request,'login_merchant.html',{'formdata':mdata})
def login_customer(request):
    return render(request,'login_customer.html')
def Become_Seller(request):
    return render(request,'Become_Seller.html')
def reviews(request):
    return render(request,'reviews.html')
def trys(request):
    return render(request,'try.html')
def aboutus(request):
    return render(request,'aboutus.html')
def product_form(request):
    mdata={}
    if request.method=='POST' :
        mname = request.POST.get('name')
        mcat = request.POST.get('cat')
        msubcat = request.POST.get('subcat')
        mprice = request.POST.get('price')
        mdesc = request.POST.get('desc')
        mdate = request.POST.get('date')
        mimage = request.FILES.get('image')

        mdata = {
                'mname': mname,
                'mcat': mcat,
                'msubcat': msubcat,
                'mprice': mprice,
                'mdate': mdate,
                'mimage': mimage,
                'mdesc': mdesc,
        }
        myobj=Products(product_name=mname,category=mcat,subcategory=msubcat,price=mprice,product_desc=mdesc,product_pub_date=mdate,image=mimage)
        myobj.save()
    return render(request,'product_form.html',{'formdata':mdata})
def thanks(request):
    return render(request,'thanks.html')
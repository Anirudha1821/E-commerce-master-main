from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="HomePage"),
    path("home/", views.home,name="HomePage"),
    path("Product/<slug:myid>", views.Product,name="HomePage"),
    path("contact/", views.contact,name="HomePage"),
    path("tracker/", views.tracker,name="HomePage"),
    path("search/", views.search,name="HomePage"),
    path("reviews/", views.reviews,name="HomePage"),
    path("checkout_page/", views.checkout_page,name="HomePage"),
    path("login_merchant/", views.login_merchant,name="HomePage"),
    path("login_customer/", views.login_customer,name="HomePage"),
    path("login/", views.login,name="HomePage"),
    path("Become_Seller/", views.Become_Seller,name="HomePage"),
    path("trys/", views.trys,name="HomePage"),
    path("multistepformexample_save/", views.multistepformexample_save,name="HomePage"),
    path("register/", views.register,name="HomePage"),
]

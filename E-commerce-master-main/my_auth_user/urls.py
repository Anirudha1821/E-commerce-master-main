from django.urls import path
from . import views
urlpatterns = [
    path("sign_up/", views.sign_up,name="sign_up"),
    path("sign_in/", views.sign_in,name="sign_in"),
    path("sign_out/", views.sign_out,name="sign_out"),
    path("profile/", views.profile,name="profile"),
    path("change_pass/", views.change_pass,name="change_pass"),
    path("userdetail/<int:id>", views.userdetail,name="userdetail"),
]
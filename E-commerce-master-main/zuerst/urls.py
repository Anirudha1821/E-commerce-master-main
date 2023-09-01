from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("home/", include('myweb.urls')),
    path("", include('myweb.urls')),
    path("auth/", include('my_auth_user.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

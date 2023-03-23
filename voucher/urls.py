from voucher.views import voucher, infor
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from voucher.views import voucher, infor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', voucher, name='voucher'),
    path('voucher/', infor, name='infor'),

]
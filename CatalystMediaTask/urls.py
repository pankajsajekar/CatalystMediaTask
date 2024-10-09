from django.contrib import admin
from django.urls import include, path

from company import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # logout
    path('accounts/logout/', views.account_logout, name='account_logout'),
    ##tets
    # django-allauth
    path('accounts/', include('allauth.urls') ),
    
    path('', include('company.urls')),
]

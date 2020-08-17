from django.urls import path
from . import views


urlpatterns = [
    #url:dashboard
    path('',views.dashboard,name='dashboard'),
    #dashboard/models
    path('<str:brand_name>/',views.brandmodels,name='brandmodels'),
    path('<str:brand_names>/enter-details/<str:model_name>',views.phoneinfo,name='phoneinfo'),







]
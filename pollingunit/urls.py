from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pollingunits/', views.polling_unit, name='polling_unit'),
    path('localgoverments/', views.local_government, name="local_government"),
]
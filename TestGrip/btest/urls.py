from django.urls import path
from .views import CreateStep, CreateTest, ListTest
from . import views
app_name = 'btest'
urlpatterns = [
    path('test/',CreateTest.as_view(),name='test' ),
    path('step/',CreateStep.as_view(),name='step' ),
    path('',views.homepage, name = 'home'),
    path('testlist/',ListTest.as_view(), name ='testlist')
   
]

from django.urls import path 
from blog import views 

urlpatterns = [
	path('',views.index,name='blog-index'),
	path('<id>/',views.detail,name='blog-detail'),
	]
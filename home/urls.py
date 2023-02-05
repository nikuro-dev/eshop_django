from django.urls import path
from home.views import index_page

#urls here

urlpatterns = [
    path('', index_page, name='home-page')
]

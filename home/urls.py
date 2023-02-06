from django.urls import path
from home.views import index_page, contact_page

#urls here

urlpatterns = [
    path('', index_page, name='home-page'),
    path('contact-us', contact_page, name='contact-us')
]

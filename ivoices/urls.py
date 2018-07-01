from django.conf.urls import url
from ivoices import views

urlpatterns = [
    url(r'^invoices/', views.invoice_list),
]

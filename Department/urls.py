from django.urls import path
from Department import views
urlpatterns = [
    path('', views.home_view),
    path('Branch/', views.add_branch, name="branch"),
    path('payment/', views.add_payment, name="payment"),
    path('demandType/', views.add_demandtype, name='Demand'),
    path('Customer/', views.add_customer, name='Customer'),
    path('demandRate/', views.add_demandrate, name='demandRate'),
    path('bill/', views.add_bill, name='bill'),
    path('search/', views.search, name='search'),
    path('usearch/', views.usearch, name='usearch'),
   # path('udetail/', views.usearch, name='usearch'),
    path('paymentDetails/', views.add_paymentDetails, name="paymentDetails")
]
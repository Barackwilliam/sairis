
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-product-1/', views.admin_products_view_1,name='admin-products-1'),
    path('admin-product-2/', views.admin_products_view_2,name='admin-products-2'),
    path('admin-product-3/', views.admin_products_view_3,name='admin-products-3'),
    path('admin-product-4/', views.admin_products_view_4,name='admin-products-4'),
    path('admin-product-5/', views.admin_products_view_5,name='admin-products-5'),



    path('admin-add-product/', views.admin_add_product_view,name='admin-add-product'),
    path('admin-add-product-1', views.admin_add_product_view_1, name='admin-add-product-1'),
    path('admin-add-product-2', views.admin_add_product_view_2,name='admin-add-product-2'),
    path('admin-add-product-3', views.admin_add_product_view_3,name='admin-add-product-3'),
    path('admin-add-product-4', views.admin_add_product_view_4,name='admin-add-product-4'),
    path('admin-add-product-5', views.admin_add_product_view_5,name='admin-add-product-5'),


    path('way', views.way,name='way'), 
    path('hosting', views.hosting,name='hosting'),


    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('delete-product-1/<int:pk>', views.delete_product_view_1,name='delete-product-1'), 
    path('delete-product-2/<int:pk>', views.delete_product_view_2,name='delete-product-2'),
    path('delete-product-3/<int:pk>', views.delete_product_view_3,name='delete-product-3'),
    path('delete-product-4/<int:pk>', views.delete_product_view_4,name='delete-product-4'),
    path('delete-product-5/<int:pk>', views.delete_product_view_5,name='delete-product-5'),





    path('update-product/<int:pk>', views.update_product_view,name='update-product'),
    path('update-product-1/<int:pk>', views.update_product_view_1,name='update-product-1'),
    path('update-product-2/<int:pk>', views.update_product_view_2,name='update-product-2'),
    path('update-product-3/<int:pk>', views.update_product_view_3,name='update-product-3'),
    path('update-product-4/<int:pk>', views.update_product_view_4,name='update-product-4'),
    path('update-product-5/<int:pk>', views.update_product_view_5,name='update-product-5'),




    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='ecom/web_home.html'),name='customerlogin'),



    path('customer-home', views.customer_home_view,name='customer-home'),
    path('customer-home-1', views.customer_home_view_1,name='customer-home-1'),
    path('customer-home-2', views.customer_home_view_2,name='customer-home-2'),
    path('customer-home-3', views.customer_home_view_3,name='customer-home-3'),
    path('customer-home-4', views.customer_home_view_4,name='customer-home-4'),
    path('customer-home-5', views.customer_home_view_5,name='customer-home-5'),



    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),
    path('pay', views.pay,name='pay'),
   
   


]

from django.urls import path
from . import views

urlpatterns = [
    # Auth (simple templates + basic handlers)
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Travel pages
    path('', views.travel_options, name='travel_options'),
    path('booking/<int:pk>/', views.booking_form, name='booking_form'),
    path('confirmation/<int:booking_id>/', views.confirmation, name='confirmation'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('book/<int:option_id>/', views.book_travel, name='book_travel'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]

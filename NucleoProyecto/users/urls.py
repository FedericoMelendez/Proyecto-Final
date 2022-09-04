from django.urls import path
from users.views import login_request, register, show_profile,create_profile,edit_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/', show_profile, name='profile'),
    path ('create-profile/',create_profile,name='create_profile'),
    path ('edit-profile/<int:pk>/',edit_profile,name='edit_profile'),
]
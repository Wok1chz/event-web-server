from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('schedule/', EventHome.as_view(), name='schedule'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>', ShowPost.as_view(), name='post'),
    path('profile/', ShowProfile.as_view(), name='profile'),
    path('add/', event_sign, name='add'),
    path('del/', event_delete, name='del'),
    path('pdf/', get_pdf, name='pdf')
]
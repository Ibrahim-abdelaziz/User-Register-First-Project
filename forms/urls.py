from django.urls import path
from .views import index, register,registerr,register_user,log,log_user,profile,logout_user,log_info,loginfo_backend,edit_register,notes,one_note,delete_register,show_user


urlpatterns = [
    path('', index, name='index'),
    path('home',notes,name='notes'),
    path('one_note/<int:id>/',one_note,name='one_note'),
    path('register',register,name='register'),
    path('edit/<int:id>/',edit_register, name='edit'),
    path('delete/<int:id>/',delete_register, name='delete'),
    path('registerr',registerr,name='registerr'),
    path('register_user',register_user,name='register_user'),
    path('log',log,name='log'),
    path('log_user',log_user,name='log_user'),
    path('profile/<str:username>/',profile, name='profile'),
    path('logout_user',logout_user, name='logout_user'),
    path('log_info/<str:username>/',log_info, name='log_info'),
    path('loginfo_backend/<str:username>/',loginfo_backend, name='loginfo_backend'),
    path('show_user/<str:username>/', show_user, name='show_user'),

]

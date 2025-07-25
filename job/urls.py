from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.home,name='home'),
   path('login',views.signin,name='login'),
   path('register',views.register,name='register'),
   path('dashboard',views.dashboard,name='dashboard'),
   path('people_post',views.people_post,name='people_post'),
   path('company_post',views.company_post,name='company_post'),
   path('profile',views.profile,name='profile'),
   path('apply_job/<int:post_id>',views.apply_job,name='apply_job'),
   path('view_applicante/<int:post_id>',views.view_applicante,name='view_applicante'),
   #path('post',views.post,name='post'),
   path('view_profile/<int:user_id>',views.view_profile,name='view_profile'),
   path('people_photo',views.people_photo,name="people_photo"),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

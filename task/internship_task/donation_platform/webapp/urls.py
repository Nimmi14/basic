from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Donar_home,name='home'),
    path('uform/',views.Donar_signup, name='uform'),
    # path('dform/',views.doctor_signup,name='dform'),
    path('ulogin/',views.Donar_login,name='ulogin'),
    # path('dlogin/',views.doctor_login,name='dlogin'),
    path('ddash/',views.Donar_dashboard,name='ddash'),
    # path('ddash/',views.doctor_dashboard,name='ddash'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


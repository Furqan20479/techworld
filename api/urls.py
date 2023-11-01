
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appoint'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('testi/', views.testimonial, name='testi'),
    path('four_0_four/', views.four_0_four, name='four'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



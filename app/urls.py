from django.urls import path, re_path
from .views import home_view, news_view, news_detail_view, ourClients_view, about_view, login_view, signup_view, try_login
from .views import NewsCreateView, NewsUpdateView, NewsDeleteView
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import serve
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='app/home.html'), name='logout'),

    path('try_login/', try_login, name="try_login"),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('signup/', signup_view, name='signup'),

    path('home/', home_view, name="home"),
    path('clients/', ourClients_view, name="clients"),
    path('about/', about_view, name='about'),
    path('news/', news_view, name='news'),
    path('news_detail/<int:pk>/', news_detail_view, name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    re_path(r'^(?!static/|media/|news_images).*$', RedirectView.as_view(url='/home/'))

]
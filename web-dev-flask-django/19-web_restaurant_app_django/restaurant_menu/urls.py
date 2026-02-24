from django.urls import path
from . import views
from .views import AboutView

urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    path("item/<int:pk>/", views.MenuItemDetail.as_view(), name="menu_item"),
    path('about/', AboutView.as_view(), name='about')
]
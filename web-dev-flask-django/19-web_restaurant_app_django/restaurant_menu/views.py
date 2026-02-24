from django.shortcuts import render
from django.views import generic
from .models import Item

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["starters"] = Item.objects.filter(meal_type="starters", status=1).order_by("-date_created")
        context["salads"] = Item.objects.filter(meal_type="salads", status=1).order_by("-date_created")
        context["main_dishes"] = Item.objects.filter(meal_type="main_dishes", status=1).order_by("-date_created")
        context["desserts"] = Item.objects.filter(meal_type="desserts", status=1).order_by("-date_created")
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"

from django.shortcuts import render
from .models import Homepage, Category


def index(request):
    homepage = Homepage.objects.all()
    category = Category.objects.all()
    context = {
        "homepage": homepage,
        "title": "List pages",
        "category": category}
    return render(request, template_name="homepage/index.html", context=context)


def get_category(request, category_id):
    homepage = Homepage.objects.filter(category_id=category_id)
    category = Category.objects.all()
    categories = Category.objects.get(pk=category_id)
    context = {
        "homepage": homepage,
        "categories": categories,
        "category": category
    }
    return render(request, "homepage/category.html", context=context)

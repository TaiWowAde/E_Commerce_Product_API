from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product
from categories.models import Category

@login_required
def dashboard_home(request):
    q = request.GET.get("q", "").strip()
    products_qs = Product.objects.select_related("category", "created_by").order_by("-created_date")
    if q:
        products_qs = products_qs.filter(name__icontains=q)

    paginator = Paginator(products_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "q": q,
        "page_obj": page_obj,
        "total_products": products_qs.count(),
        "total_categories": Category.objects.count(),
    }
    return render(request, "dashboard/index.html", context)

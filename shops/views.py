from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Shop, Rent

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shop_list.html', {'shops': shops})

def rent_status(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    rent_records = Rent.objects.filter(shop=shop).order_by('year', 'month')
    return render(request, 'shops/rent_status.html', {'shop': shop, 'rent_records': rent_records})

def export_rent_pdf(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="rent_{shop.name}.pdf"'
    response.write(f"PDF export of rent records for shop: {shop.name} (ID: {shop.id})")
    return response

def export_rent_excel(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="rent_{shop.name}.xlsx"'
    # For now, a simple placeholder text, later replace with real Excel generation
    response.write(f"Excel export of rent records for shop: {shop.name} (ID: {shop.id})")
    return response

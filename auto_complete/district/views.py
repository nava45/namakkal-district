from django.shortcuts import render
from django.http import Http404

from district.models import Item, Location, Category

def home(request):
    return render(request, "district/home.html", locals())

def get_items(request):
    if request.is_ajax():
        print "ajax"

def view_item_detail(request, location, category, item):
    if item is None:
        raise Http404()
    else:
        print item, category, location
        try:
            status = True
            location = Location.objects.filter(place__iexact=location)[0]
            category = Category.objects.filter(name__iexact=category)[0]
            item = Item.objects.filter(location=location, category=category, name__icontains=item)
            return render(request, "district/item_detail.html", locals())
        except IndexError:
            return render(request, "district/item_detail.html", {'status': False })
            

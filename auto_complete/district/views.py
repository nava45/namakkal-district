from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify

from district.models import Item, Location, Category

import json

def home(request):
    return render(request, "district/home.html", locals())

def get_items(request):
    if request.is_ajax():
        print "ajax",request.POST
        items = Item.objects.filter(slug_name__icontains=request.POST.get('search'))
        items = [(str(i.name), slugify(i.location.place)+'/'+slugify(i.category.name)+'/'+slugify(i.name)+'/') for i in items]
        return HttpResponse(json.dumps({'items': items}))
    else:
        return HttpResponse('We love ajax :( not you')

def view_item_detail(request, location, category, item):
    if item is None:
        raise Http404()
    else:
        print item, category, location
        try:
            status = True
            location = Location.objects.filter(place__iexact=location)[0]
            category = Category.objects.filter(name__iexact=category)[0]
            item = Item.objects.filter(location=location, category=category, slug_name__icontains=item)
            return render(request, "district/item_detail.html", locals())
        except IndexError:
            return render(request, "district/item_detail.html", {'status': False })
            

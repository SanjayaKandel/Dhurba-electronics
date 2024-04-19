from django.shortcuts import render,redirect
from . models import Items, Accessories
from . forms import ItemRegister, AccessoriesRegistration, UpdateAccessories, UpdateItems
# Create your views here.

#User page
def index(request):
    item = Items.objects.all()
    accessories = Accessories.objects.all()
    det={
        'items':item,
        'accessories':accessories
    }
    return render(request,"Home/index.html", det)

#Admin page
def admin_index(request):
    accessories = Accessories.objects.all()
    item = Items.objects.all()
    
    det={
        'items':item,
        'accessories':accessories
    }
    return render(request,'Home/admin.html', det)
#adding Items
def add_item(request):
    form = ItemRegister()
    if request.method =='POST':
        form = ItemRegister(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    return render(request,'Home/add_item.html',{'form':form})

#Updating Items
def update_items(request,id):
    item = Items.objects.get(pk=id)
    form = UpdateItems(instance=item)
    if request.method=='POST':
        accessories = UpdateItems(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    return render(request,'Home/update_items.html',{'form':form})

#Deleting items
def delete_items(request, id):
    items = Items.objects.get(pk=id)
    items.delete()
    return redirect('admin_index')

#adding accessories items
def add_accessories(request):
    form = AccessoriesRegistration()
    if request.method =='POST':
        form = AccessoriesRegistration(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    return render(request, 'Home/add_accessories.html',{'form':form})

#Updating accessories
def update_accessories(request,id):
    accessories = Accessories.objects.get(pk=id)
    form = UpdateAccessories(instance=accessories)
    if request.method=='POST':
        accessories = UpdateAccessories(request.POST,request.FILES, instance=accessories)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    return render(request,'Home/update_accessories.html',{'form':form})
#Delete accessories
def delete_accessories(request, id):
    accessories = Accessories.objects.get(pk=id)
    accessories.delete()
    return redirect('admin_index')

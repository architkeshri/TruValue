from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PhoneBrands,PhoneModels
from .forms import PhoneInfo
from django.http import HttpResponse
import  datetime
from django.contrib import messages


@login_required
def dashboard(request):
    phone_brands = PhoneBrands.objects.all()
    context = {'phone_brands':phone_brands,
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required
def brandmodels(request,brand_name):
    brand= PhoneBrands.objects.get(BrandName=brand_name)

    context = {'brand':brand,}
    return render(request,'dashboard/brandmodels.html',context)

@login_required
def phoneinfo(request,brand_names,model_name):


    phone_info = PhoneModels.objects.get(model_name=model_name)
    if request.method == 'POST':
        form = PhoneInfo(request.POST,instance=phone_info)
        context = {
            'form': form,
        }
        if form.is_valid():
            evaluated_price = float(phone_info.model_price)
            if form.cleaned_data['charger']=='No':
                evaluated_price = evaluated_price - .15*evaluated_price
            if form.cleaned_data['warranty_period'] == 'No':
                evaluated_price = evaluated_price - .20*evaluated_price
            if form.cleaned_data['refurbished'] == 'Yes':
                evaluated_price = evaluated_price - .25*evaluated_price

            date = form.cleaned_data['purchase_date']







        return HttpResponse("<h1 align='center'> Evaluated Price: Rs"+str(evaluated_price) + "</h1>")

    else:
        form = PhoneInfo(instance=phone_info)
        context = {


            'form': form,
        }

    return render(request, 'dashboard/phoneinfo.html', context)




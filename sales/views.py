from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from marketing_app.models import *

# Create your views here.

def product_sales(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')
    
    product = get_object_or_404(Product, id=product_id)
    sales = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.product = product
            info.status = True
            info.save()
            return redirect('index')
        else:
            print(form.errors)  

    context = {
        'sale': sales,
        'product': product
    }
    return render(request, 'buybook.html', context)



def course_sales(request, course_id):
    if not request.user.is_authenticated:
        return redirect('index')
    
    course = get_object_or_404(Course, id=course_id)
    sales = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.course = course
            info.status = True
            info.save()
            return redirect('index')
        else:
            print(form.errors)  

    context = {
        'sale': sales,
        'course': course
    }
    return render(request, 'buycourse.html', context)



def consultation_sales(request, consultation_id):
    if not request.user.is_authenticated:
        return redirect('index')
    
    consultation = get_object_or_404(Consultation, id=consultation_id)
    sales = ConsultationForm()

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.consultation = consultation
            info.status = True
            info.save()
            return redirect('index')
        else:
            print(form.errors)  

    context = {
        'sale': sales,
        'consultation': consultation
    }
    return render(request, 'buyconsultation.html', context)

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from datetime import date
from django.contrib.auth import login, logout, authenticate
from sales.models import *

# Create your views here.
def index(request):
    signup_form = SignupForm()
    login_form = LoginForm()
    error = None

    all_products = Product.objects.all()
    purchased_products_ids = []

    if request.user.is_authenticated:
        purchased_products_ids = ProductSale.objects.filter(
            user=request.user,
            status=True
        ).values_list('product_id', flat=True)

    all_courses = Course.objects.all()
    purchased_courses_ids = []
    if request.user.is_authenticated:
        purchased_courses_ids = CourseSale.objects.filter(
            user= request.user,
            status=True
        ).values_list('course_id', flat = True)


    all_consultations = Consultation.objects.all()
    purchased_consultations_ids = []
    if request.user.is_authenticated:
        purchased_consultations_ids = ConsultationSale.objects.filter(
            user= request.user,
            status=True
        ).values_list('consultation_id', flat = True)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                has_info = Information.objects.filter(user=user).exists()
                if not has_info:
                    return redirect('informations')
                else:
                    return redirect('index')
            else:
                error = 'Invalid Username or Password!'
                return redirect('index', error=error)

    today = date.today()
    info = Information.objects.first()
    age = None
    if info and info.birthday:
        age = today.year - info.birthday.year - (
            (today.month, today.day) < (info.birthday.month, info.birthday.day)
        )

    social_icons = SocialIcon.objects.all()
    socials = {icon.name.lower(): icon.link for icon in social_icons}

    context = {
        'info': info,
        'email': User.objects.first(),
        'count': User.objects.count(),
        'age': age,
        'social': socials,
        'links': Links.objects.all(),
        'products': all_products,
        'pur_pro_ids': purchased_products_ids,
        'courses': all_courses,
        'pur_cor_ids': purchased_courses_ids,
        'consultations': all_consultations,
        'pur_cons_ids': purchased_consultations_ids,
        'signup': signup_form,
        'login': login_form,
        'error': error,
    }
    return render(request, 'index.html', context)

def signin(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            has_info = Information.objects.filter(user=user).exists()
            if not has_info:
                return redirect('informations')
            else:
                return redirect('index')

def signout(request):
    logout(request)
    return redirect('index')

def informations(request):
    if request.user.is_authenticated:
        try:
            info = Information.objects.get(user=request.user)
        except Information.DoesNotExist:
            info = None

        information_form = InformationForm()

        if request.method == 'POST':
            form = InformationForm(request.POST, request.FILES)
            if form.is_valid():
                info = form.save(commit=False)
                info.user = request.user 
                info.save()
                return redirect('index')

        context = {
            'email': User.objects.first(),
            'info': Information.objects.first(),
            'form': information_form
        }

        return render(request, 'informations.html', context)
    else:
        return redirect('index')  

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models import Count
from datetime import timedelta
from sales.models import *
from django.db.models.functions import TruncMonth
import json


# Create your views here.
def stats_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        total_users = User.objects.count()
        total_product_sales = ProductSale.objects.count()
        total_courses_sales = CourseSale.objects.count()
        total_consultations_sales = ConsultationSale.objects.count()
        today = now().date()
        this_month = now().month

        new_users_today = User.objects.filter(date_joined__date=today).count()
        new_users_this_month = User.objects.filter(date_joined__month=this_month).count()

        new_products_today = ProductSale.objects.filter(created_at__date=today).count()
        new_products_month = ProductSale.objects.filter(created_at__month=this_month).count()

        new_courses_today = CourseSale.objects.filter(created_at__date=today).count()
        new_courses_month = CourseSale.objects.filter(created_at__month=this_month).count()

        new_consultations_today = ConsultationSale.objects.filter(created_at__date=today).count()
        new_consultations_month = ConsultationSale.objects.filter(created_at__month=this_month).count()

        def get_monthly_data(model, date_field):
            qs = (
                model.objects.annotate(month=TruncMonth(date_field))
                .values('month')
                .annotate(count=Count('id'))
                .order_by('month')
            )
            labels = [entry['month'].strftime("%B") for entry in qs]
            data = [entry['count'] for entry in qs]
            return labels, data

        user_labels, user_data = get_monthly_data(User, 'date_joined')
        product_labels, product_data = get_monthly_data(ProductSale, 'created_at')
        course_labels, course_data = get_monthly_data(CourseSale, 'created_at')
        consult_labels, consult_data = get_monthly_data(ConsultationSale, 'created_at')

        context = {
            'email': User.objects.first(),
            'info': Information.objects.first(),
            'total_users': total_users,
            'new_users_today': new_users_today,
            'new_users_this_month': new_users_this_month,

            'total_product_sales': total_product_sales,
            'new_products_today': new_products_today,
            'new_products_month': new_products_month,

            'total_courses_sales': total_courses_sales,
            'new_courses_today': new_courses_today,
            'new_courses_month': new_courses_month,

            'total_consultations_sales': total_consultations_sales,
            'new_consultations_today': new_consultations_today,
            'new_consultations_month': new_consultations_month,

            'user_labels': json.dumps(user_labels),
            'user_data': json.dumps(user_data),

            'product_labels': json.dumps(product_labels),
            'product_data': json.dumps(product_data),

            'course_labels': json.dumps(course_labels),
            'course_data': json.dumps(course_data),

            'consult_labels': json.dumps(consult_labels),
            'consult_data': json.dumps(consult_data),
        }

        return render(request, 'stats.html', context)
    else:
        return redirect('index')
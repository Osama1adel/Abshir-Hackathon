from django.shortcuts import render
from .models import Cluster

def home(request):
    # جلب جميع المشاكل مرتبة بالأكثر تكراراً
    clusters = Cluster.objects.all().order_by('-count')
    context = {
        'clusters': clusters,
        'total_count': sum(c.count for c in clusters), # حساب إجمالي الاستفسارات
    }
    return render(request, 'dashboard/index.html', context)

def generator(request):
    return render(request, 'dashboard/generator.html')
from django.shortcuts import render, get_object_or_404
from .models import Image
from datetime import datetime, timedelta

def gallery_view(request):
    one_month_ago = datetime.now() - timedelta(days=30)
    images = Image.objects.filter(created_date__gte=one_month_ago)
    return render(request, 'gallery.html', {'images': images})
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import MealWeek

# Create your views here.
def mealweek_list(request):
    mealweeks = MealWeek.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mealplanner/mealweek_list.html', {'mealweeks': mealweeks})

def mealweek_detail(request, pk):
    mealweek = get_object_or_404(MealWeek, pk=pk)
    return render(request, 'mealplanner/mealweek_detail.html', {'mealweek': mealweek})
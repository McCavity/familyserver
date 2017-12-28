from django.shortcuts import render
from django.utils import timezone
from .models import MealWeek

# Create your views here.
def mealweek_list(request):
    mealweeks = MealWeek.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mealplanner/mealweek_list.html', {'mealweeks': mealweeks})
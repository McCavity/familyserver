from django.shortcuts import render

# Create your views here.
def mealweek_list(request):
    return render(request, 'mealplanner/mealweek_list.html')
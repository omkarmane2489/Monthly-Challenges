from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
#from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes for a day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes for a day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes for a day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes for a day",
    "december": None
}
# Create your views here.

def index(request):
    
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        context ={
            "text": challenge_text,
            "month": month
        }
        return render(request,"challenges/challenge.html", context=context)
        
        
    
    except:
        raise Http404()
    
    

def monthly_challenge_by_number(request, month):
    month_list = list(monthly_challenges.keys())

    if month > len(month_list):
        return HttpResponseNotFound("Invalid Month!")
    
    input_month = month_list[month-1]
    print(input_month)
    redirect_path = reverse("month", args=[input_month])
    
    return HttpResponseRedirect(redirect_path)
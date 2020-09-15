from django.shortcuts import render

def skill(request):
    context = {'skill': 'active'}
    return render(request, 'education/skill.html', context)
from django.shortcuts import render
from .models import Districts,Divisions

# Create your views here.
from django.http import JsonResponse



def district_list(request):
    
    districts =  Districts.objects.all()
    
    contexts = {'districts':districts}
    return render(request,'information/districts.html',contexts)


def filter(request):
    msg = request.POST.get('msg')

    
    districts =  Districts.objects.all().values()
    if msg == 'all':
        districts =  Districts.objects.all().values()
    elif msg == 'visited':
        districts =  Districts.objects.filter(visited=True).values()
    elif msg == 'population50+':
        districts =  Districts.objects.filter(population_density__gt = 50).values()
    elif msg == 'education50+':
        districts =  Districts.objects.filter(education_rate__gt = 50).values()
    elif msg == 'dhaka':
        districts =  Districts.objects.filter(Divisions__name = 'Dhaka').values()
    # print(districts)




    name,education,population,visited,division = [],[],[],[],[]
    
    for i in districts:
        name.append(i['name'])
        education.append(i['education_rate'])
        population.append(i['population_density'])
        if i['visited']:
            visited.append('Yes')
        else:
            visited.append('No')

        # getting division foreign key name
        division.append(Divisions.objects.filter(id=i['Divisions_id']).values()[0]['name'])
    


    data = {
        'name':name,
        'education':education,
        'population':population,
        'visited':visited,
        'division':division,
    }
    print(data)
    
    
    # return districts`
    
    return JsonResponse({'data':data})
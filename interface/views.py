import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import json


def survivors(request):
    response = requests.get('http://127.0.0.1:8000/api/survivors/')
    survivors = response.json()
    context = {'survivors': survivors}
    return render(request, 'interface/survivors.html', context)

def survivor_detail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/survivors/{pk}/')
    survivor = response.json()

    response = requests.get('http://127.0.0.1:8000/api/survivors/')
    survivors = response.json()
    
    context = {'survivor': survivor, 'survivors': survivors}
    return render(request, 'interface/survivor_detail.html', context)

def resources_report(request):
    response = requests.get('http://127.0.0.1:8000/api/survivors/get_resources_report/')
    context = {'report': response.json()}
    print(response)
    return render(request, 'interface/resources_report.html', context)

def report_infected(request, pk):
    data = {
            'survivor_reported': request.POST.get('survivor_reported'),
            'latitude': float(request.POST.get('latitude')),
            'longitude': float(request.POST.get('longitude')),
            }
    print(data)
    response = requests.put(f'http://127.0.0.1:8000/api/survivors/{pk}/report_infected/', json=data)
    return redirect(reverse('interface:survivor_detail', kwargs={'pk': pk}))

def update_location(request, pk):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        data = {'latitude': latitude, 'longitude': longitude}
        print(data)
        requests.patch(f'http://127.0.0.1:8000/api/survivors/{pk}/', data=data)
        return redirect(reverse('interface:survivor_detail', kwargs={'pk': pk}))
    response = requests.get(f'http://127.0.0.1:8000/api/survivors/{pk}/')
    survivor = response.json()
    return render(request, 'interface/update_location.html', {'survivor': survivor})

def add_survivor(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'sex': request.POST.get('sex'),
            'latitude': request.POST.get('latitude'),
            'longitude': request.POST.get('longitude'),
            'infected': request.POST.get('infected', False),
            "points": 0,
            "reports": 0,
            'water': request.POST.get('water'),
            'food': request.POST.get('food'),
            'medication': request.POST.get('medication'),
            'ammunition': request.POST.get('ammunition'),
        }
        requests.post('http://127.0.0.1:8000/api/survivors/', data=data)
        return redirect(reverse('interface:survivors'))
    return render(request, 'interface/add_survivor.html')

def delete_survivor(request, pk):
    response = requests.delete(f'http://127.0.0.1:8000/api/survivors/{pk}/')
    return redirect(reverse('interface:survivors'))

def make_trade(request, pk):
    if request.method == 'POST':
        data = {
            "survivor1": pk,
            "survivor2": request.POST['survivor2'],
            "survivor1_items": request.POST.getlist('survivor1_items'),
            "survivor2_items": request.POST.getlist('survivor2_items')
        }
        print(data)
        requests.put(f"http://127.0.0.1:8000/api/survivors/{pk}/make_trade/", data=data)
        return redirect(reverse('interface:survivor_detail', kwargs={'pk': pk}))

    response = requests.get(f'http://127.0.0.1:8000/api/survivors/{pk}/')
    survivor1 = response.json()

    response = requests.get(f'http://127.0.0.1:8000/api/survivors/{request.GET["survivor2"]}/')
    survivor2 = response.json()
    
    context = {'survivor1': survivor1, 'survivor2': survivor2}
    return render(request, 'interface/make_trade.html', context)
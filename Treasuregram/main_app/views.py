from django.shortcuts import render
from django.http import HttpResponse

class Treasure: 
    def __init__(self, name, value, material, location, image_url):
        self.name = name
        self.value = value 
        self.material = material
        self.location = location
        self.image_url = image_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'http://example.com/gold'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'http://example.com/fool'),
    Treasure('Coffe can', 20.00, 'tin', 'Acme, CA', 'http://example.com/coffe')
]

def index(request):
    context = { 'treasures' : treasures }
    return render(request, 'index.html', context)





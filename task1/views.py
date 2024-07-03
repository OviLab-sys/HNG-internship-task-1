import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    
    # Get client's IP address
    client_ip = request.META.get('REMOTE_ADDR')
    
    # Get location and weather information (using example APIs, you can replace these with actual ones)
    location_api_url = f"http://ip-api.com/json/{client_ip}"
    weather_api_url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q="
    
    location_response = requests.get(location_api_url).json()
    city = location_response.get('city', 'Unknown')
    
    weather_response = requests.get(weather_api_url + city).json()
    temperature = weather_response['current']['temp_c']

    # Create response
    response_data = {
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }
    
    return Response(response_data)

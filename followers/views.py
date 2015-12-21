from django.shortcuts import render

# Create your views here.


import requests
from bs4 import BeautifulSoup


def get_followers(handle):
	try:
		url = "https://twitter.com/{}".format(handle)
		soup =BeautifulSoup(requests.get(url).text, 'html.parser')
		followers =  soup.find('li', {'class':'ProfileNav-item--following'}).find('span', {'class':'ProfileNav-value'}).text
		return followers
	except:
		return 'Error getting followers for the handle, please try again'





def home(request):
	if request.method == "POST":
		handle = request.POST.get('handle')
		followers = get_followers(handle)
		return render(request, 'followers/home.html', {'followers':followers, 'handle':handle})
	else:
		return render(request, 'followers/home.html') 

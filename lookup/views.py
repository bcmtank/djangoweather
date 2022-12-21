#add comment

from django.shortcuts import render



def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=1F52106E-44D5-404B-880D-E199039D8997")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color = "unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description ="(201 to 300) Health alert: The risk of health effects is increased for everyone."
			category_color = "veryunhealthy"
		elif aapi[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 to 500) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color = "hazardous"


		if api[1]['Category']['Name'] == "Good":
			category_description_1 = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color_1 = "good"
		elif api[1]['Category']['Name'] == "Moderate":
			category_description_1 = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color_1 = "moderate"
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color_1 = "unhealthyforsensitivegroups"
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_description_1 = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color_1 = "unhealthy"
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_description_1 = "(150.5 to 250.4) Health alert: The risk of health effects is increased for everyone."
			category_color_1 = "veryunhealthy"
		elif api[1]['Category']['Name'] == "Hazardous":
			category_description_1 = "(250.5+) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color_1 = "hazardous"
	  
		if api[2]['Category']['Name'] == "Good":
			category_description_2 = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color_2 = "good"
		elif api[2]['Category']['Name'] == "Moderate":
			category_description_2 = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color_2 = "moderate"
		elif api[2]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description_2 = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color_2 = "unhealthyforsensitivegroups"
		elif api[2]['Category']['Name'] == "Unhealthy":
			category_description_2 = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color_2 = "unhealthy"
		elif api[2]['Category']['Name'] == "Very Unhealthy":
			category_description_2 = "(201 to 300) Health alert: The risk of health effects is increased for everyone."
			category_color_2 = "veryunhealthy"
		elif api[2]['Category']['Name'] == "Hazardous":
			category_description_2 = "(301 to 500) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color_2 = "hazardous"
		
		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description, 
			'category_description_1': category_description_1, 
			'category_description_2': category_description_2, 
			'category_color': category_color, 
			'category_color_1': category_color_1, 
			'category_color_2': category_color_2
			})


	else:

		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=84119&distance=6&API_KEY=1F52106E-44D5-404B-880D-E199039D8997")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color = "unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description ="(201 to 300) Health alert: The risk of health effects is increased for everyone."
			category_color = "veryunhealthy"
		elif aapi[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 to 500) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color = "hazardous"


		if api[1]['Category']['Name'] == "Good":
			category_description_1 = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color_1 = "good"
		elif api[1]['Category']['Name'] == "Moderate":
			category_description_1 = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color_1 = "moderate"
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color_1 = "unhealthyforsensitivegroups"
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_description_1 = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color_1 = "unhealthy"
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_description_1 = "(150.5 to 250.4) Health alert: The risk of health effects is increased for everyone."
			category_color_1 = "veryunhealthy"
		elif api[1]['Category']['Name'] == "Hazardous":
			category_description_1 = "(250.5+) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color_1 = "hazardous"
	  
		if api[2]['Category']['Name'] == "Good":
			category_description_2 = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color_2 = "good"
		elif api[2]['Category']['Name'] == "Moderate":
			category_description_2 = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color_2 = "moderate"
		elif api[2]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description_2 = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color_2 = "unhealthyforsensitivegroups"
		elif api[2]['Category']['Name'] == "Unhealthy":
			category_description_2 = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color_2 = "unhealthy"
		elif api[2]['Category']['Name'] == "Very Unhealthy":
			category_description_2 = "(201 to 300) Health alert: The risk of health effects is increased for everyone."
			category_color_2 = "veryunhealthy"
		elif api[2]['Category']['Name'] == "Hazardous":
			category_description_2 = "(301 to 500) Health warning of emergency conditions: everyone is more likely to be affected."
			category_color_2 = "hazardous"
		
		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description, 
			'category_description_1': category_description_1, 
			'category_description_2': category_description_2, 
			'category_color': category_color, 
			'category_color_1': category_color_1, 
			'category_color_2': category_color_2
			})

def about(request):
	return render(request, 'about.html', {})

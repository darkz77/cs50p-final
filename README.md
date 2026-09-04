# Ask Temperature CLI

### Video Demo: <URL HERE>

### Author:
**Name**: Nguyen Minh Hoang
**Github**: darkz77
**edX**: ngmhoang202@gmail.com
**City * Country**: Da Nang - Vietnam
**Date of publish**: TBD

### Description - What is Ask Weather CLI?
**Ask Temperature CLI** is a simple tool for you to quickly check the temperature of your city. 
This tool uses Open Meteo's Geolocation API to fetch the latitude and longitude of your inputted city so you don't have to search them yourself. Just simply input your city name.
You can check your current apperent temperature right now or ask for a forecast for X days ahead or a min/max temperature for the next 7 days. I also use tabulate() to do all formatting for the table since it is easy to use and familiar to me through out CS50P course.

### Dependencies and git flow:
I wrote this project using some imports from tabulate, requests, pytest. Those imports are written and kept in the requirements.txt file. Before running project.py, run ```pip install -r requirements.txt```

### Technical approach:
All of the function of this tool stays inside 1 *project.py* file. Where main() is the navigator to different function and keep the program alive until user wants to shutdown. This approach makes this CLI similar to GUI tool.
Other functions are separated and small enough so that I can maintain them separately and easily in the future. Each function serve a small and testable chunk of work, including:
a. *fetch_forecast_api* - call and get the json response from Open Meta. I separate it into a new def so that I don't have to type it multiple times in other functions
b. *get_location* - this function call Open Meteo's Geolocation API to get the latitude and longitude from the city name user inputs.
c. *get_min_max* - this function get the min/max temperature from 2m height from Open Meteo. This is my favourite since I first practice zip() function and it allows me to understand deeper on this interesting function.
d. *get_forecast* - this function returns a table of temperature forecast for X amount of days from today. This function receives an int input from the user for X days. Due to the limitation from Open Meteo, X cannot be exceed 16 days
e. *get_current_temp* - This function just simply get the current temperature of your city
f. *generate_table* - A function to call tabulate and return a formatted table for other results.
All of these temperature returns in Celsius.

### Unit test approach
This project uses pytest to perform unit test. I tested 3 functions in *project.py* and all test cases are written in *test_project.py*
a. *test_get_location* - This script is used to test get_location function. This is rather simple to do the unit test since it will returns 2 floats for latitude and longitude. The pytest.approx() is used to compare the floats with assert approximately.
b. *test_get_min_max* - This script is used to test get_min_max() function. It is a bit more difficult compare to get_location since it requires to mock the JSON data returns from Open Meteo's API. I need to dig deeper into request function and how to mock API data in order to write unit test for this function.
c. *fetch_forecast_api* - Similarly to get_min_max(), to test this function requires mock data from API.
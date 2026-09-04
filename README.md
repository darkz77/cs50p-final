# Ask Temperature CLI

### Video Demo: <URL HERE>

### Author:
**Name**: Nguyen Minh Hoang
**Github**: darkz77
**edX**: ngmhoang202@gmail.com
**City * Country**: Da Nang - Vietnam
**Date of publish**: TBD

### Description:
1. What is Ask Weather CLI?
Ask Temperature CLI is a simple tool for you to quickly check the temperature of your city. 
This tool uses Open Meteo's Geolocation API to fetch the latitude and longitude of your inputted city so you don't have to search them yourself. Just simply input your city name.
You can check your current apperent temperature right now or ask for a forecast for X days ahead or a min/max temperature for the next 7 days.

2. Technical approach:
All of the function of this tool stays inside 1 project.py file. Where main() is the navigator to different function and keep the program alive until user wants to shutdown. This approach makes this CLI similar to GUI tool.
Other functions are separated so that it can be small enough so that I can maintain them separately and easily in the future. Each function serve a small and testable chunk of work
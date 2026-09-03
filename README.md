# Weather CLI

#### Video Demo: <URL HERE>

#### Description:

Weather CLI is a command-line application, written for CS50's Introduction to
Programming with Python final project, that lets a user look up weather
information for any city in the world by name. Rather than requiring the user
to know a location's coordinates, the program resolves a plain-language city
name to a latitude and longitude using the Open-Meteo Geocoding API, and then
uses those coordinates to query the Open-Meteo Forecast API for three kinds
of weather data: the daily minimum and maximum temperature, an hourly
temperature forecast for a user-specified number of days, and the current
temperature. Results that consist of a table (the daily min/max and the
hourly forecast) are rendered as a formatted grid in the terminal using the
`tabulate` library, so the output is easy to read directly from the console
without any extra tooling.

The project is intentionally a single file, `project.py`, since the amount
of logic involved does not justify splitting it into a package. It is
organized around one entry point, `main`, and five supporting functions that
each do one job:

- **`main`** drives the interactive menu loop. It repeatedly prompts the
  user to choose between Min/Max, Forecast, Current temperature, or Quit,
  validates that choice before doing any network work, and then dispatches
  to the appropriate function once a city has been resolved to coordinates.
- **`get_location`** takes a city name, calls the Open-Meteo Geocoding API,
  and returns the `(latitude, longitude)` of the best match, or reports that
  the city could not be found.
- **`get_min_max`** queries the Forecast API's daily endpoint and returns the
  min/max temperature for each of the next several days, paired with table
  headers for display.
- **`get_forecast`** asks the user how many days of forecast they want, then
  queries the Forecast API's hourly endpoint and returns an hour-by-hour
  temperature table for that span.
- **`get_current_temp`** queries the Forecast API's current-conditions
  endpoint and returns the temperature right now.
- **`generate_table`** is a small, pure formatting helper shared by the two
  table-producing functions above; it wraps `tabulate` so that table layout
  logic lives in exactly one place instead of being duplicated.

A few design choices are worth calling out. Open-Meteo was chosen as the
weather provider because it is free, requires no API key, and offers both
geocoding and forecast data from the same provider, which keeps the project
free of credential management. Network calls are deliberately isolated in
their own functions rather than inlined in `main`, so that `main` stays
focused on user interaction and each API call can be tested independently.
User input is handled with a retry loop pattern — invalid input, such as a
non-numeric number of forecast days, prints a message and loops back to the
prompt instead of crashing the program, since a CLI tool that exits on the
first typo is frustrating to use.

`requirements.txt` lists the two third-party packages the project depends
on: `requests`, for making HTTP calls to the Open-Meteo APIs, and
`tabulate`, for formatting tabular output. Both are installed with
`pip install -r requirements.txt` before running `python project.py`.

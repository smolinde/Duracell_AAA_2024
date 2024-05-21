# Weather Data Scraping
## 1 Sources
To retrieve accurate weather data for the project we utilize [Weather Underground](https://www.wunderground.com/), [Chromedriver](https://chromedriver.chromium.org/downloads), and a modification of a Python script from [this github repository](https://github.com/zperzan/scrape_wunderground).
## 2 Modifications
The offered script is outdated and had to be modified in order to satisfy new Python syntax and selenium Chromedriver import.
## 3 Prerequisites
1. The machine used for this tutorial runs on [Windows 10](https://www.microsoft.com/en-us/software-download/windows10) or [Windows 11](https://www.microsoft.com/en-us/software-download/windows11)
2. [Google Chrome](https://www.google.com/chrome/) is installed (latest version)
3. [Chrome Driver executable file](https://chromedriver.chromium.org/downloads) is downloaded (corresponding version to your Chrome installation)
4. [Python for Windows](https://www.python.org/downloads/windows/) is installed (3.11 or 3.12 recommended)
5. [Selenium for Python](https://selenium-python.readthedocs.io/) is installed (corresponding version to your Python installation)
6. All the other Python dependencies mentioned in the [github repository](https://github.com/zperzan/scrape_wunderground) are installed
7. You have ~2 hours of time
## 4 Usage
1. Place the ```scrape_wunderground.py```, ```scrape_all_weather.py```, and ```chromedriver.exe``` files into one directory of your choice
2. Edit ```scrape_all_weather.py``` with an editor of your choice and set the station ID, date range, and weather interval
3. In [PowerShell](https://learn.microsoft.com/en-us/powershell/), navigate with the ```cd``` command to the chosen directory
4. Start the script by running ```python scrape_all_weather.py```
5. Don't get scared by the constantly popping up Chrome tab. Let the script do its thing 😉
6. Press ```WINDOWS + L``` and come back in about two hours if you are retrieving data for one whole year in 5 minute intervals
7. Log into your PC. If there is no Chrome tab popping up the script probably terminated. In the same directory you shall find a new file called ```weather_data.csv```
8. Your file is ready for further usage
# 5 Contents
The output file contains following data columns:
* Timestamp (yyyy-mm-dd hh:mm:ss, local time)
* Temperature (°F)
* Dew Point (°F)
* Humidity (%)
*  Wind Speed (mph)
*  Wind Gust (mph)
*  Pressure (in)
*  Precipitation Rate (in)
*  Precipitation Accumulation (in)
# 6 Troubleshooting
If something doesn't work as expected it might be due to changes within selenium library and/or the Weather Underground website itself. Search the internet, there are many possible solutions! If you get an empty dataset it might be that the station you selected does not have data available for the selected year. In this case, manually find another station in the same city that does have data entries for the desired date range.
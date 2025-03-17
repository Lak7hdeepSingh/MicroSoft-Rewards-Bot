# Bing Search Automation Script  
This is a Python script that automates Bing searches using the Selenium library. It simulates human-like behavior by performing randomized searches with delays, which can be useful for maximizing Bing reward points or automating search-based tasks.  

## 🚀 How It Works  
- ✅ Generates random search terms using the Faker library.  
- ✅ Opens Bing in the Edge browser and performs a search.  
- ✅ Waits for a random delay between searches to mimic human behavior.  
- ✅ Repeats the process 30 times (configurable).  

## 📂 Setup  
Install the required libraries:  
```bash
pip install selenium faker
```
## 🔥 Usage
Run the script in command Promt using:
```
python script.py
```
## 🛠️ Requirements
+ Python 3.8+
+ Microsoft Edge browser
+ Edge WebDriver

## ✅ Features
- ✔️ Automates up to 30 searches (adjustable)
- ✔️ Simulates human-like behavior with random delays
- ✔️ Clean termination with try-except-finally handling

## 👨‍💻 How to Customize
- To adjust the number of searches, change the value in:
```
for _ in range(30):
```
To modify the delay time, adjust the range in:
```
time.sleep(random.uniform(5, 10))
```
## Updating the Driver Path
- To make the script work, you need to update the driver_path variable with the correct path to your Edge WebDriver:

- Download the Edge WebDriver from the official Microsoft site:
[Download Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)


- Extract the downloaded file and place the msedgedriver.exe file in a known location (e.g., C:\Users\<YourUsername>\Downloads).

- Open the script and update the driver_path variable with the correct location of the WebDriver:
```
driver_path = r"C:\Users\<YourUsername>\Downloads\msedgedriver.exe"
```
- Save the changes and run the script! ✅

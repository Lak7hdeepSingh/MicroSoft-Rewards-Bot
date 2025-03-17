import time
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

fake = Faker()


options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")


driver_path = r"C:\Users\Lak7h\OneDrive\Desktop\Automate\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

def search_bing():
    search_term = fake.word()
    driver.get("https://www.bing.com")
    

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    
    print(f"Searching on Bing: {search_term}")

def main():
    try:
        for _ in range(30):  
            search_bing()
            time.sleep(random.uniform(5, 10))  
        print("Searches completed!")
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

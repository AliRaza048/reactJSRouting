import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver ka path specify karein
chrome_driver_path = "E:/bot/glbot/chromedriver.exe"  # Actual path ke saath replace karein

# Initialize ChromeOptions
chrome_options = Options()

# Initialize ChromeDriver service
service = Service(chrome_driver_path)

# Start the ChromeDriver service
service.start()

# Initialize ChromeDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the login page
driver.get("https://getlike.io/en/login/")

# Add a delay to allow time for manual login (adjust as needed)
time.sleep(60)  # 60 seconds for you to manually log in

# Capture the cookies after login
cookies = driver.get_cookies()

# Quit the driver
driver.quit()

# Initialize a new ChromeDriver session
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the task page
driver.get("https://getlike.io/en/tasks/")

# Set the captured cookies in the new session
for cookie in cookies:
    driver.add_cookie(cookie)

try:
    # Rest of your code here...

    time.sleep(10)

    # Now find and click the button on the new page
    new_page_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "list-3-1"))
    )
    new_page_button.click()

    time.sleep(10)

    # Task ka button dhoondhein aur click karein
    task_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "do-task"))
    )
    task_button.click()

    # Rest of your code...

except Exception as e:
    print("An error occurred:", str(e))

# Quit the driver
driver.quit()





# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # ChromeDriver ka path specify karein
# chrome_driver_path = "E:/bot/glbot/chromedriver.exe"  # Actual path ke saath replace karein
#
# # Initialize ChromeOptions
# chrome_options = Options()
#
# # Initialize ChromeDriver service
# service = Service(chrome_driver_path)
#
# # Start the ChromeDriver service
# service.start()
#
# # Initialize ChromeDriver with the specified service and options
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to the login page
# driver.get("https://getlike.io/en/login/")
#
# # Add a delay to allow time for manual login (adjust as needed)
# time.sleep(60)  # 60 seconds for you to manually log in
#
# try:
#     # Wait for the dashboard header element to appear
#     dashboard_header_element = WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "page-header"))
#     )
#
#     # Wait for 20 seconds to ensure the dashboard is fully loaded
#     time.sleep(20)
#
#     # Click on the "task" button
#     task_button_element = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/tasks/']"))
#     )
#     task_button_element.click()
#
#
#     time.sleep(10)
#
#     # Now find and click the button on the new page
#     new_page_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "list-3-1"))
#     )
#     new_page_button.click()
#
#     time.sleep(10)
#
#     # Task ka button dhoondhein aur click karein
#     task_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, "do-task"))
#     )
#     task_button.click()
#
#     time.sleep(20)
#
#     # Naye window ka intezar karein
#     new_window_handle = WebDriverWait(driver, 20).until(EC.new_window_is_opened)
#
#     # Naye window mein switch karein
#     driver.switch_to.window(new_window_handle)
#
#     # Naye window ka intezar karein
#     WebDriverWait(driver, 20).until(EC.url_changes(driver.current_url))
#
#     # Message print karein jo naye window ka sahi tarah se load hone ki taraf ishara kare
#     print("New window loaded successfully:", driver.current_url)
#
#     # 30 seconds ke liye observation ke liye intezar karein
#     time.sleep(30)
#
#
# except Exception as e:
#     print("An error occurred:", str(e))
#
# # Quit the driver
# driver.quit()



# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Specify the path to the ChromeDriver executable
# chrome_driver_path = "E:/bot/glbot/chromedriver.exe"  # Replace this with the actual path
#
# # Initialize ChromeOptions
# chrome_options = Options()
#
# # Set any desired options here (if needed)
#
# # Initialize the ChromeDriver service
# service = Service(chrome_driver_path)
#
# # Start the ChromeDriver service
# service.start()
#
# # Initialize ChromeDriver with the specified service and options
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to the login page
# driver.get("https://getlike.io/en/login/")
#
# # Add a delay to allow time for manual login (adjust as needed)
# time.sleep(60)  # 60 seconds for you to manually log in
#
# # Wait for the dashboard element to appear (adjust as needed)
# # dashboard_element = WebDriverWait(driver, 60).until(
# #     EC.visibility_of_element_located((By.CLASS_NAME, "dashboard-class"))
# # )
# dashboard_element = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "page-header"))
# )
#
# # Once the dashboard is visible, find the button element by XPath
# button_element = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/taskmarket']"))
# )
# # Click on the button
# button_element.click()
#
# # Add a delay to observe the action (adjust as needed)
# time.sleep(10)
#
# # Don't forget to quit the driver when done
# driver.quit()




# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Specify the path to the ChromeDriver executable
# chrome_driver_path = "E:/bot/glbot/chromedriver.exe"  # Replace this with the actual path
#
# # Initialize ChromeOptions
# chrome_options = Options()
#
# # Set any desired options here (if needed)
#
# # Initialize the ChromeDriver service
# service = Service(chrome_driver_path)
#
# # Start the ChromeDriver service
# service.start()
#
# # Initialize ChromeDriver with the specified service and options
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to the website
# driver.get("https://getlike.io/")
#
# # Add a delay to ensure the page is fully loaded
# time.sleep(5)
#
# # Locate the dropdown button element
# dropdown_button = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
#
# # Click the dropdown button to show the list
# dropdown_button.click()
#
# # Wait for the language options to appear
# language_option = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and @href='/en/']"))
# )
#
# # Click the language option to change the language to English
# language_option.click()
#
# # Add a delay to observe the change (you can adjust this as needed)
# time.sleep(500)
#
# # Quit the driver
# driver.quit()








#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# # Specify the path to the ChromeDriver executable
# chrome_driver_path = "E:/bot/glbot/chromedriver.exe"  # Replace this with the actual path
#
# # Initialize ChromeOptions
# chrome_options = Options()
#
# # Set any desired options here (if needed)
#
# # Initialize the ChromeDriver service
# service = Service(chrome_driver_path)
#
# # Start the ChromeDriver service
# service.start()
#
# # Initialize ChromeDriver with the specified service and options
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to a specific website
# driver.get("https://getlike.io/")
#
# # Add a delay to keep the browser window open for 10 seconds (you can adjust this time)
# time.sleep(500)
#
# # Don't forget to quit the driver when done
# driver.quit()

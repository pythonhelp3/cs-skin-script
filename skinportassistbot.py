import undetected_chromedriver as uc
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from database import Database
import os

db = Database()

# Find and select the "Add to cart" button after a qualifying item is found

class Bot:

    filtered_items = []

    def __init__(self, enable, run):
        if(enable == True):
            self.options = Options()
            # The profile directory user has to be the chrome profile you want to use, I used chrome profile named "Profile 1"
            self.options.add_argument('--profile-directory=user')
            # This argument needs to be the path of your chrome profile minus the profile name, such as this C:\\Users\\USERNAME\\AppData\\Local\\Google\\Chrome\\User Data\\
            self.options.add_argument(r"--user-data-dir=app-data")
            self.driver = uc.Chrome(options=self.options)
            
# This part of the code is not opening the link in chrome even once chrome is open

            print("App-Data folder generated.")

            print("Opening Webpage")
            
            
            if(run == True):
                self.driver.get("https://skinport.com/market?sort=date&order=desc")
                pass
        

    def start(self):
        print("Starting Bot")
        filtered_item = []  # input("Please enter the items you wish to filter: ")
        discount = input("Please enter the discount: ")
        price = input("Please enter the price: ")
        # cart_items = input()

        self.find_item(filtered_items = filtered_item, discount = discount, price = price, cart_items=1)
        self.make_purchase()

    # Setter function for filtering for later
    def add_filter(self, item_list):
        return self.filtered_items.append(item_list)
    
    # this helper function will drive the bot to make a purchase 
    def make_purchase(self):
        # Wait for the cart element to have a value of :cart_items    
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".CartButton-count"), 1))

        # Find the first element and click it
        cart_button = driver.find_element(By.CSS_SELECTOR, ".CartButton-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_button).click().perform()

        # Wait for the second element to be clickable and click it
        view_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".CartButton-viewCart")))
        actions.move_to_element(view_cart_button).click().perform()

        # Wait for the checkboxes to appear and click them
        check_box1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tradelock']")))
        check_box2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='cancellation']"))) 

        # Perform the checkbox clicking actions using action chains
        actions = ActionChains(self.driver)
        actions.move_to_element(check_box1).click().perform()
        actions.move_to_element(check_box2).click().perform()

        # Click the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SubmitButton-title")))
        proceed_to_checkout_button.click()

        # Click the CSV element
        pyautogui.moveTo(1262, 348)
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.typewrite('145')

        # Click the pay now button
        pyautogui.moveTo(1226, 419)
        time.sleep(0.1)
        pyautogui.click()

        # Update the cookies to store the state of the checkboxes
        # tradelock_value = str(check_box1.is_selected()).lower()
        # cancellation_value = str(check_box2.is_selected()).lower()

        # # Write function that will tell me if there exist a database file
        # if os.path.exists(os.getcwd() + "/database.db"):
        #     print("file found")
        # else:
        #     print("file not found")




    # this helper function will drive the bot to make selections based on prices, discounts, items allowed in cart, etc.
    def find_item(self, filtered_items, discount, price, cart_items):

        print("Filtered Items", filtered_items)
        print("Discount", discount)
        print("Price", price)

        # print("Press Ctrl-C to quit.") # to be used while the bot is running in the background

        try:
            if(self.driver.current_url == 'https://skinport.com/market?sort=data&order=desc'):
                # scape the page for discounted elements
                de = self.driver.find_elements(By.CSS_SELECTOR, ".GradientLabel.ItemPreview-discount span")
                actions = ActionChains(self.driver)

                for discount_element in de:
                    discount_value = int (discount_element.text.strip("− %"))

                    # if the discount value is greater than discount% than find the item, price and add to cart
                    if discount_value >= discount:
                        item_element = discount_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'ItemPreview')]")

                        # Find the price element and extract the price value
                        price_element = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-priceValue .Tooltip-link")
                        price_value = float(price_element.text.strip("$"))

                        # Once item is found sort throught the filter list to identify whether or not the item
                        #   added to the list (Not sure if this works lol)
                        if 4 < price_value <= 10 and item_element not in filtered_items:
                            # Hover over the item to reveal the "Add to cart" button
                            actions.move_to_element(item_element).perform()

                            # Add a small delay to ensure the "Add to cart" button is displayed
                            time.sleep(0.05)

                            # Find and click the "Add to cart" button
                            add_to_cart_button = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-mainAction")
                            add_to_cart_button.click()

                            # Add the item to the filtered items list
                            filtered_items.append(item_element)

                            # Print the item details
                            item_name_element = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-name")
                            item_name = item_name_element.text
                            print(f"Added {item_name} to cart")

                        break

                        # Wait for the cart element to have a value of 1
            cart_count = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".CartButton-count"), "1"))

            # Find the first element and click it
            cart_button = self.driver.find_element(By.CSS_SELECTOR, ".CartButton-button")
            actions = ActionChains(self.driver)
            actions.move_to_element(cart_button).click().perform()

            # Wait for the second element to be clickable and click it
            view_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".SubmitButton.CartDropdown-checkout")))
            actions.move_to_element(view_cart_button).click().perform()

            # Wait for the checkboxes to appear and click them
            check_box1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tradelock']")))
            check_box2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='cancellation']")))

            # Perform the checkbox clicking actions using action chains
            actions = ActionChains(self.driver)
            actions.move_to_element(check_box1).click().perform()
            actions.move_to_element(check_box2).click().perform()

            # Click the "Proceed to Checkout" button
            proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SubmitButton-title")))
            proceed_to_checkout_button.click()

            # Click the CVC element
            pyautogui.moveTo(1262, 348)
            time.sleep(1)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.typewrite('145')

              #Click the pay now button
            pyautogui.moveTo(1226, 419)
            time.sleep(0.1)
            pyautogui.click()

            # Soon to add a new database for simplifying trades, cancellations, etc.. May revert
            #    to sessions cookies but will test running times very soon.

             
        except:
            # KeyboardInterrupt()
            print('\n')
            pass


# Testing Features

bot = Bot(enable=True, run=True) # working 
# (Camden comment) The false statement also needed to be in quotations for the bot to run, I will test the bot now and let you know about further errors
bot.start()

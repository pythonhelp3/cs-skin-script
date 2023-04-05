import undetected_chromedriver as uc
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time





# Find and select the "Add to cart" button after a qualifying item is found

class Bot:
    def __init__(self, enable, run):
        if(enable == True):
            self.options = Options()
            self.options.add_argument('--profile-directory=user')
            self.options.add_argument(r"--user-data-dir=app-data")
            self.driver = uc.Chrome(options=self.options)

            print("App-Data folder generated.")

            print("Opening Webpage")
            
            if(run == True):
                self.driver.get("https://skinport.com/market?sort=date&order=desc")
                pass
        

    def start(self):
        print("Starting Bot")


        self.find_item(filtered_items = [], discount = 27, price = 4, cart_items=1)


    # this helper function will drive the bot to make selections based on prices, discounts, items allowed in cart, etc.
    def find_item(self, filtered_items, discount, price, cart_items):

        print("Filtered Items", filtered_items)
        print("Discount", discount)
        print("Price", price)

        try:
            if(driver.current_url == 'https://skinport.com/market?sort=data&order=desc'):
                # scape the page for discounted elements
                de = driver.find_elements(By.CSS_SELECTOR, ".GradientLabel.ItemPreview-discount span")
                actions = ActionChains(driver)

                for discount_element in de:
                    discount_value = int (discount_element.text.strip("− %"))

                    # if the discount value is greater than discount% than find the item, price and add to cart
                    if discount_value >= discount:
                        item_element = discount_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'ItemPreview')]")

                        # Find the price element and extract the price value
                        price_element = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-priceValue .Tooltip-link")
                        price_value = float(price_element.text.strip("$"))

                        # Check if the price value if greater than $price
                        if price_value >= price:
                            # Hover over the item to reveal the "Add to cart" button
                            actions.move_to_element(item_element).perform()

                            # Add a small delay to ensure the "Add to cart" button is displayed
                            time.sleep(0.5)

                            # Find and click the "Add to cart" button
                            add_to_cart_button = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-mainAction")
                            add_to_cart_button.click()
                            break

                # Wait for the cart element to have a value of :cart_items    
                cart_count = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".CartButton-count"), cart_items))

                # Find the first element and click it
                cart_button = driver.find_element(By.CSS_SELECTOR, ".CartButton-button")
                actions = ActionChains(driver)
                actions.move_to_element(cart_button).click().perform()

                # Wait for the second element to be clickable and click it
                view_cart_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".CartButton-viewCart")))
                actions.move_to_element(view_cart_button).click().perform()

        except:
            pass


    # this helper function will drive the bot to make a purchase   
    def make_purchase(self):
        pass







# Testing Features

bot = Bot(enable="True", run=False) # working
bot.start()

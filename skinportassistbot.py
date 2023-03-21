import undetected_chromedriver as uc
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Set up the webdriver (assuming you have already installed it)
options = Options()
options.add_argument('--profile-directory=user')
options.add_argument(r"--user-data-dir=app-data")
driver = uc.Chrome(options=options)

# Navigate to the skinport.com/cart page
driver.get("https://skinport.com/market?sort=date&order=desc")


# changing this soon to only run for a certain amount of time, so that it will not get caught
# within an infinte loop when there are no items to buy, trade, or sell.
while True:
    try:
        # get current url
        if driver.current_url == 'https://skinport.com/market?sort=date&order=desc':


            # scapes the page for the discouted elements 
            discount_elements = driver.find_elements(By.CSS_SELECTOR, ".GradientLabel.ItemPreview-discount span")
            actions = ActionChains(driver)

            for discount_element in discount_elements:
                discount_value = int(discount_element.text.strip("− %"))

                if discount_value >= 27:
                    item_element = discount_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'ItemPreview')]")

                    # Find the price element and extract the price value
                    price_element = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-priceValue .Tooltip-link")
                    price_value = float(price_element.text.strip("$"))

                    # Check if the price value is greater than $4
                    if 4< price_value <= 10:
                        # Hover over the item to reveal the "Add to cart" button
                        actions.move_to_element(item_element).perform()

                        # Add a small delay to ensure the "Add to cart" button is displayed
                        time.sleep(0.5)

                        # Find and click the "Add to cart" button
                        add_to_cart_button = item_element.find_element(By.CSS_SELECTOR, ".ItemPreview-mainAction")
                        add_to_cart_button.click()
                        break

            # Wait for the cart element to have a value of 1
            cart_count = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".CartButton-count"), "1"))

            # Find the first element and click it
            cart_button = driver.find_element(By.CSS_SELECTOR, ".CartButton-button")
            actions = ActionChains(driver)
            actions.move_to_element(cart_button).click().perform()

            # Wait for the second element to be clickable and click it
            view_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".SubmitButton.CartDropdown-checkout")))
            actions.move_to_element(view_cart_button).click().perform()

        # Wait for the checkboxes to appear and click them
        check_box1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tradelock']")))
        check_box2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='cancellation']")))

        # Perform the checkbox clicking actions using action chains
        actions = ActionChains(driver)
        actions.move_to_element(check_box1).click().perform()
        actions.move_to_element(check_box2).click().perform()

        # Click the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SubmitButton-title")))
        proceed_to_checkout_button.click()

        # Click the CVC element
        pyautogui.moveTo(1262, 348)
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.typewrite('146')

        #Click the pay now button
        pyautogui.moveTo(1226, 419)
        time.sleep(0.1)
        pyautogui.click()

        break

        # Update the cookies to store the state of the checkboxes
        tradelock_value = str(check_box1.is_selected()).lower()
        cancellation_value = str(check_box2.is_selected()).lower()
        driver.add_cookie({"name": "tradelock", "value": tradelock_value})
        driver.add_cookie({"name": "cancellation", "value": cancellation_value})

        print("Checkboxes clicked successfully!")
        break  # Stop looping after checkboxes are clicked

    except:
        # If the checkboxes are not found on the page, refresh the page
        # and wait for 5 seconds before retrying
        print("Checkboxes not found. Refreshing the page and retrying in 5 seconds...")
        time.sleep(1)

while True:
    # Wait for the user to leave the skinport.com/cart page
    while "cart" in driver.current_url:
        time.sleep(1)

    # Wait for the user to navigate back to the skinport.com/cart page
    while "cart" not in driver.current_url:
        time.sleep(1)

    # Perform the function again if the user navigates back to the link
    if driver.current_url == 'https://skinport.com/market?sort=date&order=desc':
        # Wait for the cart element to have a value of 1
        cart_count = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".CartButton-count"), "1"))

        # Find the first element and click it
        cart_button = driver.find_element(By.CSS_SELECTOR, ".CartButton-button")
        actions = ActionChains(driver)
        actions.move_to_element(cart_button).click().perform()

        # Wait for the second element to be clickable and click it
        view_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".SubmitButton.CartDropdown-checkout")))
        actions.move_to_element(view_cart_button).click().perform()

    # Click the checkboxes
    try:
        check_box1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tradelock']")))
        check_box2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='cancellation']")))

        # Perform the checkbox clicking actions using action chains
        actions = ActionChains(driver)
        actions.move_to_element(check_box1).click().perform()
        actions.move_to_element(check_box2).click().perform()

        # Update the cookies to store the state of the checkboxes
        tradelock_value = str(check_box1.is_selected()).lower()
        cancellation_value = str(check_box2.is_selected()).lower()
        driver.add_cookie({"name": "tradelock", "value": tradelock_value})
        driver.add_cookie({"name": "cancellation", "value": cancellation_value})

        # Click the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SubmitButton-title")))
        proceed_to_checkout_button.click()

        # Click the CVC element
        pyautogui.moveTo(1262, 348)

        
        print("Checkboxes clicked successfully!")
    except:
        print("Checkboxes not found. Retrying in 5 seconds...")

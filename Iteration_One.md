(Camden comment): Feel free to delete everything I typed in here once it has been changed, or use a different iteration to implement said changes :D

### Initialization of the bot
``` python 
Set up the webdriver (assuming you have already installed it)
options = Options()
options.add_argument('--profile-directory=user')
options.add_argument(r"--user-data-dir=app-data")
driver = uc.Chrome(options=options)

Navigate to the skinport.com/cart page
driver.get("https://skinport.com/market?sort=date&order=desc")
```
This function (provided by Camden): from my understanding searches the page for a specific item and adds it to the cart, then proceeds to checkout
and saves the items data in a cookie file... 
(Comment from Camden):
This is mostly correct, however, I think a cookie file should be used on the store page when going through each item and checking for discount, not when checking out. By doing this, it will function quicker like you are mentioning. The data isn't very important to me and I am mainly using it so it doesn't try to purchase items with the discount and price variables requested that have already been purchased so that it saves times searching through the page which is constantly updated with more listings. If there is also a way to wipe that data each time the bot is stopped and creating a new cookie file to repeat the process that would be helpful.

(Comment from Evan): Camden,  I think this function will work well. I intented to add your filtered items soon after I get the bot to working. I think I would be a great idea to make a SQLite3 database to store the items and their data. I think this would be a great way to keep track of the items. I believe it will allow the bot to run faster then before. If you would like to start on creating Database functions then I will prepare the helper functions with the new functionalities.

(Comment from Camden): I'm not familiar with creating database functions but if there is information you need provided of what to avoid I can give a few examples here and then add more later on my own.

Example: Any item with the name "XM1014", any knife/daggers with the word "StatTrak" in it, any item with the word "case" in it


``` python 
First Iteration of the Bot find, and purchase functionalities courtesy of Camden (and a job well done to offer)
while True:
    try:
        # get current url
        if driver.current_url == 'https://skinport.com/market?sort=date&order=desc':

            # Wait for the button to be clickable
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "LiveBtn"))
            )

            # Click the button only if the second element is not present
            if not driver.find_elements(By.CLASS_NAME, "LiveBtn--isActive"):
                button.click()
            # ^ This code is used to click the live button when the page opens so new listings will appear, it wasn't in the original code I sent you. <-----Camden comment

            # scrapes the page for the discounted elements 
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
                        time.sleep(0.05)

                        # ^ I changed the timing on this function because I found it doesn't need that much of a delay and can find the cart button very quickly <----- Camden comment
                        
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
        pyautogui.typewrite('145')

        # 
        # ^ If there is a way to speed up this process I would like to know, typically the website just takes a second to load which is why I have the manual timings entered but if there is a way to immediately detect when the element is clickable, that would be ideal <----- Camden comment
        
        #Click the pay now button
        pyautogui.moveTo(1226, 419)
        time.sleep(0.1)
        pyautogui.click()

        # ^ Same with this process, it is manually timed and if there is a way to just detect the "pay now" button element and click it when it is available, that would work well <---- Camden comment
        
        break

        # Update the cookies to store the state of the checkboxes
        tradelock_value = str(check_box1.is_selected()).lower()
        cancellation_value = str(check_box2.is_selected()).lower()
        driver.add_cookie({"name": "tradelock", "value": tradelock_value})
        driver.add_cookie({"name": "cancellation", "value": cancellation_value})

        print("Checkboxes clicked successfully!")
        break  # Stop looping after checkboxes are clicked

        # ^ This is used because when I left the checkout page and went back with a new item, it was not clicking the checkboxes anymore. This just checks if it has been checked or not <--- Camden comment

    except:
        # If the checkboxes are not found on the page, refresh the page
        # and wait for 5 seconds before retrying
        print("Checkboxes not found. Refreshing the page and retrying in 5 seconds...")
        time.sleep(1)

        # ^ I don't have this set up to refresh the page, it just waits for the user to go to the checkout screen to detect the checkboxes, can be modified as needed but if it works then that's fine <--- Camden comment
```

Second Function: (Provided by Camden)
I will write a mark up of my understanding shortly

TLDR: this will help check out items, and save them into a cookie.

(Camden comment): I'm not entirely sure if some of this is redundant, I used it to reset the loop of checking for items if checkout was unsuccessful. I would like to have a function added that can navigate back to the original URL and click the live button again to repeat the process of searching for items. 

```python
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


```



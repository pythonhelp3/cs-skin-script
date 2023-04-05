

#### Introduction:

This application is intended to provide alogritmic trading options that watch for price fluxuations that will indicate a decrease in price, or discount.

#### Requirements
The code will open a website. The website lists in-game items. The items have a discount. If the discount is 27% or greater then they are automatically added to the cart. The price range and discount ranges are set, but future iterations will allow for easy adjustments. 

The next update will include specifying the "*types*" (cases, descriptions, conditions, etc.) of trade item that will be exclude from the search parameters. 

If an item is added to the cart but has already been purchased by another user, it will navigate back to the previous tab and select the "live" function to continue searching for new items that meet the previously mentioned criteria.

Implementing a notification system for the user when an item has been purchased but still requires payment. For example, if you purchase an item and enter your credit card details incorrectly, it will still reserve the item for up to 30 minutes until payment has been received using the correct card details. If payment is not received, it automatically relists the item with no further action required by the user. The reason this is useful is because it allows the user to review the item they have checked out and decide if they still want to purchase it. However, a notification system would be helpful if the user is away from their computer to inform them about the pending purchase.

#### Analysis

For the development of this application, with the help of the Author, I will create a simple waterfall diagram that will allow us to issues copies of the application as itended throught each step of the process. Ideally, this should be simple, and agile upon developement.

Thanks to Camden, an inital copy of the first iteration of code has been provided. Under the MIT open source copyright laws, I've obtained a working copy and will soon prepare an easy to use Development Environment. 

So far this application uses only Python, but after a closer look, I've realized that a simple User Interface may be necessary. It is a continued work in progress. 

Before I begin: I will upload a progress model that includes class diagrams, and UML charts that simplify the flow of instructions, and data operations. 

#### Development

To be continued.

#### Packages included:

- *Undetected Chromedriver*
- *PyAutoGUI*
- *Selenium*
- *Webdriver*
- *Time*




#### Todos:

- Object Oriented Diagram Analysis
    - *description*
    - *class names*
    - *uses cases*

- Scenario Diagram
    - *uses case* $\rightarrow$ (client info)
    - *scenario cases*

- Class Modules
    - *Api*
    - *Client*
    - *BotContainer*

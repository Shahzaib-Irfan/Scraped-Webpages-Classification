# AliExpress Web Scraping

## Introduction

This documentation provides a detailed overview of a web scraping script written in Python. The script utilizes the Selenium and BeautifulSoup libraries to scrape product titles from the AliExpress website for the search term "Food".

## Tools Used

- **Python**: Python is a high-level programming language known for its simplicity and readability. It is widely used for web scraping due to its rich ecosystem of libraries.
- **Selenium**: Selenium is a popular web automation tool that allows developers to interact with web pages programmatically. It supports multiple web browsers and provides features for simulating user actions.
- **BeautifulSoup**: BeautifulSoup is a Python library for parsing HTML and XML documents. It provides convenient methods for extracting data from web pages using various selection criteria.
- **Firefox WebDriver**: WebDriver is a component of Selenium that provides a platform-specific interface for controlling web browsers. In this script, we use the Firefox WebDriver to automate interactions with the Firefox browser.

## Script Overview

The provided Python script scrapes product titles from AliExpress search results pages and saves them to a CSV file. It utilizes Selenium to navigate through multiple pages of search results and BeautifulSoup to extract product titles from the HTML content.

## Detailed Steps

### 1. Imports

The script starts by importing the necessary Python modules:

- `requests`: Library for making HTTP requests (not used in this script).
- `BeautifulSoup`: Library for parsing HTML and XML documents.
- `webdriver`: Module from Selenium for automating web browser interactions.
- `By`: Enum from Selenium for locating elements on a web page.
- `Keys`: Class from Selenium for sending keyboard keys to web elements.
- `Select`: Class from Selenium for interacting with dropdowns.
- `WebDriverWait`: Class from Selenium for waiting for conditions to be met.
- `EC`: Module from Selenium for defining expected conditions.
- `NoSuchElementException`: Exception class from Selenium for handling missing elements.
- `NoAlertPresentException`: Exception class from Selenium for handling missing alerts.
- `sys`: Module providing access to system-specific parameters and functions.
- `unittest`: Framework for organizing test cases.

### 2. Selenium Setup

The `setUp()` method initializes the Selenium WebDriver for Firefox browser. It sets up implicit waits and defines variables such as the base URL and error verification lists.

### 3. Test Method

The `test_sel()` method contains the main scraping logic. It iterates through multiple pages of search results, scrolls down to load more products dynamically, extracts product titles using BeautifulSoup, and saves them to a CSV file.

### 4. Main Execution

The `if __name__ == "__main__":` block executes the test case when the script is run directly. It triggers the execution of the test case defined in the `test_sel()` method.

## Usage Instructions

1. **Prerequisites**: Ensure you have Python installed on your system.
2. **Library Installation**: Install the required libraries using `pip install requests beautifulsoup4 selenium`.
3. **WebDriver Setup**: Download the Firefox WebDriver compatible with your Firefox browser version and update the `path` variable in the script to its location.
4. **Script Execution**: Run the script using `python script_name.py`.

## Conclusion

This documentation provides a comprehensive overview of the web scraping script for AliExpress. It explains each step of the script in detail and provides instructions for usage. You can customize and extend the script according to your specific scraping requirements.
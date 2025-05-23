from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def automate_frill_voting(url, num_votes=10):
    """
    Automates voting on a Frill.co-like roadmap system by repeatedly
    opening a new incognito browser, navigating to the URL, and clicking a vote button.
    The browser window will be set to a mobile-like size to ensure the correct layout.

    Args:
        url (str): The URL of the specific feature topic page on Frill.co.
        num_votes (int): The total number of times to perform the voting action.
    """
    print(f"Starting automated voting for {num_votes} times on: {url}")

    # Using the full XPath provided by the user for precise targeting.
    # Note: Absolute XPaths can be brittle if the page structure changes.
    VOTE_BUTTON_XPATH = "/html/body/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/button"

    for i in range(num_votes):
        print(f"\n--- Vote attempt {i + 1}/{num_votes} ---")
        driver = None # Initialize driver to None for error handling in finally block
        try:
            # 1. Set up Chrome options for incognito mode and mobile window size
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

            # Set window size to a common mobile resolution (e.g., iPhone X)
            # This should trigger the mobile layout of the Frill.co page.
            chrome_options.add_argument("--window-size=375,812")
            # Optional: Run headless if you don't want to see the browser UI
            # chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--disable-gpu")

            # 2. Initialize the WebDriver for each iteration
            print("Launching new incognito browser instance with mobile dimensions...")
            driver = webdriver.Chrome(options=chrome_options)

            # 3. Navigate to the voting page
            print(f"Navigating to {url}...")
            driver.get(url)

            # 4. Wait for the vote button to be present and clickable using the specific XPath.
            print("Waiting for the vote button to be clickable using XPath...")
            vote_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, VOTE_BUTTON_XPATH))
            )

            # 5. Click the vote button using standard Selenium click.
            if vote_button:
                print("Vote button found. Attempting standard click...")
                vote_button.click()
                print("Vote clicked successfully!")

                # Add a short delay to allow the server to process the vote and UI to update
                time.sleep(3)
            else:
                print("Error: Vote button not found with the provided XPath.")

        except Exception as e:
            print(f"An error occurred during vote attempt {i + 1}: {e}")
            # Optionally, take a screenshot on error for debugging
            if driver:
                screenshot_filename = f"error_screenshot_attempt_{i+1}.png"
                driver.save_screenshot(screenshot_filename)
                print(f"Screenshot saved to {screenshot_filename}")
        finally:
            # 6. Always close the browser after each attempt
            if driver:
                print("Closing browser instance.")
                driver.quit()
            time.sleep(2)

    print("\nAutomated voting process complete.")
    print("Remember to check the Frill.co roadmap to verify the votes.")

# --- How to use this script ---
if __name__ == "__main__":
    # IMPORTANT: Replace with the actual URL of the Frill.co feature topic you want to vote on.
    # This should be the direct link to the feature that opens the side panel/full page view.
    FRIL_CO_URL = "https://roadmap.demo.io/feature-ideas/demofeature"

    # Set the number of votes you want to simulate
    NUMBER_OF_VOTES = 5 # Adjust this number for your stress test

    # Run the automation
    automate_frill_voting(FRIL_CO_URL, num_votes=NUMBER_OF_VOTES)

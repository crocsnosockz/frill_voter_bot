Frill.co Voting Automation Script

This Python script automates the process of voting on a Frill.co roadmap feature. It's designed for stress testing or repeatedly casting votes on a specific feature without requiring manual intervention or signing in. The script simulates a fresh user session for each vote by launching a new incognito browser window, effectively bypassing cookie and cache-based restrictions.
Features

    Automated Voting: Clicks the vote button on a specified Frill.co feature page.

    Incognito Mode: Each vote is cast from a clean, incognito browser session, simulating a new user and bypassing typical voting restrictions (like cookie-based limits).

    Mobile Viewport Simulation: Opens the browser in a mobile-like resolution to ensure the correct responsive layout of the Frill.co page, making the vote button easier to target.

    Robust Element Targeting: Uses a precise CSS selector to locate the vote button.

    Error Handling & Screenshots: Catches errors during the voting process and can save screenshots for debugging.

Prerequisites

Before running the script, ensure you have the following installed on your system:

    Python 3 and pip: Ensure you have Python 3 and its package installer (pip) installed.

    Google Chrome Browser: Make sure Google Chrome is installed.

    Selenium Library:

    pip install selenium

    ChromeDriver: This is a crucial component that allows Selenium to control your Chrome browser.

        Find your Chrome Browser Version: Open Chrome, type chrome://version/ in the address bar, and note down the major version number (e.g., 136).

        Download ChromeDriver: Go to the official ChromeDriver downloads page: https://googlechromelabs.github.io/chrome-for-testing/.

        Find the ChromeDriver version that matches your Chrome browser's major version under the "Stable" channel. Download the appropriate .zip file for your operating system (e.g., chromedriver-win64.zip for Windows, chromedriver-mac-arm64.zip for macOS, chromedriver-linux64.zip for Linux).

        Extract and Add to PATH: Unzip the downloaded file. You will find a chromedriver executable. Move this executable to a directory that is included in your system's PATH environment variable, and ensure it is executable.

How to Use

    Save the Script:
    Copy the Python code from the frill-voting-automation immersive (provided in the conversation) and save it as frill_voter.py (or any other .py name) in a convenient location on your computer.

    Configure the Script:
    Open the frill_voter.py file in a text editor and modify the following variables in the if __name__ == "__main__": block:

        FRIL_CO_URL:
        Replace the placeholder URL with the actual and complete direct URL of the specific Frill.co feature topic you want to vote on. This is the link that, when opened, displays the feature details (ideally in a full-page mobile layout due to the script's window sizing).

        FRIL_CO_URL = "hhttps://yourcompany.frill.co/roadmap/p/your-feature-topic-slug"

        NUMBER_OF_VOTES:
        Adjust this integer to the desired number of votes for your stress test.

        NUMBER_OF_VOTES = 5 # Adjust this number for your "stress test", don't overuse it. If it was voted 30+ times in a few minutes frame, frill will disable the voting process.

        VOTE_BUTTON_SELECTOR:
        This is currently set to button[aria-label='Vote for this Idea']. This selector works well for the Frill.co UI when viewed in a mobile layout. You generally should not need to change this. However, if the aria-label of the vote button on Frill.co ever changes, you would need to update this selector.

        Optional: Headless Mode:
        If you prefer the browser windows not to appear (i.e., the automation runs in the background), uncomment the following lines in the automate_frill_voting function:

        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")

    Run the Script:
    Open your terminal or command prompt, navigate to the directory where you saved frill_voter.py, and run:

    python frill_voter.py

    (You might need to use python3 frill_voter.py depending on your system's Python setup.)

The script will launch new incognito Chrome instances, navigate to the specified URL, click the vote button, and close the browser, repeating this process for the set number of votes. You will see progress messages in your console.
Troubleshooting

    "WebDriverException: Message: 'chromedriver' executable needs to be in PATH.":

        This means ChromeDriver is not correctly installed or not accessible via your system's PATH. Revisit step 3 in "Prerequisites" and ensure chromedriver is in a PATH directory and has appropriate executable permissions for your OS.

Feel free to contribute or suggest improvements!

Legal Disclaimer

Important: This script is intended for educational and testing purposes only. It should only be used to stress test Frill.co roadmap or feature request pages that you own or have explicit permission to test.

The author(s) or contributor(s) of this script:

    Are not responsible for any misuse of this script or any damages or disruptions caused by its use on systems or platforms for which you do not have proper authorization.

    Provide this script "as-is" without any warranties, express or implied.

    Do not endorse or encourage any activity that violates the Terms of Service of Frill.co or any other platform.

By using this script, you agree that you are solely responsible for your actions and any consequences that may arise from its use. Always ensure you are complying with all applicable laws and terms of service.

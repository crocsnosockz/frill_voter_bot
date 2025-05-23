# Frill.co Voting Automation Script

A Python script to automate voting on Frill.co feature pages. Designed for stress testing or repeated voting without login by simulating a new user session each time.

---

## Features

* **Automated Voting**: Clicks the vote button on a specific feature page.
* **Incognito Mode**: Uses new browser sessions to bypass cookies and cache.
* **Mobile View Simulation**: Sets a mobile viewport to ensure proper UI rendering.
* **Accurate Targeting**: Uses a stable CSS selector to find the vote button.
* **Error Handling**: Captures errors and can take screenshots for debugging.

---

## Prerequisites

Ensure the following are installed:

* **Python 3 + pip**
* **Google Chrome**
* **Selenium**:

  ```bash
  pip install selenium
  ```
* **ChromeDriver**:

  1. Check Chrome version: `chrome://version/`
  2. Download matching ChromeDriver: [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/)
  3. Extract and add `chromedriver` to your system's PATH.

---

## Usage

1. **Save Script**: Save the script as `frill_voter.py`.
2. **Edit Config**:

   * `FRIL_CO_URL`: Replace with the full URL of the Frill.co feature.
   * `NUMBER_OF_VOTES`: Set desired vote count, don't set this to 30+ votes in a few minutes, system might automatically disable voting.
   * `VOTE_BUTTON_SELECTOR`: Defaults to `button[aria-label='Vote for this Idea']`.
   * *(Optional)* Uncomment these lines for headless mode:

     ```python
     chrome_options.add_argument("--headless")
     chrome_options.add_argument("--disable-gpu")
     ```
3. **Run**:

   ```bash
   python frill_voter.py
   ```

---

## Troubleshooting

* **chromedriver not found**:

  > Ensure it's in a directory listed in your system PATH and is executable.

---

## Disclaimer

This script is **for educational/testing purposes only**. Use it **only on pages you own or have permission to test**.

* Provided "as is" with no warranties.
* The author is not responsible for misuse or damages.
* Do not violate Frill.co’s Terms of Service.

By using this script, you agree to take full responsibility for its use.

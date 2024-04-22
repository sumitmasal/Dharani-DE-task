# Dharani Survey Number Scraper

This Python script is designed to retrieve survey numbers from the Dharani website (https://dharani.telangana.gov.in/knowLandStatus) for a given district, mandal, and village combination.

## Prerequisites

To run this script, you need to have the following installed:

- Python 3.x
- `requests` library (install using `pip install requests`)
- `beautifulsoup4` library (install using `pip install beautifulsoup4`)

## Usage

1. Save the provided code in a Python file (e.g., `scraper.py`).
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the script using the following command: python3 scraper.py
4. When prompted, enter the names of the district, mandal, and village for which you want to retrieve the survey numbers.

Your District Name: Hyderabad
Your Mandal Name: Secunderabad
Your Village Name: Tarnaka

5. The script will attempt to retrieve the survey numbers for the specified district, mandal, and village combination and print them to the console.

## How it Works

1. The script imports the necessary libraries (`requests` and `beautifulsoup4`).
2. The `get_survey_numbers` function is defined, which takes the district, mandal, and village names as input.
3. The function makes a GET request to the Dharani website using the `requests` library.
4. The HTML content of the website is parsed using `BeautifulSoup`.
5. The HTML elements representing the drop-down menus for district, mandal, and village are located.
6. **Note:** Currently, the script does not simulate user interactions to select the desired values from the drop-down menus. This functionality needs to be implemented using a tool like `Selenium` or by interacting with the website's JavaScript.
7. The script attempts to extract the survey numbers from the HTML by searching for `<td>` elements with the class `"survey_no"`.
8. The extracted survey numbers are returned as a list.
9. In the `__main__` block, the script prompts the user to enter the district, mandal, and village names, calls the `get_survey_numbers` function, and prints the retrieved survey numbers (if any).

## Limitations and Future Improvements

- The script currently does not simulate user interactions to select the desired district, mandal, and village from the drop-down menus. This functionality needs to be implemented using a tool like `Selenium` or by interacting with the website's JavaScript.
- The script assumes that the survey numbers are displayed in `<td>` elements with the class `"survey_no"`. If the website's HTML structure changes, the code will need to be updated accordingly.
- Error handling and input validation could be improved to handle unexpected scenarios and user input gracefully.
- The script could be extended to support additional features like pagination, if the website displays survey numbers across multiple pages.

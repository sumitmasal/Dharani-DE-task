import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    # Base URL of the website
    base_url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Make a GET request to the website
    response = requests.get(base_url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the HTML elements representing the drop-down menus
    district_dropdown = soup.find("select", {"id": "district_id"})
    mandal_dropdown = soup.find("select", {"id": "mandal_id"})
    village_dropdown = soup.find("select", {"id": "village_id"})

    # Simulate user interactions (selecting values from the drop-down menus)
    # You'll need to use BeautifulSoup or Selenium to interact with the website
    # and select the desired district, mandal, and village

    # Step 5: Extract the survey numbers from the resulting HTML
    survey_numbers = soup.find_all("td", {"class": "survey_no"})
    survey_numbers = [number.text for number in survey_numbers]

    return survey_numbers

if __name__ == "__main__":
    # Example usage
    district = "Hyderabad"
    mandal = "Secunderabad"
    village = "Tarnaka"

    survey_numbers = get_survey_numbers(district, mandal, village)

    if survey_numbers:
        print(f"Survey numbers for {district}, {mandal}, {village}:")
        for number in survey_numbers:
            print(number)
    else:
        print("No survey numbers found for the given parameters.")

import requests


def main():
  # Ask the user for their zip code or city
  location = input("Please enter your zip code or city: ")

  # Use the zip code or city name to obtain weather forecast data from openweathermap.org
  try:
    api_key = "2704132183eea88753319c6db2c74014"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)

    # Validate whether the user entered valid data
    if response.status_code != 200:
      print("Invalid location. Please try again.")
      return

    # Display the weather forecast in a readable format to the user
    data = response.json()
    print("Weather forecast for", data["name"] + ":")
    print("Temperature:", data["main"]["temp"], "degrees Fahrenheit")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Description:", data["weather"][0]["description"])

  except requests.exceptions.RequestException as e:
    # Print a message to the user indicating whether or not the connection was successful
    print("Error: Unable to establish connection to the webservice.")


if __name__ == "__main__":
  while True:
    main()
    # Allow the user to run the program multiple times
    run_again = input("Do you want to run the program again? (y/n) ")
    if run_again.lower() != "y":
      break

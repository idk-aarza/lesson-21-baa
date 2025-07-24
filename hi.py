import requests

url = "https://uselessfacts.jsph.pl/category/Science.json?language=en"

def get_random_science_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact")
while True:
    user_input = input("Press Enter to get a random science fact or type 'q' to quit... ")
    
    if user_input.lower() == 'q':
        break
    get_random_science_fact()
# Requesting API Data
# - API (Application Programming Interface): A set of rules allowing different software applications to communicate.
# - REST API: An API that uses HTTP requests to fetch or modify data (GET, POST, PUT, DELETE).
# - requests module: The most popular 3rd-party library for making HTTP requests in Python. 
#   * NOTE: You may need to run 'pip install requests' in your terminal if it's not installed.
# - JSON (JavaScript Object Notation): The standard lightweight data-interchange format returned by most APIs.

import requests 
import time

print("--- 🌐 Requesting API Data in Python 🌐 ---")

# Let's use a free, public API called PokeAPI to get Pokemon data
base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(pokemon_name):
    # Construct the full URL
    url = f"{base_url}{pokemon_name.lower()}"
    
    print(f"\n📡 Fetching data from: {url}...")
    start_time = time.time()
    
    # 1. Make the GET request to the API
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: {e}")
        return

    # 2. Check the HTTP Status Code
    # 200 = OK, 404 = Not Found, 500 = Server Error
    if response.status_code == 200:
        print("✅ Success! Data retrieved.")
        
        # 3. Parse the JSON response directly into a Python dictionary
        pokemon_data = response.json() 
        
        # 4. Extract specific key-value pairs from the dictionary
        name = pokemon_data.get("name", "").capitalize()
        pokemon_id = pokemon_data.get("id", "Unknown")
        height = pokemon_data.get("height", 0)
        weight = pokemon_data.get("weight", 0)
        
        # Extracting first type from the nested list of dictionaries
        types = [t["type"]["name"] for t in pokemon_data.get("types", [])]
        type_str = ", ".join(types).title()
        
        print("\n--- 📊 Pokemon Stats 📊 ---")
        print(f"Name:   {name}")
        print(f"ID:     #{pokemon_id}")
        print(f"Type:   {type_str}")
        print(f"Height: {height} decimetres")
        print(f"Weight: {weight} hectograms")
        
    elif response.status_code == 404:
        print(f"❌ Error 404: Pokemon '{pokemon_name}' not found!")
    else:
        print(f"⚠️ Unexpected Error: HTTP Status {response.status_code}")
        
    end_time = time.time()
    print(f"⏱️ Request completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    print("\n--- 1. Valid API Request ---")
    get_pokemon_info("pikachu")

    print("\n--- 2. Invalid API Request (404 Not Found) ---")
    # Agumon is a Digimon, not a Pokemon!
    get_pokemon_info("agumon") 

# --- ⏱️ Time Complexities (Average Case) ---
# requests.get(url) - O(N) Time - Bounded by network latency (N). Extremely slow compared to local operations.
# response.json()   - O(M) Time - Where M is the character length of the JSON response payload.

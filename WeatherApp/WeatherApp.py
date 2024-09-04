import requests
import json
import win32com.client

# Weather API Key (replace with your own key)
weather_api_key = "b13989793f184149a91141538230103"

# Get city name from user
city = input("Enter the name of city\n") 

# Construct API URL
url = f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"

# Send GET request to API
r = requests.get(url)

# Check if request was successful
if r.status_code == 200:
    # Load JSON response into a dictionary
    wdict = json.loads(r.text)  # Note: it's json.loads(), not json.lodes()

    # Print current temperature in Celsius
    temp = wdict['current']['temp_c']
    print(f"Current temperature in {city}: {temp}°C")

    # Create a speech object
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    # Set speech voice (optional)
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.Id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0":
            speaker.Voice = voice
            break

    # Set speech rate (optional)
    speaker.Rate = 1  # Normal speech rate

    # Speak the temperature
    speaker.Speak(f"Current temperature in {city} is {temp} degrees Celsius")
else:
    print(f"Failed to retrieve weather data. Status code: {r.status_code}")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    # Set speech voice (optional)
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.Id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0":
            speaker.Voice = voice
            break

    speaker.Speak(f"Failed to retrieve weather data for {city}. Please try again later.")
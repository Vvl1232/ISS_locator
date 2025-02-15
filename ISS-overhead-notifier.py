import requests as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def is_iss_overhead(latitude, longitude, user_lat, user_lon):
    """Check if the ISS is overhead within a certain range"""
    return abs(latitude - user_lat) < 5 and abs(longitude - user_lon) < 5

def send_email(subject, body, to_email, from_email, from_password):
    """Send an email notification"""
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)
    server.quit()

# Your location
user_lat = 18.5562  # Your latitude
user_lon = 73.8456  # Your longitude

# Email details
to_email = "limkarvinitpro@gmail.com"
from_email = "limkarvinit@gmail.com"
from_password = "gyml zwnc rpxn dowz"

while True:
    # Fetch the current location of the ISS
    response = r.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Use OpenCage Geocoding API to get the address
    geocode_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": f"{iss_latitude},{iss_longitude}",
        "key": "ecaf71abcaa4417d9388b2e8f58161a4"  # Replace with your actual API key
    }
    geocode_response = r.get(geocode_url, params=params)
    geocode_response.raise_for_status()
    geocode_data = geocode_response.json()

    # Extract the formatted address
    formatted_address = geocode_data["results"][0]["formatted"]

    print(f"Longitude: {iss_longitude}, Latitude: {iss_latitude}")
    print(f"Address: {formatted_address}")

    # Check if the ISS is overhead
    if is_iss_overhead(iss_latitude, iss_longitude, user_lat, user_lon):
        subject = "ISS Overhead Alert"
        body = f"The ISS is currently overhead at Longitude: {iss_longitude}, Latitude: {iss_latitude}."
        send_email(subject, body, to_email, from_email, from_password)
        print("Email sent!")

    # Check every 60 seconds
    time.sleep(5)
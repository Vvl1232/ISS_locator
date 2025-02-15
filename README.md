# ISS Overhead Notification System

In the past two days, I created a Python script that checks if the International Space Station (ISS) is overhead and sends an email notification.

📚 Libraries Used:
requests
smtplib
email.mime.multipart
email.mime.text
time

🌐 Features:
Fetches real-time ISS location using the Open Notify API.
Uses OpenCage Geocoding API to convert ISS coordinates to a human-readable address.
Sends email alerts when the ISS is overhead at my location.

🛠 Deployment: I deployed the script on AWS Lambda and set up AWS CloudWatch to run the function every 1 minute. This allows for continuous monitoring and automated email alerts.

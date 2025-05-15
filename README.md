# ISS Tracker Notifier 🚀

This Python script notifies you via email when the International Space Station (ISS) is flying over your location **at night** so you can go outside and see it.

## 🔧 Features

- Checks real-time ISS position using a public API
- Detects if it's currently dark at your location
- Sends an email alert if the ISS is nearby and visible
- Runs in the background and checks every 60 seconds

## 💡 Skills Used

- Python Programming
- Working with APIs (`requests`)
- Email Automation using `smtplib`
- Environment Variables with `dotenv`
- Time & Scheduling in Python
- Error handling and condition-based logic
- Git & GitHub for version control
- Real-time background task execution

## 📦 Requirements

- Python 3
- `requests`
- `python-dotenv`

Install required libraries:

```bash
pip install requests python-dotenv
```

### 🛠️ Setup

1. Clone the repo
```bash
git clone https://github.com/yourusername/iss-tracker-notifier.git
cd iss-tracker-notifier
```
2. Create a .env file in the project directory and add your info:
```env
EMAIL=youremail@gmail.com
APP_PASSWORD=your_gmail_app_password
LATITUDE=Your_Latitude
LONGITUDE=Your_Longitude
```
**🔒 Make sure your .env file is listed in .gitignore so you don't expose your credentials.**

3. Run the script
```bash
python3 main.py
```
## 📬 Email Notes
- You need to use an App Password if you're using Gmail with 2-step verification.
- Learn how to generate an App Password.

## 🛰 Example Output
```txt
International Space Station is here
Look Up!
```

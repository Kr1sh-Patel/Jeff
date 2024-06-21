# Jeff Personal Project

This project is a Python virtual assistant named Jeff, designed to perform basic tasks through voice commands.

## Features

* Text-to-Speech: Jeff can speak text aloud using the pyttsx3 library.
* Speech Recognition: Jeff can understand spoken commands using the speech_recognition library.
* Wikipedia Search: Jeff can access and summarize information from Wikipedia.
* Web Browsing: Jeff can open web browsers like YouTube, Google, and Stack Overflow.
* Time Announcement: Jeff can tell you the current time.
* VS Code Launch: Jeff can launch the Visual Studio Code IDE for you.
* Email Sending: Jeff can send emails using SMTP (Note: Security considerations are mentioned later).

## Requirements

* Python 3 (https://www.python.org/downloads/)
* `pyttsx3` library (installation: pip install pyttsx3)
* `speech_recognition` library (installation: pip install speech_recognition)
* `wikipedia` library (installation: pip install wikipedia)
* `webbrowser` library (included in the standard Python library)
* `os` library (included in the standard Python library)
* `smtplib` library (included in the standard Python library)

## Installation

1. Install the required libraries as mentioned above.
2. Copy the `jeff_pp_project.spec` and `jeff.py` files into your desired project directory.
3. Run the script using `python jeff.py`.

## Usage

* Jeff will greet you and ask how he can help.
* Speak your commands clearly for Jeff to understand.
* Here are some examples of commands you can use:
  * "Wikipedia search for [topic]"
  * "Open YouTube"
  * "Open Google"
  * "Open Stack Overflow"
  * "What time is it?"
  * "Open code" (to launch VS Code)
  * "Email to me" (Jeff will prompt you for the content and send it to the specified address)
  * "Exit" (to quit Jeff)

## Security Considerations for Email Sending

## Caution 
This code uses your Gmail credentials directly in the script. This is a security risk, as anyone with access to the script can potentially send emails from your account. For production use, consider:

* Using a secure email library that supports authentication methods like OAuth2.
* Storing credentials securely using environment variables or a configuration file.

## Additional Notes

* This is a basic example of a virtual assistant. You can extend its functionality by adding more commands and integrating with other APIs.
* Feel free to modify the code to customize Jeff's behavior to your preferences.

I hope this README.md provides a clear and informative guide to your project!

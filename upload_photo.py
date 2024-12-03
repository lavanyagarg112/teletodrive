from telethon.sync import TelegramClient
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from dotenv import load_dotenv
import shutil

load_dotenv()

env_vars = os.environ

# Telegram API credentials
api_id = env_vars['API_ID']  # Replace YOUR_API_ID with the actual API ID
api_hash = env_vars['API_HASH']  # Replace YOUR_API_HASH with the actual API Hash

# Initialize Telegram client
client = TelegramClient('session2_photos', api_id, api_hash)

# Google Drive authentication
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")  # Load credentials from a file
    if gauth.credentials is None:
        # Authenticate if credentials are not present
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh the credentials if expired
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")  # Save credentials for future use
    return GoogleDrive(gauth)

drive = authenticate_google_drive()

# Google Drive folder ID (Replace with your specific folder ID)
FOLDER_ID = env_vars['FOLDER_ID_PHOTOS']  # Replace with the Google Drive folder ID

# Function to upload a file to a specific folder in Google Drive
def upload_to_drive(file_path):
    if file_path:
        file_name = os.path.basename(file_path)
        gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': FOLDER_ID}]})
        gfile.SetContentFile(file_path)
        gfile.Upload()
        print(f"Uploaded {file_name} to Google Drive folder ID: {FOLDER_ID}")

# Function to download and upload photos with pagination
def download_and_upload_photos():
    with client:
        # Replace 'YourChatName' with the actual Telegram chat or channel name
        chat_name = int(env_vars['CHAT_NAME'])
        topic_id = int(env_vars['TOPIC_ID'])
        total_messages = 0
        offset_id = 0

        while True:
            # Fetch messages in batches of 10,000
            messages = client.get_messages(chat_name, limit=10000, offset_id=offset_id, reply_to=topic_id)

            if not messages:
                break  # No more messages to fetch

            for message in messages:
                if message.photo:
                    # Download the photo to a local 'downloads' folder
                    file_path = message.download_media(file="./downloads/")
                    print(f"Downloaded: {file_path}")

                    # Upload the photo to Google Drive
                    upload_to_drive(file_path)

            # Update offset_id to the last message ID
            offset_id = messages[-1].id
            total_messages += len(messages)

            print(f"Fetched {total_messages} messages so far...")

    print(f"Total messages fetched and processed: {total_messages}")

# Main function to execute the script
if __name__ == "__main__":
    # Ensure a 'downloads' directory exists
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    download_and_upload_photos()
    shutil.rmtree("downloads")
    os.remove("mycreds.txt")
    print("Downloads folder and creds file deleted.")

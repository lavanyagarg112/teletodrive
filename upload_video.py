from google.auth.transport.requests import Request
from telethon.sync import TelegramClient
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv
import shutil

load_dotenv()

env_vars = os.environ

# Telegram API credentials
api_id = env_vars['API_ID']  # Replace with your Telegram API ID
api_hash = env_vars['API_HASH']  # Replace with your Telegram API Hash

# Initialize Telegram client
client = TelegramClient('session2_videos', api_id, api_hash)

# Google Drive authentication function using Google API client
def authenticate_google_drive():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    
    # Check if token file exists
    if os.path.exists('mycreds.txt'):
        creds = Credentials.from_authorized_user_file('mycreds.txt', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('mycreds.txt', 'w') as token:
            token.write(creds.to_json())
    
    # Build the Google Drive service
    service = build('drive', 'v3', credentials=creds)
    return service

FOLDER_ID = env_vars['FOLDER_ID_VIDEOS']

# Function to upload videos to a specific folder in Google Drive
def upload_video_to_drive(file_path):
    service = authenticate_google_drive()

    file_metadata = {'name': os.path.basename(file_path), 'parents': [FOLDER_ID]}
    media = MediaFileUpload(file_path, mimetype='video/mp4')

    file = service.files().create(body=file_metadata, media_body=media, fields='id,name').execute()
    print(f'Uploaded video: {file["name"]} with ID: {file["id"]}')

# Function to download and upload only videos
def download_and_upload_videos():
    with client:
        chat_id = int(env_vars['CHAT_NAME'])
        topic_top_msg_id = int(env_vars['TOPIC_ID'])

        total_messages = 0
        offset_id = 0

        while True:
            # Fetch messages from the topic
            messages = client.get_messages(
                chat_id, limit=100, offset_id=offset_id, reply_to=topic_top_msg_id
            )

            if not messages:
                break  # No more messages to fetch

            for message in messages:
                if message.video:  # Check if the message contains a video
                    # Download the video to a local 'downloads' folder
                    file_path = message.download_media(file="./downloads/")
                    print(f"Downloaded: {file_path}")

                    # Upload the video to Google Drive
                    upload_video_to_drive(file_path)

            offset_id = messages[-1].id  # Update offset_id for the next batch
            total_messages += len(messages)
            print(f"Fetched {total_messages} messages so far...")

    print(f"Total messages fetched and processed: {total_messages}")

# Main function to execute the script
if __name__ == "__main__":
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    download_and_upload_videos()
    shutil.rmtree("downloads")
    os.remove("mycreds.txt")
    print("Downloads folder and creds file deleted.")

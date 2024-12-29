# Photo and Video Upload from Telegram to Google Drive

## Description

This Python project allows you to **download photos and videos** from a **Telegram topic from a channel** and **upload them to Google Drive**. The project provides two separate scripts:

- **`upload_photo.py`**: Downloads photos from Telegram and uploads them to a Google Drive folder.
- **`upload_video.py`**: Downloads videos from Telegram and uploads them to a separate Google Drive folder.

## Requirements

- **Python 3.x**
- **Telegram API credentials** (API ID and API Hash)
- **Google Drive API credentials** (OAuth 2.0 client)
- **Environment variables** for secure handling of credentials

### Installation

1. Download the source code zip file under the latest release found [here](https://github.com/lavanyagarg112/teletodrive/releases).
2. Unzip the file
3. Open the folder in the terminal.
4. Next, follow the steps below.

### Required Python Libraries

To install the required libraries, you will need to first create a virtual environment and then install the dependencies from the `requirements.txt` file.

1. **Create a virtual environment:**

   In your project directory, run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   - **For Windows (Command Prompt):**
     ```bash
     venv\Scripts\activate
     ```

   - **For macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**

   Once the virtual environment is activated, run:

   ```bash
   pip install -r requirements.txt
   ```

## Setup Instructions

### 1. **Telegram API Credentials**

To interact with Telegram, you need to obtain your **API ID** and **API Hash**.

1. Go to [Telegram Developer Tools](https://my.telegram.org/auth) and log in with your Telegram account.
2. Create a new application to get your **API ID** and **API Hash**.

### 2. **Google Drive API Credentials**

Follow these steps to obtain Google Drive credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Navigate to **APIs & Services > Library** and enable the **Google Drive API**.
4. Go to **APIs & Services > Credentials**, click **Create Credentials**, and choose **OAuth 2.0 Client IDs**.
5. Download the **`client_secrets.json`** file and place it in your project directory.
6. Important: Save the file with the exact name **`client_secrets.json`**


### 3. **Get `chat_id` and `topic_id` for Telegram**

To download media from a Telegram chat/channel, you will need the `chat_id` and `topic_id`. Here's how to get them:

1. Go to [telegram web](https://web.telegram.org)
2. Open the channel and topic you wish to access
3. In the url, the last part has the format `/#<Chat ID>_<Topic ID>`
4. Thus, you have now obtained your `Chat ID` and `Topic ID`

There are other ways to access your chat id and topic id. I will be putting them here soon.

### 4. **Set Up Environment Variables**

Create a `.env` file in your project directory and add the following environment variables:

```env
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
FOLDER_ID_PHOTOS=your_google_drive_photos_folder_id
FOLDER_ID_VIDEOS=your_google_drive_videos_folder_id
CHAT_NAME=your_telegram_chat_name_or_id
TOPIC_ID=your_telegram_topic_id
START_DATE=start_date_to_filter_your_photos_and_videos
END_DATE=end_date_to_filter_your_photos_and_videos
TIMEZONE=your_timezone_as_per_standard_notation
```

Replace the placeholders with your actual credentials and folder information:

- **API_ID**: Your Telegram API ID.
- **API_HASH**: Your Telegram API Hash.
- **FOLDER_ID_PHOTOS**: Google Drive folder ID where photos will be uploaded.
- **FOLDER_ID_VIDEOS**: Google Drive folder ID where videos will be uploaded.
- **CHAT_NAME**: The name or ID of the Telegram chat/channel from which you are downloading media.
- **TOPIC_ID**: The topic ID in the Telegram chat/channel.
- **START_DATE**: The start date from when you want the photos/videos to be taken.
- **END_DATE**: The end date until when you want the photos/videos to be taken.
- **TIMEZONE**: Your current timezone to ensure that the start and end dates are accurate. (eg: Asia/Singapore. It will default to UTC if wrong format or not provided)

---

## Usage

### 1. **Upload Photos** (`upload_photo.py`)

Once you’ve set up the environment, run the `upload_photo.py` script to download and upload photos from Telegram to Google Drive:

```bash
python upload_photo.py
```

The script will:

- Authenticate your google drive
- Authenticate telegram if not already authenticated
- Download photos from the specified Telegram chat/channel.
- Upload them to the Google Drive folder specified by `FOLDER_ID_PHOTOS`.

### 2. **Upload Videos** (`upload_video.py`)

To upload videos, use the `upload_video.py` script:

```bash
python upload_video.py
```

The script will:

- Authenticate your google drive
- Authenticate telegram if not already authenticated
- Download videos from the specified Telegram chat/channel.
- Upload them to the Google Drive folder specified by `FOLDER_ID_VIDEOS`.

---

## Basic File Structure

```
photo-video-upload-project/
│
├── .env                # Environment variables
├── client_secrets.json # Google OAuth 2.0 credentials
├── upload_photo.py     # Script to download and upload photos
├── upload_video.py     # Script to download and upload videos
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

More files such as credential files, download files or session files will be created as you work.

---

## Coming soon

1. download photos/videos from chats
2. download photos/videos from entire channel

If you are familiar with python/coding, you can do the above yourself by:
- remove the `reply_to=` parameter from `client.get_messages`
- set the `chat_name` env to be the individual chat id or channel id instead. topic id will not be used.

---

## License

This project is **not open source** and is intended for **personal or internal use only**. Redistribution and modification of the code are not permitted without prior written consent from the author.

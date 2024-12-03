# Photo and Video Upload from Telegram to Google Drive

## Description

This Python project allows you to **download photos and videos** from a **Telegram chat/channel** and **upload them to Google Drive**. The project provides two separate scripts:

- **`upload_photo.py`**: Downloads photos from Telegram and uploads them to a Google Drive folder.
- **`upload_video.py`**: Downloads videos from Telegram and uploads them to a separate Google Drive folder.

## Requirements

- **Python 3.x**
- **Telegram API credentials** (API ID and API Hash)
- **Google Drive API credentials** (OAuth 2.0 client)
- **Environment variables** for secure handling of credentials

### Required Python Libraries

To install the required libraries, you will need to first create a virtual environment and then install the dependencies from the `requirements.txt` file.

1. **Create a virtual environment:**

   In your project directory, run the following command to create a virtual environment (you can replace `venv` with any name you prefer):

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

### 3. **Set Up Environment Variables**

Create a `.env` file in your project directory and add the following environment variables:

```env
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
FOLDER_ID_PHOTOS=your_google_drive_photos_folder_id
FOLDER_ID_VIDEOS=your_google_drive_videos_folder_id
CHAT_NAME=your_telegram_chat_name_or_id
TOPIC_ID=your_telegram_topic_id
```

Replace the placeholders with your actual credentials and folder information:

- **API_ID**: Your Telegram API ID.
- **API_HASH**: Your Telegram API Hash.
- **FOLDER_ID_PHOTOS**: Google Drive folder ID where photos will be uploaded.
- **FOLDER_ID_VIDEOS**: Google Drive folder ID where videos will be uploaded.
- **CHAT_NAME**: The name or ID of the Telegram chat/channel from which you are downloading media.
- **TOPIC_ID**: The topic ID in the Telegram chat/channel.

---

## Usage

### 1. **Upload Photos** (`upload_photo.py`)

Once you’ve set up the environment, run the `upload_photo.py` script to download and upload photos from Telegram to Google Drive:

```bash
python upload_photo.py
```

The script will:

- Download photos from the specified Telegram chat/channel.
- Upload them to the Google Drive folder specified by `FOLDER_ID_PHOTOS`.

### 2. **Upload Videos** (`upload_video.py`)

To upload videos, use the `upload_video.py` script:

```bash
python upload_video.py
```

The script will:

- Download videos from the specified Telegram chat/channel.
- Upload them to the Google Drive folder specified by `FOLDER_ID_VIDEOS`.

---

## File Structure

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

---
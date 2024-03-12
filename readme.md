# Flask Message Project

This project is a web application developed with Flask that allows sending messages to Discord and Telegram channels using their respective APIs. The application is designed to receive HTTP requests and send messages to the specified channels in the request body.

## Configuration

Before running the application, make sure to set the following environment variables:

- `PORT`: The port on which the Flask server will run.
- `DISCORD_CHANNEL_ID`: The ID of the Discord channel to which messages will be sent.
- `DISCORD_TOKEN`: The authentication token of the Discord bot.
- `TELEGRAM_CHANNEL_ID`: The ID of the Telegram channel to which messages will be sent.
- `TELEGRAM_TOKEN`: The authentication token of the Telegram bot.

## Installation

1. Clone the project repository:

   ```bash
   git clone https://github.com/your_username/repository_name.git

2. Navigate to the project directory:

    ```bash
    cd repository_name

3. Install virtual environment:

    ```bash
    pip install virtualenv venv

4. Activate virtual environment:

    ```bash
    .\venv\Scripts\activate

5. Install the necessary dependencies:

    ```bash 
    pip install -r requirements.txt

## Local Execution

- python main.py
- The application will run on the specified port or on the default port 8000 if none is provided.


## Usage

### Send Messages to Discord

- **URL:** `/messages/send-discord`
- **HTTP Method:** `POST`
- **Request Body:** It should be a JSON object with the following structure:

  ```json
  {
    "content": "Content of the message to send to Discord"
  }


  ### Send Messages to Telegram

- **URL:** `/messages/send-telegram`
- **HTTP Method:** `POST`
- **Request Body:** It should be a JSON object with the following structure:

  ```json
  {
    "message": "Content of the message to send to Telegram"
  }

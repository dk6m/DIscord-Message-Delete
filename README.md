# Discord Message Deleter

This Python script is used to bulk delete a specific user's messages on Discord. The user can run this script by providing their Discord **token** and then delete their messages from a specific channel or server (guild).

## Features:
- The user logs in with their Discord token and the script automatically retrieves their user ID.
- Messages from a specific channel or server can be deleted based on the provided channel or server ID.
- After the deletion process, the user is given the option to either finish the process or delete messages from another channel.
- The user can delete messages from multiple channels or servers, and when the process is complete, they are informed about it.

## Requirements:
- Python 3.x
- `requests` module (for interacting with the Discord API)

## Installation:

1. **Ensure Python and the required module are installed**:
    - Download Python 3.x from [here](https://www.python.org/downloads/).
    - To install the required module, use the following command in your terminal or command prompt:
    ```bash
    pip install requests
    ```

2. **Download the script**:
    - Download or clone this repository to your local machine.

3. **Obtain Your Token**:
    - You will need a Discord bot token or a user token. You can refer to online guides on how to obtain a token.

4. **Run the Script**:
    - Run `main.py` using the following command:
    ```bash
    python main.py
    ```

5. **Enter Your Token and Other Details**:
    - Once the script starts, you will be prompted to enter your Discord token.
    - Then, you will need to choose whether to delete messages from DM or Server.
    - You will be asked to provide the channel ID or server ID, and the script will begin deleting messages.

6. **After Completion, Choose an Option**:
    - Once the deletion process is complete, you will be given the option to either:
      - Press `Enter` to finish the process, or
      - Press `1` to delete messages from another channel/server.

## Usage:

1. **Enter Token**: Provide your Discord bot or user token.
2. **Choose Mode**: Select `[1] DM` or `[2] Server`.
3. **Enter Channel ID or Server ID**: Provide the appropriate ID to delete messages from the selected channel or server.
4. **Delete Messages**: The script will start deleting messages from the specified location.
5. **Process Options**: After the process is complete, you will be asked if you want to delete messages from another channel or finish the process.


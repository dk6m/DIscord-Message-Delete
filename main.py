import requests, time


TOKEN = input("Token: ")


headers = {'Authorization': TOKEN}
user_info = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
if user_info.status_code == 200:
    uid = user_info.json()['id']
    print(f"User ID obtained: {uid}")
else:
    print("Failed to retrieve user ID. Make sure your token is valid.")
    exit()


mode = input('[1] DM\n[2] Server\n')

class Deleter:
    def something(self, stuff):
        messages = []
        for block in stuff:
            for message in block:
                if message['author']['id'] == uid:
                    messages.append('%s:%s' % (message['channel_id'], message['id']))
        self.something_else(messages)

    def something_else(self, messages):
        if len(messages) == 0:
            print("Successfully deleted all messages.")
        else:
            print(f'Deleting {len(messages)} messages.')
            for message in messages:
                channel = message.split(':')[0]
                message_id = message.split(':')[-1]
                r = requests.delete(f'https://discordapp.com/api/v6/channels/{channel}/messages/{message_id}', headers=headers)
                time.sleep(0.2)

obj = Deleter()

def delete_messages():
    if mode == '1':
        channel_id = input('Channel ID: ')
        while True:
            r = requests.get(f'https://discordapp.com/api/v6/channels/{channel_id}/messages/search?author_id={uid}', headers=headers)
            try:
                messages = r.json()['messages']
                obj.something(messages)
                if not messages:
                    break 
            except KeyError:
                print(f"Error: 'messages' not found in response. Full response: {r.json()}")
                break
    else:
        server = input('Server ID: ')
        while True:
            r = requests.get(f'https://discordapp.com/api/v6/guilds/{server}/messages/search?author_id={uid}&include_nsfw=true', headers=headers)
            try:
                messages = r.json()['messages']
                obj.something(messages)
                if not messages:
                    break  
            except KeyError:
                print(f"Error: 'messages' not found in response. Full response: {r.json()}")
                break

while True:
    delete_messages()

    user_choice = input("\nPress Enter to finish or '1' to delete messages from another channel: ").strip()
    if user_choice != '1':
        print("Process finished.")
        break  
    else:
        mode = input('[1] DM\n[2] Server\n') 

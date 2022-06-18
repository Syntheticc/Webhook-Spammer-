from dhooks import webhook
import time

print("""
███████ ██    ██ ███    ██ ███████ ██████   █████  ███    ███ 
██       ██  ██  ████   ██ ██      ██   ██ ██   ██ ████  ████ 
███████   ████   ██ ██  ██ ███████ ██████  ███████ ██ ████ ██ 
     ██    ██    ██  ██ ██      ██ ██      ██   ██ ██  ██  ██ 
███████    ██    ██   ████ ███████ ██      ██   ██ ██      ██ 
            Devved By ryang#1337 discord.gg/generate 
""")

message = input("Message to spam: ")
webhookurl = webhook(input("enter webhook url: "))
delay = int(input("enter delay: "))

while true:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent!")
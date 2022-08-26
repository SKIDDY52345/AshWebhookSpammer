from optparse import Option
import os
import requests
from colorama import Fore

os.system("title AshWebhookSpammer")
os.system("cls")

print(Fore.CYAN + ''' █████╗ ███████╗██╗  ██╗    ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔══██╗██╔════╝██║  ██║    ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████║███████╗███████║    ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██╔══██║╚════██║██╔══██║    ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║  ██║███████║██║  ██║    ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ 
------------------------------------------------------------------------------------------------------------------------------------------------------------''')
print(Fore.CYAN + "[1] Webhook Spammer | [2] Webhook Deleter")
option = input(Fore.CYAN + "\nOption >> ")

if option=="1":
    webhookUrl1 = input("Enter Your Webhook: ")
    message = input("Enter Your Message: ")
    payload = {
        'content': message,
        'username': "Ash Webhook Spammer",
        'avatar_url': "https://cdn.discordapp.com/attachments/960610436741492780/1010563618569457664/servericon2.0.gif"
    }
    while True:
        r = requests.post(webhookUrl1, json=payload)
        print(Fore.GREEN + f'{r}')
        
elif option=="2":
    webhookUrl2 = input("Enter Your Webhook: ")
    r = requests.delete(webhookUrl2)


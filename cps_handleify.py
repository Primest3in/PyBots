import responses
import discord
import methods
import json
from discord.utils import get


s = "https://codeforces.com/profile/"

async def send_message(message, user_message):
    try :
        res = responses.handle_response(user_message)
        await message.channel.send(res)
    except Exception as e:
        print(e)






def run_discord_bot():
    token = ''
    client = discord.Client(intents=discord.Intents.all())
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        channel = str(message.channel)
        user_message = str(message.content)
        a = ""
        ok = 1
        for i in range(0, len(user_message)):
            if(user_message[i] == '?'):
                for j in range(0, i):
                    a += user_message[j]
                    ok = 0
                break
        if(not ok):
            user_message = a   


        front_url, handle = methods.parse(user_message)

        print(f"{username} said in chanel '{channel}': {handle} ")
        
        if((not len(handle)) or front_url != s):
            await   message.channel.send("Error! Please follow this format **https://codeforces.com/profile/Primest3in** and try again.")
        else :  
            rank = methods.getRole(handle)
            role = get(message.author.guild.roles, name = rank) 
            await message.author.add_roles(role) 
            await message.channel.send(f'**{rank}** role given to user **{username}**')
    client.run(token)
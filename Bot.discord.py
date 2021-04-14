import discord 
#id = 787691717717262406

def read token ():
    with open ("tokent.txt", "r") as f:
        lines = f.readlines()
        return line [0].strip()

token = read token ()

client = discord.client



@client.event
async def on_message (message):
        id = client.get_guild(787691717717262406)

        if message.content.find("!!price")!= -1:
            await message.channel.send("20€") # if the user says !!price we will send back 20€
        elif message.content == "!!user":
            await message.channel.send(f"""# of Members{id.member_count}""")

client.run(token)
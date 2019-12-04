import discord
import json
import time


target_channel = 651552578223734795


def todays_birthdays():

    today = time.strftime("%m").zfill(2) + time.strftime("%d").zfill(2)

    f = [x.strip() for x in open("data/birthdays.txt", encoding="utf-8").readlines()]

    f = f[f.index("<start " + today + ">") + 1:]

    f = f[:f.index("<end>")]

    f.pop(0)

    h = []

    for i in range(0, len(f)//2, 2):

        h.append(f[i] + " - " + f[i+1])

    return h




class SimpleClient(discord.Client):

    async def on_ready(self):
        print("uuauwelfk")

        channel = self.get_channel(651552578223734795)

        await channel.send("Happy birthday to:")

        for i in todays_birthdays():

            await channel.send(i)

        quit(21)


with open('data\\config.json') as json_data_file:
    data = json.load(json_data_file)
    token = data['discord']['token']

a = SimpleClient()
a.run(token)
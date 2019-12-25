import discord
import json
import time
import os


def today():
    return time.strftime("%m").zfill(2) + time.strftime("%d").zfill(2)


def birthdays(date):

    base_data = [x.strip() for x in open("data/birthdays.txt", encoding="utf-8").readlines()]

    base_data = base_data[base_data.index("<start " + date + ">") + 2:]
    base_data = base_data[:base_data.index("<end>")]

    return [base_data[i] + " - " + base_data[i+1] for i in range(0, len(base_data), 2)]


class SimpleClient(discord.Client):

    async def on_ready(self):
        print("Daily Update Initialization")

        channel = self.get_channel(target_channel)

        await channel.send("Happy birthday to:")
        for i in birthdays(today()):
            await channel.send("-- " + i)

        quit(21)


with open('data/config.json') as json_data_file:
    data = json.load(json_data_file)
    token = data['discord']['token']

target_channel = data['channels']['birthday']

a = SimpleClient()
a.run(token)

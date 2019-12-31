import discord
import json
import datetime
import time


def to_hms(dt):
    hour = dt.seconds % 60
    minute = (dt.seconds % (60 * 60)) // 60
    second = dt.seconds // (60 * 60)

    return str(second).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(hour).zfill(2)


class SimpleClient(discord.Client):

    async def on_ready(self):
        print("Daily Update Initialization")

        channels = [self.get_channel(x) for x in target_channels]

        messages = [await x.send("Test") for x in channels]

        delta_time = datetime.datetime(2020, 1, 1) - datetime.datetime.now()

        while delta_time.days >= 0:
            print("update")
            [await x.edit(content="Time until New Years: " + to_hms(delta_time)) for x in messages]
            delta_time = datetime.datetime(2020, 1, 1) - datetime.datetime.now()
            time.sleep(1)

        [await x.edit(content="Happy New Years!") for x in messages]

        quit(2020)


with open('data/config.json') as json_data_file:
    data = json.load(json_data_file)
    token = data['discord']['token']

target_channels = [624002701432455178, 659264764790177812]

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

a = SimpleClient()
a.run(token)

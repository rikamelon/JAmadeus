import discord
from src import Commands, Substitutions
import asyncio


class Client(discord.Client):

    stack = True
    substitutions = []

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        Commands.create_r_bot()
        print('Created Reddit bot!')
        Commands.create_r34_bot(asyncio.get_running_loop())
        print('Created r34 bot')
        self.update_subs()
        print('Retrieved substitutions')

    async def on_message(self, message):
        if message.author.name != "Amadeus":
            await Commands.handle_message(message, self)

    def update_subs(self):
        self.substitutions = []
        self.substitutions.extend(Substitutions.stands())
        self.substitutions.extend(Substitutions.stand())
        self.substitutions.extend(Substitutions.nicu())
        self.substitutions.extend(Substitutions.im_x())
        self.substitutions.extend(Substitutions.shoot_me())
        self.substitutions.extend(Substitutions.kill_me())
        self.substitutions.extend(Substitutions.stab_me())
        self.substitutions.extend(Substitutions.nullpo())
        self.substitutions.extend(Substitutions.cyanide())
        self.substitutions.extend(Substitutions.thanks_bot())

    async def send(self, message, channel, file=None, filename=None, embed=None):

        if embed:
            return await channel.send(message, embed=embed)
        if file:
            return await channel.send(message, file=discord.File(file, filename=filename))
        return await channel.send(message)

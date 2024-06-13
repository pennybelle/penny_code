# bot.py
import asyncio
import discord
import re

from discord.ext import commands, tasks

TOKEN = "ODExNzg2MTg3MDU2NDgwMjc2.YC3QzQ.cOLNjcXB6-qpy2AwKmSj5R8S3Lc"

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description='Relatively simple autodelete bot!')


from discord.ext import tasks, commands

class AutoDeleteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean_timer.start()

    @commands.command()
    @commands.has_any_role("ヽ(´ー`)人(´∇｀)人(`Д´)ノ")
    async def kill(self, ctx):
        exit()

    @commands.command()
    @commands.has_any_role("ヽ(´ー`)人(´∇｀)人(`Д´)ノ")
    async def nuke(self, ctx):
        await self._clean(ctx.message.channel, 0, 50000000)

    @commands.command()
    @commands.has_any_role("ヽ(´ー`)人(´∇｀)人(`Д´)ノ")
    async def cut(self, ctx, start_id, stop_id, limit=1000):
        await ctx.message.delete()
        await self._cut(ctx.message.channel, start_id, stop_id, limit=1000)

    async def _cut(self, channel, start_id, stop_id, limit=1000):
        
        if start_id == "*":
            start_id = 0 
            is_deleting = True
        else:
            start_id = int(start_id) #Converting the id to an int
            is_deleting = False

        if stop_id == "*":
            stop_id = 0 
        else:
            stop_id = int(stop_id) #Converting the id to an int
        
        async for msg in channel.history(limit=limit):
            if msg.id == start_id:
                is_deleting = True

            if is_deleting:
                asyncio.create_task(msg.delete())

            if msg.id == stop_id:
                break

    @commands.command()
    @commands.has_any_role("ヽ(´ー`)人(´∇｀)人(`Д´)ノ")
    async def clean(self, ctx, seconds = None, limit = None):
        await ctx.message.delete()
        if seconds == "*":
            await self._clean(ctx.message.channel, 0, 50000000)
        else:
            await self._clean(ctx.message.channel, seconds, limit)

    async def _clean(self, channel, seconds = 600, limit = 1000, delete_before = True):
        limit = int(limit) #Converting the amount of messages to delete to an integer

        time_channel = self.bot.get_channel(809931339087216700)

        if channel is None:
            return

        # Get the current time
        get_current_time_message = await time_channel.send(f"bye bye")
        current_time = get_current_time_message.created_at
        await get_current_time_message.delete() # Delete the message used for current time

        async for msg in channel.history(limit=limit):
            if (current_time-msg.created_at).total_seconds() > seconds:
                await msg.delete()

    def cog_unload(self):
        self.clean_timer.cancel()

    @tasks.loop(minutes=5)
    async def clean_timer(self):
        await self._clean(self.bot.get_channel(811275037326704711), 3600, 1000) #bot-cmds
        await self._clean(self.bot.get_channel(920870500966740069), 3600, 1000) #fishing
        await self._clean(self.bot.get_channel(804787907751182338), 10800, 1000) #radio-transmissions
        await self._clean(self.bot.get_channel(855880520399454218), 300, 1000) #the-void
        await self._clean(self.bot.get_channel(848983285156937779), 2592000, 1000) #frequency-info
        await self._clean(self.bot.get_channel(806648155264385065), 604800, 1000) #testing
        await self._clean(self.bot.get_channel(809931339087216700), 300, 1000) #bots

    @commands.Cog.listener()
    async def on_message(self, message):
        blacklist_word = set([
            "owo",
            "uwu",
            "VQFYLYQHY",
            "vqfylyqhy"
        ])
        blacklist_contains = [
            "o w o"
        ]
        blacklist_regex = [
            "n+\s*g+\s*g+\s*r+$",
            "n+\s*g+\s*r+$",
            "n+\s*i+\s*g+\s*g+\s*r+$",
            "n+\s*g+\s*g+\s*e+\s*r+$",
            "n+\s*i+\s*g+\s*r+$",
            "n+\s*i+\s*g+\s*e+\s*r+$",
            "n+\s*i+\s*g+\s*e+\s*r+\s*s+$",
            "n+\s*i+\s*g+\s*g+\s*e+\s*r",
            "n+\s*i+\s*g+\s*g+\s*e+\s*r",
            "n+\s*i+\s*g+\s*g+\s*a+$",
            "c+\s*h+\s*i+\s*n+\s*k+$",
            "f+\s*a+\s*g+$",
            "f+\s*a+\s*g+\s*s+$",
            "f+\s*a+\s*g+\s*o+$",
            "f+\s*a+\s*g+\s*g+\s*o+$",
            "f+\s*a+\s*g+\s*g+\s*o+\s*t",
            "f+\s*a+\s*g+\s*g+\s*e+\s*t"
        ]
        
        message_words = set(message.content.lower().split())
        message_text = message.content.lower()
        if  len(blacklist_word & message_words) > 0 or any(substring in message_text for substring in blacklist_contains) or any(re.search(cur_regex, message_text) is not None for cur_regex in blacklist_regex):
            print("\nMessage deleted: ", message.content, "\n", message, "\n")
            await message.delete()

@bot.event
async def on_ready():
    print(f'{bot.user} [{bot.user.id}] is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'\t- {guild.name}(id: {guild.id})')

bot.add_cog(AutoDeleteCog(bot))

bot.run(TOKEN)




import settings
import discord 
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        
    @bot.command(
        aliases=['p'],
        help="Call and Response",
        description="Answers with pong",
        enabled=True
    )
    async def ping(ctx):
        """ Answers with pong """
        await ctx.send("pong")
        
    @bot.command(
        aliases=['b'],
        help="Call and Response",
        description="Answers with bong",
        enabled=True
    )
    async def bing(ctx):
        """ Answers with bong """""
        await ctx.send("bong")
        
    @bot.command(
        aliases=['d'],
        help="Call and Response",
        description="Answers with dong",
        enabled=True
    )
    async def ding(ctx):
        """ Answers with dong """""
        await ctx.send("dong")


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
import settings
import discord 
import requests
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
        aliases=['wisdom', 'wis'],
        help="Random Generators",
        description="Retrieves a randomly generated quote from Buddhist figures",
        enabled=True
    )
    async def wordsofwisdom(ctx):
        try:
            response = requests.get(settings.BUDDHA_API_URL)
            data = response.json()
            quote = data["text"]
            await ctx.send(quote)
        except Exception as e:
            logger.error(e)
            await ctx.send("Sorry, I couldn't retrieve a quote at this time")
        
    @bot.command(
        aliases=['vm', 'mock'],
        help="Random Generators",
        description="Retrieves a randomly generated vicious mockery insult",
        enabled=True
    )
    async def viciousmockery(ctx):
        try:
            response = requests.get(settings.INSULTS_API_URL)
            data = response.json()
            insult = data["insult"]
            await ctx.send(insult)
        except Exception as e:
            logger.error(e)
            await ctx.send("Sorry, I couldn't retrieve an insult at this time")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
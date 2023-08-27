import settings
import discord 
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

BUDDHA_API_URL = os.getenv("BUDDHA_API_URL")
INSULTS_API_URL = os.getenv("INSULTS_API_URL")

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
        response = requests.get(BUDDHA_API_URL)
        data = response.json()
        quote = data["text"]
        await ctx.send(quote)
        
    @bot.command(
        aliases=['vm'],
        help="Random Generators",
        description="Retrieves a randomly generated vicious mockery insult",
        enabled=True
    )
    async def viciousmockery(ctx):
        response = requests.get(INSULTS_API_URL)
        data = response.json()
        insult = data["insult"]
        await ctx.send(insult)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
    
    @bot.command()
    async def slap(ctx, who : discord.Member):
        await ctx.send(f"{ctx.author.name} slapped {who.mention}")

if __name__ == "__main__":
    run()
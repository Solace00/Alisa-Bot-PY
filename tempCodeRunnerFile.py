intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command=None)

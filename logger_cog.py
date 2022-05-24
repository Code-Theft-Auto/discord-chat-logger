import json,datetime,discord
from discord.ext.commands import Cog,context



KEYWORD = (
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R',
    'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M', '`', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '0', '-', '=', '[', ']', '\\', ';', "'", ',', '.', '/', '~', '!',
    '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':',
    '"', '<', '>', '?', '"', "'", ''
)

bot = discord.bot()

class Logger(Cog):
    """## A simple chat logger
    Make sure to create a file named log.json
    """

    def __init__(self, bot):
        self.bot = bot


    @Cog.listener('on_message')
    async def log(self,message: context.Context ):

        AUTHID = str(message.author.id)
        AUTHNAME = message.author

        with open("log.json", "r") as jsonfile:
            jsonfile = json.load(jsonfile)

        if message.content.startswith(KEYWORD):

            with open("log.json", "w") as f:

                if AUTHID in jsonfile:

                    time_ = datetime.datetime.now()

                    try:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": message.author.guild.name
                        }

                    except AttributeError:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": "DM"
                        }

                    else:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": message.author.guild.name
                        }

                    jsonfile[AUTHID]["messages"].append(content)
                    json.dump(jsonfile, f, indent=7)

                else:

                    time_ = datetime.datetime.now()

                    jsonfile[AUTHID] = {
                        "id": int(AUTHID),
                        "name": f"{AUTHNAME}",
                        "messages": []
                    }

                    try:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": message.author.guild.name
                        }

                    except AttributeError:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": "DM"
                        }

                    else:
                        content = {
                            "message": message.content,
                            "time": time_.strftime("%d/%m/%Y %I:%M %p"),
                            "guild": message.author.guild.name
                        }

                    jsonfile[AUTHID]["messages"].append(content)
                    json.dump(jsonfile, f, indent=7)
        await bot.process_commands(message)


def setup(bot):
    bot.add_cog(Logger)

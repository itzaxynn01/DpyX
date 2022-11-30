import discord
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed , File
from discord.ext.commands import CommandNotFound
from datetime import datetime
PREFIX = '+'
OWNER_IDS = [1046816200237256734]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX  ,
                            owner_ids = OWNER_IDS , 
                        intents=discord.Intents.all(),)
        
    

    def run(self , version):
        self.VERSION = version


        with open("./lib/bot/token.0", "r" , encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot ... ")
        super().run(self.TOKEN , reconnect=True)


    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")


    async def on_error(self, err ,*args ,**kwargs):
        if err == "on_command_error":
            await args[0].send("something went wrong")

        else:
            channel = self.get_channel(1046890155132330020)
            await channel.send("an error occured")
            raise 
    
    async def on_command_error(self, ctx,exc):
        if isinstance(exc, CommandNotFound):
            pass

        else:
            raise exc.original

    async def on_ready(self):
        if not self.ready:
            
            self.ready = True
            print("bot ready")

            channel = self.get_channel(1046890155132330020)
            await channel.send("now online")

            embed = Embed(title="now online", description="DpyX is Now online",colour=0xFF0000,timestamp=datetime.utcnow())
            fields =[("Name", "Value" , True),
                    ("Another Field", "This field is next to oithe one" , True),
                    ("a non inline field" , "this field will not appear on its own row",False)]
        for name , value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(text="this is footer")
                embed.set_author(name="dpyx",)
                await channel.send(embed=embed)

                await channel.send(file=File("./data/images/profile.png"))

                

        else:
            print("bot reconnected")
 
            

    async def on_message(self, message):
        pass


bot = Bot()
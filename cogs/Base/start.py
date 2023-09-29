from disnake.ext import commands
from disnake import (
    CommandInteraction,
    Embed,
    Member as DisnakeMember,
    User as DisnakeUser,
    Guild as DisnakeGuild,
)

from datetime import datetime

class Start(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command('help')
    async def help(self, ctx: commands. Context):
        channel = ctx.guild.system_channel

        emb = Embed(
            description=f"Рад всех привествовать я - {self.bot.user}",
            color=0x8B0000,
        )
        await channel.send(embed=emb)

    @commands.slash_command(
        description="Хелп",
        name='help'
    )
    async def slah_help(
            self,
            inter: CommandInteraction,
    ):

        emb = Embed(
            description=f"Рад всех привествовать я - {self.bot.user}",
            color=0x8B0000,
        )
        await inter.send(embed=emb)


def setup(bot: commands.Bot):
    bot.add_cog(Start(bot))
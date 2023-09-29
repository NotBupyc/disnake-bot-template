from disnake.ext import commands
from disnake import (
    Embed, 
    Member as DisnakeMember, 
    Guild as DisnakeGuild)

from config import Users, Guilds

class Join_And_Leave(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: DisnakeGuild):
        """Bot join in server"""
        if not await Guilds.get_server(guild.id):
            await Guilds.create_server(guild)
            
        channel = guild.system_channel

        emb = Embed(
            title="Всем привет!",
            description=f"Рад всех привествовать я - {self.bot.user}",
            color=0x8B0000,
        )
        await channel.send(embed=emb)

        for member in guild.members:
            if member.bot:
                continue
            if not await Users.get_user(member.id):
                await Users.create_user(member)


    # Join member in server
    @commands.Cog.listener()
    async def on_member_join(self, member: DisnakeMember):
        # channel = member.guild.system_channel
        
        if not Users.get_user(member.id):
            await Users.create_user(member)
            


    # Leave member from server
    @commands.Cog.listener()
    async def on_member_remove(self, member: DisnakeMember):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Join_And_Leave(bot))

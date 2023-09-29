from disnake.ext import commands
import os
import logging

from config import bot, TOKEN, COG_DIR, OTHER_COGS, BASE_DIR


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(asctime)s %(levelname)s %(message)s")


@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.NotOwner):
        pass
    logger.warning(error)


@bot.event
async def on_ready():
    print(f"\nBot {bot.user} was started \n")


@commands.is_owner()
@bot.command()
async def load(ctx: commands.Context, extension):
    if extension in OTHER_COGS:
        bot.load_extension(extension)
        print(f"Load cog: {extension}")
        await ctx.message.add_reaction("✅")
        return

    for file in os.listdir(rf"{COG_DIR}\{extension}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{extension}.{file[:-3]}")
            print(f"Загрузка кога: {extension} / {file}")
            await ctx.message.add_reaction("✅")


@commands.is_owner()
@bot.command()
async def unload(ctx: commands.Context, extension):
    if extension in OTHER_COGS:
        bot.unload_extension(extension)
        print(f"Unload cog: {extension}")
        await ctx.message.add_reaction("✅")
        return

    for file in os.listdir(rf"{COG_DIR}\{extension}"):
        if file.endswith(".py"):
            bot.unload_extension(f"{COG_DIR}.{extension}.{file[:-3]}")
            print(f"Unload cog: {extension} / {file}")
            await ctx.message.add_reaction("✅")


@commands.is_owner()
@bot.command()
async def reload(ctx: commands.Context, extension):
    if extension in OTHER_COGS:
        bot.reload_extension(extension)
        print(f"Reload cog: {extension}")
        await ctx.message.add_reaction("✅")
        return

    for file in os.listdir(rf"{COG_DIR}\{extension}"):
        if file.endswith(".py"):
            bot.reload_extension(f"{COG_DIR}.{extension}.{file[:-3]}")
            print(f"Reload cog: {extension} / {file}")
            await ctx.message.add_reaction("✅")


def main():
    """Loading cogs and starting bot"""
    print('--------Loading cogs--------')

    for dir in os.listdir(COG_DIR):
        for i, file in enumerate(os.listdir(rf'{COG_DIR}\{dir}')):
            if file.endswith(".py"):
                bot.load_extension(f"{COG_DIR}.{dir}.{file[:-3]}")
                print(f"({i+1}) Load cog: {dir} / {file}")

    print("\n--------Loading other cogs--------")
    for cog in OTHER_COGS:
        bot.load_extension(cog)
        print(f'Load cog: {cog}')

    bot.run(TOKEN)

if __name__ == "__main__":
    main()




import os
import json
import asyncio
import discord
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def prefix(self, ctx, sett = 'list', *, prefix = 'None!!!'):
        if sett == 'set':
            if ctx.author.has_permissions(manage_guild=True):
                if prefix == 'None!!!':
                    return await ctx.send("```MissingRequiredArgument: Atleast one argument is missing.```")

                else:
                    with open("./configs/prefixes.json", "r") as f:
                        prefixes = json.load(f)

                    prefixes[str(ctx.guild.id)] = prefix

                    with open("./configs/prefixes.json", "w") as f:
                        json.dump(prefixes, f, indent=2)

                    e = discord.Embed(
                        description='<:tickYes:787334378630938672> Successfully changed prefix to `{}`.'.format(prefix),
                        color=discord.Color.green()
                    )
                    #e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    #footerd(e)

                    await ctx.send(embed=e)
            else:
                return await ctx.send("```You are missing Manage Server permission(s) to run this command.```")

        if sett == 'list':
            with open("./configs/prefixes.json", "r") as f:
                prefixes = json.load(f)

            e = discord.Embed(
                description='Current prefix is `' + prefixes.get(f"{str(ctx.guild.id)}") + '`.',
                color=emcolor
            )
            #e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            #footerd(e)
            await ctx.send(embed=e)

        else:
            return await ctx.send('```BadArgument: There are only two options (set, list).```')
            
    @commands.command(aliases=['setmuterole', 'set_mute_role'])
    @commands.guild_only()
    async def muterole(self, ctx, *, role: discord.Role):
        if ctx.author.has_permissions(manage_guild=True):
            a = await ctx.send(f"<a:dicegif:786111161036701736> Setting the **{role.name}** role as the muterole...")

            try:
                with open('./configs/muteroles.json', "r") as p:
                    thing = json.load(p)
            except:
                with open('./configs/muteroles.json', "w") as pp:
                    pp.write("{}")

            thing[str(ctx.guild.id)] = int(role.id)

            with open('./configs/muteroles.json', "w") as f:
                json.dump(thing, f, indent=2)

            await a.edit(content=f"<:tickYes:787334378630938672> Saved the **{role.name}** role as the muterole.")

def setup(bot):
    bot.add_cog(Configuration(bot))
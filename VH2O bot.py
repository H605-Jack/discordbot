import discord
import time
import asyncio
import random
from discord.ext import commands
from itertools import cycle

messages = joined = 0
client = commands.Bot(command_prefix='.')
status = cycle(['Status', 'On Air'])


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


#####################
#   I. Main Commands
#   The statements using for develop the commands for everybody in server.
####


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


def read_text_channel():
    with open("id ex(1).txt") as e:
        lines = e.readlines()
        return lines[0].strip()


bot = discord.Client
token = read_token()
client.remove_command('help')


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(200)
        except Exception as e:
            print(e)
            await asyncio.sleep(200)


async def record_usage(ctx):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)


@client.command()
@commands.before_invoke(record_usage)
async def who(ctx):  # Output: <User> used who at <Time>
    await ctx.send('i am a bot')


@client.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx):
    await ctx.send('You can manage messages.')


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(780075933830873099)

    if message.author == client.user:
        return
    if message.content.find("Hello") != -1:
        await message.channel.send("xin chao")
    if message.content.find("hello") != -1:
        await message.channel.send("xin chao")
    if message.content.find('fuck') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('shit') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('bitch') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('cock') != -1:
        await message.channel.send("Hey! That word is not allowed here! ⛔️")
    if message.content.find('c0ck') != -1:
        await message.channel.send("⚠️ B O N K !! Stop swearing!")
    if message.content.find('sex') != -1:
            await message.channel.send("Hey, friend! That NSFW word is not allowed here! ⛔️")
    if message.content.find('pussy') != -1:
        await message.channel.send("Hey, friend! That word is not allowed here! ⛔")
    if message.content.find('cum') != -1:
            await message.channel.send("Hey! That word is not allowed here! ⛔")
    if message.content.find('FUCK') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('SHIT') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('BITCH') != -1:
        await message.channel.send("⚠️WARNING!! NO SWEARING! FOLLOW THE RULES!")
    if message.content.find('COCK') != -1:
        await message.channel.send("Hey! That word is not allowed here! ⛔️")
    if message.content.find('C0CK') != -1:
        await message.channel.send("⚠️ B O N K !! Stop swearing!")
    if message.content.find('SEX') != -1:
            await message.channel.send("Hey, friend! That NSFW word is not allowed here! ⛔️")
    if message.content.find('PUSSY') != -1:
        await message.channel.send("Hey, friend! That word is not allowed here! ⛔")
    if message.content.find('CUM') != -1:
            await message.channel.send("Hey! That word is not allowed here! ⛔")
    elif message.content == "_users":
        await message.channel.send(f"""# of Members: {id.member_count}""")
    else:
        print(f"""user: {message.author} send {message.content}, in channel {message.channel}""")

    await client.process_commands(message)


client.loop.create_task(update_stats())


@client.command()
async def ping(ctx):
    await ctx.send(f'Well, here it is! {round(client.latency * 1000)}')


@client.command(aliases=['heyVH2O'])
async def _heyvh2o(ctx, *, question):
    if ctx.author == client.user:
        return
    responses = ['I can move like that.',
                 "I'm so cold today...",
                 "Me like that.",
                 "Maybe",
                 "Nah, -.- ask another question plz",
                 "Ask NekoBot đi I'm busy :|",
                 "Ask Jackie (王杰), I'm idiot ",
                 "☀️ sunrise",
                 "pét pẹt :|",
                 "誰明浪子心?",
                 "I remember my dad fought a lot during Vietnam War... ",
                 'I can watch some Japanese Anime now :)']
    await ctx.send(f'Answer: {random.choice(responses)}')


@_heyvh2o.error
async def _heyvh2o_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("""```.heyVH2O <question>
        
Ask for question.```""")


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def info(ctx, *, member: discord.Member):
    fmt = """```{0}
joined on {0.joined_at}
has {1} roles.```"""
    await ctx.send(fmt.format(member, len(member.roles)))


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("""```.info <member.mention> 
        
please mention a member.```""")
    if isinstance(error, commands.BadArgument):
        await ctx.send("""```.info <member.mention> 

please mention a member.```""")


##########
#     II. About Bot information
#     Use these resources from VH2O Assistant to help.
#####


@client.command(pass_content=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title='VH2O Assistant Bot',
        description="""
        VH2O Assistant prefix = `.`
        Here is some commands you can use for interact with bot:
        `ping` = Returns the report of ping (ms).
        `heyVH2O` = Ask assistant with question. 
        `_users` = Check the numbers of members.
        
        # Please notice: If you all see the bot is online with status said `playing On Air`, that's means bot is now 
        activate from Python. Otherwise (only Online status), bot is not activated.
        
        Need more help? Ask Jackie for help.
                    """
    )

    await ctx.send(embed=embed)


client.run(token)

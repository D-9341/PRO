import asyncio
import random
import datetime
import json
import os
import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = commands.when_mentioned_or('cy\\'), owner_id = 338714886001524737)
client.remove_command('help')

guilds = [693929822543675455, 735874149578440855]
members = [338714886001524737]

#Fun
@client.command()
@commands.cooldown(1, 3, commands.BucketType.default)
async def rp(ctx):
    await ctx.message.delete()
    emb = discord.Embed(description = '[Ныа](https://www.youtube.com/watch?v=idmTSW9mfYI)', colour = discord.Color.orange())
    await ctx.send(embed = emb)
        
@client.command(aliases = ['.rap'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def rap(ctx):
    await ctx.message.delete()
    emb = discord.Embed(colour = ctx.author.color)
    emb.set_image(url = 'https://thumbs.gfycat.com/MessyCarefreeHousefly-size_restricted.gif')
    await ctx.send(embed = emb)
        
@client.command()
@commands.cooldown(1, 5, commands.BucketType.default)
async def zatka(ctx):
    await ctx.message.delete()
    emb = discord.Embed(title = 'Форма заявки для Набор кадров', colour = ctx.author.color)
    emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
    emb.add_field(name = '(1). ZATKA в STEAM.  ZATKA_KING#8406 в Discord.', value = 'возраст 14+  часовой пояс IL +0.', inline = False)
    emb.add_field(name = '(2). Интересующая управление:', value = 'Discord', inline = False)
    emb.add_field(name = '(3). Опыт администрирования:', value = 'Есть.', inline = False)
    emb.add_field(name = 'творческие:', value = 'Есть.', inline = False)
    emb.add_field(name = 'технические навыки:', value = 'Нет.', inline = False)
    emb.add_field(name = '(4). Сколько часов готовы уделять работе', value = '[ 15+ в неделю ]', inline = False)
    emb.add_field(name = 'в какое время дня свободны', value = '16:00 до 22:00+', inline = False)
    await ctx.send(embed = emb)

@client.command(aliases = ['Cu', 'CU'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def cu(ctx):
    await ctx.message.delete()
    await ctx.send('Медь')
    
@client.command(aliases = ['c', 'C', 'coin', 'Coin', 'COIN', 'Coinflip', 'COINFLIP'])
@commands.cooldown(3, 3, commands.BucketType.default)
async def coinflip(ctx):
    await ctx.message.delete()
    emb = discord.Embed(description = 'Решка!', colour = discord.Color.red())
    emb.set_image(url = 'https://static.ayana.io/commands/flipcoin/heads.png')
    emb1 = discord.Embed(description = 'Орёл!', colour = discord.Color.red())
    emb.set_image(url = 'https://static.ayana.io/commands/flipcoin/tails.png')
    choices = [emb, emb1]
    rancoin = random.choice(choices)
    await ctx.send(embed = rancoin)
#Fun

#Embeds
@client.command(aliases = ['ctx'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def content(ctx, arg):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        message = await ctx.fetch_message(id = arg)
        if message.author == client.user:
            await ctx.send(f'```cy/say noembed "{message.content}"```')
        else:
            await ctx.send(f'```{message.content}```')

@client.command(aliases = ['emb_ctx'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def emb_content(ctx, arg):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приветную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        message = await ctx.fetch_message(id = arg)
        for emb in message.embeds:
            if message.author == client.user:
                await ctx.send(f'```cy/say "" "" t& {emb.title} d& {emb.description} f& {emb.footer.text} c& {emb.colour} a& {emb.author.name} img& {emb.image.url} fu& {emb.thumbnail.url}```')
            else:
                await ctx.send(f'```title {emb.title} description {emb.description} footer {emb.footer.text} color {emb.colour} author {emb.author.name} image {emb.image.url} footer img {emb.thumbnail.url}```')
            
@client.command(aliases = ['emb_e'])
@commands.has_permissions(mention_everyone = True)
@commands.cooldown(1, 20, commands.BucketType.default)
async def say_everyone(ctx, arg = None, text = None, t = None, d = None, fu = None, img = None, f = None, c = None, a : discord.Member = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        if c == None:
            c = ctx.author.color
        else:
            c = int('0x' + c, 16)
        if a == None:
            a = ctx.author
        if img == None:
            img = ('')
        if f == None:
            f = ('')
        if fu == None:
            fu = ('')
        emb = discord.Embed(title = t, description = d, colour = c)
        emb.set_author(name = a, icon_url = a.avatar_url)
        emb.set_image(url = img)
        emb.set_thumbnail(url = f)
        emb.set_footer(text = fu)
        if arg == 'noembed':
            await ctx.send('@everyone ' + text)
        elif arg != 'noembed':
            await ctx.send('@everyone', embed = emb)
    
@client.command(aliases = ['Say', 'SAY'])
@commands.has_permissions(manage_channels = True)
async def say(ctx, arg = None, text = None, t = None, d = None, fu = None, img = None, f = None, c = None, a : discord.Member = None, *, role: discord.Role = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        if c == None:
            c = ctx.author.color
        else:
            c = int('0x' + c, 16)
        if a == None:
            a = ctx.author
        if img == None:
            img = ('')
        if f == None:
            f = ('')
        if role != None:
            c = role.color
        if fu == None:
            fu = ('')
        emb = discord.Embed(title = t, description = d, colour = c)
        emb.set_author(name = a, icon_url = a.avatar_url)
        emb.set_image(url = img)
        emb.set_thumbnail(url = f)
        emb.set_footer(text = fu)
        if role is not None and arg != 'noembed':
            await ctx.send(f'{role.mention}', embed = emb)
        elif role is None and arg != 'noembed':
            await ctx.send(embed = emb)
        if arg == 'noembed':
            await ctx.send(text)

@client.command(aliases = ['emb_ed'])
@commands.has_permissions(manage_channels = True)
async def emb_edit(ctx, arg, t = None, d = None, fu = None, img = None, f = None, c = None, a : discord.Member = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        message = await ctx.fetch_message(id = arg)
        if c == None:
            c = ctx.author.color
        else:
            c = int('0x' + c, 16)
        if a == None:
            a = ctx.author
        if img == None:
            img = ('')
        if f == None:
            f = ('')
        if fu == None:
            fu = ('')
        emb = discord.Embed(title = t, description = d, colour = c)
        emb.set_author(name = a, icon_url = a.avatar_url)
        emb.set_image(url = img)
        emb.set_thumbnail(url = f)
        emb.set_footer(text = fu)
        await message.edit(embed = emb)
        await ctx.send('👌', delete_after = 1)
    
@client.command(aliases = ['Edit', 'EDIT'])
@commands.has_permissions(manage_channels = True)
async def edit(ctx, arg, *, text):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        message = await ctx.fetch_message(id = arg)
        await message.edit(content = text)
        await ctx.send('👌', delete_after = 1)
#Embeds

#Cephalon
@client.command(aliases = ['Join', 'JOIN'])
async def join(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        else:
            emb = discord.Embed(description = 'Ты должен быть в канале, чтобы использовать это.', colour = discord.Color.orange())
            await ctx.send(embed = emb)
            return
        vc = await channel.connect()

@client.command(aliases = ['Ping', 'PING'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def ping(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        emb = discord.Embed(description = f'Pong! `{round(client.latency * 1000)} ms`', colour = discord.Color.red(), timestamp = ctx.message.created_at)
        await ctx.send(embed = emb)

@client.command(aliases = ['Info', 'INFO'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def info(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        await ctx.send(f'Сервер `{ctx.guild}` не имеет активных подписок. Если вы купили приватную версию, напишите разработчику, чтобы ваш сервер был добавлен в список разрешённых.')
    else:
        emb = discord.Embed(colour = discord.Color.red())
        emb.set_author(name = client.user.name, url = 'https://warframe.fandom.com/wiki/Cephalon_Cy', icon_url = client.user.avatar_url)
        emb.add_field(name = 'Версия', value = '0.12.7.9018')
        emb.add_field(name = 'Написан на', value = 'discord.py')
        emb.add_field(name = 'Разработчик', value = 'сасиска#2472')
        emb.add_field(name = 'Веб-сайт', value = '```http://ru-unioncraft.ru/```')
        emb.set_footer(text = 'Данное приложение не имеет никакого причастия к игре Warframe.', icon_url = 'https://i.playground.ru/p/yVaOZNSTdgUTxmzy_qvzzQ.png')
        await ctx.send(embed = emb)

@client.command(aliases = ['invcy'])
@commands.cooldown(1, 3, commands.BucketType.default)
async def invite(ctx):
    await ctx.message.delete()
    if ctx.message.author.id != 338714886001524737:
        await ctx.send(f'{ctx.author.mention}, вы не являетесь владельцем данного бота. Пашол нахуй')
    else:
        emb = discord.Embed(description = '[Ссылка](https://discord.com/oauth2/authorize?client_id=762015251264569352&scope=bot&permissions=8) для быстрого приглашения меня на сервера. Даже не пытайтесь вызвать эту команду, если вы не сасиска#2472. А, и ещё - даже если вы пригласите меня - вы не сможете выполнять команды.', colour = discord.Color.red())
        await ctx.send(embed = emb)
#Cephalon
        
#корень
@client.command(aliases = ['Help', 'HELP'])
@commands.cooldown(1, 3, commands.BucketType.default)
async def help(ctx, arg = None):
    await ctx.message.delete()
    if arg == None:
        emb = discord.Embed(title = "Меню команд Cephalon Cy", description = 'Существует дополнительная помощь по командам, пропишите cy\\help |команда|', colour = discord.Color.red())
        emb.add_field(name = 'cy\\about', value = 'Показывает информацию о человеке.')
        emb.add_field(name = 'cy\\avatar', value = 'Показывает аватар человека.')
        emb.add_field(name = 'cy\\ban', value = 'Бан человека.')
        emb.add_field(name = 'cy\\clear', value = 'Очистка чата.')
        emb.add_field(name = 'cy\\dm', value = 'Пишет участнику любой написанный текст.')
        emb.add_field(name = 'cy\\edit', value = 'Редактирует сообщение.', inline = False)
        emb.add_field(name = 'cy\\say', value = 'От лица бота отправляется высоконастраеваемый эмбед. Может использоваться как say, так и emb')
        emb.add_field(name = 'cy\\emb_ctx', value = 'Позволяет увидеть контент эмбеда.')
        emb.add_field(name = 'cy\\emb_edit', value = 'Редактирует эмбед. Работает как VAULTBOT', inline = False)
        emb.add_field(name = 'cy\\say_everyone', value = 'Совмещает в себе команды everyone и say.')
        emb.add_field(name = 'cy\\everyone', value = 'Пишет сообщение от лица бота и пингует @everyone')
        emb.add_field(name = 'cy\\give', value = 'Выдаёт роль.', inline = False)
        emb.add_field(name = 'cy\\guild', value = 'Показывает информацию о сервере.')
        emb.add_field(name = 'cy\\join', value = 'Бот заходит в голосовой канал.')
        emb.add_field(name = 'cy\\kick', value = 'Кик человека.')
        emb.add_field(name = 'cy\\mute', value = 'Мут человека.', inline = False)
        emb.add_field(name = 'cy\\remind', value = 'Может напомнить вам о событии, которое вы не хотите пропустить.')
        emb.add_field(name = 'cy\\role', value = 'Показывает информацию о роли')
        emb.add_field(name = 'cy\\take', value = 'Забирает роль.', inline = False)
        emb.add_field(name = 'cy\\unmute', value = 'Принудительный размут человека.')
        emb.add_field(name = 'Обозначение символов cy\\help', value = '|| - опционально, <> - обязательно')
        emb.set_footer(text = 'Cephalon Cy by сасиска#2472')
        await ctx.send(embed = emb)
    elif arg == 'about':
        await ctx.send('```cy\\about |@пинг/имя/ID|```')
    elif arg == 'avatar':
        await ctx.send('```cy\\avatar |@пинг/имя/ID|```')
    elif arg == 'ban':
        await ctx.send('```cy\\ban <@пинг/имя/ID> |причина|```')
    elif arg == 'clear':
        await ctx.send('```cy\\clear <количество> |confirm|```')
    elif arg == 'dm':
        await ctx.send('```cy\\dm <@пинг/имя/ID> <текст>```')
    elif arg == 'edit':
        await ctx.send('```cy\\edit <ID> <новый текст>```')
    elif arg == 'say':
        await ctx.send('```cy\\say |noembed| |text| |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг/имя/ID| |@роль/имя роли/ID роли|(cy\\say "" "" "title" "description" "footer")```')
    elif arg == 'emb_ctx':
        await ctx.send('```cy\\emb_ctx <ID>```')
    elif arg == 'emb_edit':
        await ctx.send('```cy\\emb_edit <ID> |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг/имя/ID| |@роль/имя роли/ID роли|```')
    elif arg == 'say_everyone':
        await ctx.send('```cy\\say_everyone |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг/имя/ID| |@роль/имя роли/ID роли|(cy\\say_everyone "" "" "title" "description" "footer")```')
    elif arg == 'give':
        await ctx.send('```cy\\give <@пинг/имя/ID> <@роль/имя роли/ID роли>```')
    elif arg == 'kick':
        await ctx.send('```cy\\kick <@пинг/имя/ID> |причина|```')
    elif arg == 'mute':
        await ctx.send('```cy\\mute <@пинг/имя/ID> <время(s,m,h,d(15s, 5m, 1h, 5d))> |причина|```')
    elif arg == 'remind':
        await ctx.send('```cy\\remind <время(s,m,h,d(15s, 5m, 1h, 5d))> <текст>```')
    elif arg == 'role':
        await ctx.send('```cy\\role <@роль/имя роли/ID роли>```')
    elif arg == 'take':
        await ctx.send('```cy\\take <@пинг/имя/ID> <@роль/имя роли/ID роли>```')
    elif arg == 'unmute':
        await ctx.send('```cy\\unmute <@пинг/имя/ID> |причина|```')
    else:
        emb = discord.Embed(description = 'Для этой команды не нужны аргументы', colour = discord.Color.red())
        emb.set_footer(text = 'Хотя, возможно, вы ввели команду неправильно?')
        await ctx.send(embed = emb)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = 'В Discord API'))
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        emb = discord.Embed(description = f'{ctx.author.mention}, я не знаю такую команду!', colour = discord.Color.red())
        emb.set_footer(text = 'Считаете, что такая команда должна быть? Напишите сасиска#2472 и опишите её суть!')
        await ctx.send(embed = emb)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()
        emb = discord.Embed(description = f'{ctx.author.mention}, команда в кд, потерпи чутка!', colour = discord.Color.red())
        await ctx.send(embed = emb)
#корень
        
        
t = os.environ.get('t')
client.run(t)

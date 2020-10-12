import asyncio
import random
import datetime
import re
import json
import os
import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = commands.when_mentioned_or('cy\\'), owner_id = 338714886001524737)
client.remove_command('help')

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {'h': 3600, 's': 1, 'm': 60, 'd': 86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        time = 0
        matches = re.findall(time_regex, args)
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(f'{value} не является правильным аргументом! Правильные: h|m|s|d')
            except ValueError:
                raise commands.BadArgument(f'{key} не число!')
        return time

guilds = [693929822543675455, 735874149578440855]
         #SPELL               #test guild

#Events
@client.event
async def on_guild_join(guild):
    if guild.id not in guilds:
        channel = client.get_channel(693929823030214658)
        emb = discord.Embed(description = f'Я был несанкционированно добавлен на сервер `{guild.name}` | ID {guild.id}', colour = discord.Color.red())
        await channel.send(embed = emb)
    else:
        channel = client.get_channel(693929823030214658)
        emb = discord.Embed(description = f'Я был санкционированно добавлен на сервер `{guild.name}` | ID {guild.id}', colour = discord.Color.red())
        await channel.send(embed = emb)
#Events

#Mod
@client.command()
@commands.has_permissions(view_audit_log = True)
@commands.cooldown(1, 5, commands.BucketType.default)
async def dm(ctx, member: discord.User, *, text):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(description = f'{text}', colour = ctx.author.color)
        emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await member.send(embed = emb)

@client.command(aliases = ['Kick', 'KICK'])
@commands.cooldown(1, 10, commands.BucketType.default)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason: str = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if member.id != 338714886001524737:
            if reason == None:
                reason = 'Не указана.'
            if ctx.author.top_role == member.top_role:
                emb = discord.Embed(description = f'{ctx.author.mention}, ваша высшая роль равна высшей роли {member.mention}. Кик отклонён.', colour = discord.Color.red())
                await ctx.send(embed = emb)
            else:
                emb = discord.Embed(colour = member.color)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                emb.add_field(name = 'Был кикнут', value = member.mention)
                emb.add_field(name = 'По причине', value = reason)
                await ctx.send(embed = emb)
                await member.kick(reason = reason)
        else:
            emb = discord.Embed(description = f'Извините, {ctx.author.mention}, но вы не можете кикнуть моего создателя!', colour = discord.Color.red())
            await ctx.send(embed = emb)

@client.command(aliases = ['Ban', 'BAN'])
@commands.cooldown(1, 10, commands.BucketType.default)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if member.id != 338714886001524737:
            if reason == None:
                reason = 'Не указана.'
            if ctx.author.top_role == member.top_role:
                emb = discord.Embed(description = f'{ctx.author.mention}, ваша высшая роль равна высшей роли {member.mention}. Бан отклонён.', colour = discord.Color.red())
                await ctx.send(embed = emb)
            else:
                emb = discord.Embed(colour = member.color)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                emb.add_field(name = 'Был кикнут', value = member.mention)
                emb.add_field(name = 'По причине', value = reason)
                await ctx.send(embed = emb)
                await member.ban(reason = reason)
        else:
            emb = discord.Embed(description = f'Извините, {ctx.author.mention}, но вы не можете забанить моего создателя!', colour = discord.Color.red())
            await ctx.send(embed = emb)

@client.command(aliases = ['Give', 'GIVE'])
@commands.has_permissions(manage_channels = True)
async def give(ctx, member: discord.Member, *, role: discord.Role):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if role != None:
            if role > member.top_role and ctx.message.author.id != 338714886001524737:
                await ctx.send('Вы не можете выдать эту роль, так как она имеет более высокий ранг, чем ваша высшая роль.')
            elif role == ctx.author.top_role and ctx.message.author.id != 338714886001524737:
                await ctx.send('Вы не можете выдать эту роль кому-либо, так как она равна вашей высшей роли.')
            elif role.is_default():
                await ctx.send('Выдавать everyone? Всё с башкой хорошо?')
            else:
                await member.add_roles(role)
                channel = client.get_channel(714175791033876490)
                emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                emb.add_field(name = 'Была выдана роль', value = f'{role.mention} | {role.name} | ID {role.id}')
                emb.add_field(name = 'Выдана:', value = member.mention)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await channel.send(embed = emb)
        else:
            emb = discord.Embed(description = f'{ctx.author.mention}, я не могу найти {role.mention} в списке ролей.', colour = member.color, timestamp = ctx.message.created_at)
            await ctx.send(embed = emb)
            
@client.command(aliases = ['Take', 'TAKE'])
@commands.has_permissions(manage_channels = True)
async def take(ctx, member: discord.Member, *, role: discord.Role):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if role != None:
            if role > ctx.author.top_role and ctx.message.author.id != 338714886001524737:
                await ctx.send('Вы не можете забрать эту роль, так как она имеет более высокий ранг, чем ваша высшая роль.')
            elif role == ctx.author.top_role and ctx.message.author.id != 338714886001524737:
                await ctx.send('Вы не можете забрать эту роль у кого-либо, так как она равна вашей высшей роли.')
            elif role.is_default():
                await ctx.send('Забирать everyone? Всё с башкой хорошо?')
            else:
                await member.remove_roles(role)
                channel = client.get_channel(714175791033876490)
                emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                emb.add_field(name = 'Была забрана роль', value = f'{role.mention} | {role.name} | ID {role.id}')
                emb.add_field(name = 'Забрана:', value = member.mention)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await channel.send(embed = emb)
        else:
            emb = discord.Embed(description = f'{ctx.author.mention}, я не могу найти {role.mention} в списке ролей.', colour = member.color, timestamp = ctx.message.created_at)
            await ctx.send(embed = emb)
            
@client.command(aliases = ['Mute', 'MUTE'])
@commands.has_permissions(manage_channels = True)
async def mute(ctx, member: discord.Member, time: TimeConverter, *, reason: str = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if member.id != 338714886001524737:
            role = discord.utils.get(ctx.guild.roles, name = 'Muted')
            if role != None:
                await member.add_roles(role)
                if reason == None:
                    reason = 'Не указана'
                emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                emb.add_field(name = 'В муте', value = f'{member.mention}')
                emb.add_field(name = 'По причине', value = reason)
                emb.add_field(name = 'Время мута', value = f'{time}s')
                await ctx.send(embed = emb, delete_after = time)
                await asyncio.sleep(time)
                if role != None:
                    if role in member.roles:
                        emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                        emb.add_field(name = 'Размучен по истечению времени', value = member.mention)
                        emb.add_field(name = 'Был в муте по причине', value = reason)
                        emb.add_field(name = 'Время мута составляло', value = f'{time}s')
                        await member.remove_roles(role)
                        await ctx.send(f'{member.mention}', embed = emb)
                    else:
                        emb = discord.Embed(description = f'Снятие мута для {member.mention} не требуется. Роли Muted не обнаружено в списке ролей участника.', colour = discord.Color.red())
                        await ctx.send(embed = emb)
                else:
                    emb = discord.Embed(description = f'{ctx.author.mention}, Я не могу снять мут у {member.mention} из-за того, что роль Muted была удалена/отредактирована!', colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    await ctx.send(embed = emb)
            else:
                await ctx.guild.create_role(name = 'Muted', colour = discord.Colour(0x000001))
                role = discord.utils.get(ctx.guild.roles, name = 'Muted')
                emb1 = discord.Embed(description = f'{ctx.author.mention}, По причине того, что я не нашёл нужную роль, была создана роль {role.name} с цветом {role.colour}.', colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb1.set_footer(text = 'Это сообщение должно показываться только 1 раз. Иначе, роль была удалена/отредактирована')
                await ctx.send(embed = emb1)
                await asyncio.sleep(3)
                role = discord.utils.get(ctx.guild.roles, name = 'Muted')
                await member.add_roles(role)
                emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                emb.add_field(name = 'В муте', value = f'{member.mention}')
                emb.add_field(name = 'По причине', value = reason)
                emb.add_field(name = 'Время мута', value = f'{time}s')
                await ctx.send(embed = emb, delete_after = time)
                await asyncio.sleep(time)
                if role != None:
                    if role in member.roles:
                        emb = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                        emb.add_field(name = 'Размучен по истечению времени', value = member.mention)
                        emb.add_field(name = 'По причине', value = reason)
                        emb.add_field(name = 'Время мута составляло', value = f'{time}s')
                        await ctx.send(f'{member.mention}', embed = emb)
                        await member.remove_roles(role)
                    else:
                        emb = discord.Embed(description = f'Снятие мута для {member.mention} не требуется. Роли Muted не обнаружено в списке ролей участника.', colour = discord.Color.red())
                        await ctx.send(embed = emb)    
        else:
            emb = discord.Embed(description = f'Извините, {ctx.author.mention}, но вы не можете замутить моего создателя!', colour = discord.Color.red())
            await ctx.send(embed = emb)
        
@client.command(aliases = ['Unmute', 'UNMUTE'])
@commands.has_permissions(manage_channels = True)
async def unmute(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        role = discord.utils.get(ctx.guild.roles, name = 'Muted')
        if role != None:
            if role in member.roles:
                await member.remove_roles(role)
                if reason == None:
                    reason = 'Не указана.'
                emb = discord.Embed(title = f'Принудительное снятие мута у {member}', colour = member.color, timestamp = ctx.message.created_at)
                emb.add_field(name = 'Снял мут', value = ctx.author.mention)
                emb.add_field(name = 'По причине', value = reason)
                await ctx.send(embed = emb)
            else:
                emb = discord.Embed(description = 'Снятие мута не требуется. Роли Muted не обнаружено в списке ролей участника.')
                await ctx.send(embed = emb)
        else:
            emb = discord.Embed(description = f'{ctx.author.mention}, Я не могу снять мут у {member.mention} из-за того, что роль Muted была удалена/отредактирована!', colour = discord.Color.red(), timestamp = ctx.message.created_at)
            await ctx.send(embed = emb)

@client.command(aliases = ['Clear', 'CLEAR'])
@commands.cooldown(1, 10, commands.BucketType.default)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount: int, confirm: str = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
        return
    else:
        if amount == 0:
            emb = discord.Embed(description = 'Удалять 0 сообщений?', colour = discord.Color.red())
            await ctx.send(embed = emb, delete_after = 3)
        elif amount == 1:
            emb = discord.Embed(description = f'удалено {amount} сообщение', colour = discord.Color.red())
            await ctx.channel.purge(limit = amount)
            await ctx.send(embed = emb, delete_after = 1)
        elif amount == 2:
            emb = discord.Embed(description = f'удалено {amount} сообщения', colour = discord.Color.red())
            await ctx.channel.purge(limit = amount)
            await ctx.send(embed = emb, delete_after = 1)
        elif amount == 3:
            emb = discord.Embed(description = f'удалено {amount} сообщения', colour = discord.Color.red())
            await ctx.channel.purge(limit = amount)
            await ctx.send(embed = emb, delete_after = 1)
        elif amount == 4:
            emb = discord.Embed(description = f'удалено {amount} сообщения', colour = discord.Color.red())
            await ctx.channel.purge(limit = amount)
            await ctx.send(embed = emb, delete_after = 1)
        elif amount >= 10:
            if confirm == 'confirm':
                await ctx.send(f'Через 3 секунды будет удалено {amount} сообщений')
                await asyncio.sleep(3)
                await ctx.channel.purge(limit = amount + 1)
                await ctx.send(f'удалено {amount} сообщений', delete_after = 2)
            if confirm == None:
                emb = discord.Embed(description = f'{ctx.author.mention}, для выполнения этой команды мне нужно ваше подтвеждение! (чувствительно к регистру)', colour = discord.Color.red())
                await ctx.send(embed = emb)
        else:
            emb = discord.Embed(description = f'удалено {amount} сообщений', colour = discord.Color.red())
            await ctx.channel.purge(limit = amount)
            await ctx.send(embed = emb, delete_after = 1)
#Mod

#Misc
@client.command(aliases = ['Guild', 'GUILD'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def guild(ctx, guild: discord.Guild = None):
    await ctx.message.delete()
    if ctx.guild.id in guilds:
        if guild == None:
            guild = ctx.guild
		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        emb = discord.Embed(title = f'Информация о {guild}', colour = discord.Color.red(), timestamp = ctx.message.created_at)
        emb.add_field(name = 'ID сервера', value = guild.id)
        emb.add_field(name = 'Уровень сервера', value = guild.premium_tier)
        emb.add_field(name = 'Люди, бустящие сервер', value = guild.premium_subscribers)
        emb.add_field(name = 'Количество человек на сервере', value = guild.member_count)
        emb.add_field(name = 'Статусы', value = f'🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}')
        if len(guild.roles) >= 15:
            emb.add_field(name = f'Роли', value = 'Слишком много', inline = False)
        else:
            emb.add_field(name = f'Роли [{len(guild.roles)-1}]', value = ' '.join([role.mention for role in guild.roles[1:]]), inline = False)
        emb.add_field(name = 'Дата создания сервера', value = guild.created_at.strftime('%d/%m/%Y %H:%M:%S UTC'), inline = False)
        emb.set_thumbnail(url = guild.icon_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.default)
async def role(ctx, *, role: discord.Role):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if role.mentionable == False:
            role.mentionable = 'Нет'
        elif role.mentionable == True:
            role.mentionable = 'Да'
        if role.managed == False:
            role.managed = 'Нет'
        elif role.managed == True:
            role.managed = 'Да'
        if role.hoist == False:
            role.hoist = 'Нет'
        elif role.hoist == True:
            role.hoist = 'Да'
        emb = discord.Embed(title = role.name, colour = role.colour)
        emb.add_field(name = 'ID', value = role.id)
        emb.add_field(name = 'Цвет', value = role.color)
        emb.add_field(name = 'Упоминается?', value = role.mentionable)
        emb.add_field(name = 'Управляется интеграцией?', value = role.managed)
        emb.add_field(name = 'Позиция в списке', value = role.position)
        emb.add_field(name = 'Создана', value = role.created_at.strftime('%d/%m/%Y %H:%M:%S UTC'), inline = False)
        emb.add_field(name = 'Показывает участников отдельно?', value = role.hoist)
        await ctx.send(embed = emb)
    
@client.command(aliases = ['Avatar', 'AVATAR'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def avatar(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy)) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if user == None:
            user = ctx.author
        emb = discord.Embed(description = f'[Прямая ссылка]({user.avatar_url})', colour = user.color)
        emb.set_author(name = user)
        emb.set_image(url = user.avatar_url)
        await ctx.send(embed = emb)
    
@client.command(aliases = ['me', 'Me', 'ME', 'About', 'ABOUT'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def about(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if member == None:
            member = ctx.author
        if member.nick == None:
            member.nick = 'Не указан'
        if member.bot == False:
            bot = 'Неа'
        elif member.bot == True:
            bot = 'Ага'
        emb = discord.Embed(title = f'Информация о {member}', colour = member.color, timestamp = ctx.message.created_at)
        emb.add_field(name = 'ID', value = member.id)
        emb.add_field(name = 'Создан', value = member.created_at.strftime('%d/%m/%Y %H:%M:%S UTC'), inline = False)
        emb.add_field(name = 'Вошёл', value = member.joined_at.strftime('%d/%m/%Y %H:%M:%S UTC'), inline = False)
        emb.add_field(name = 'Упоминание', value = member.mention)
        emb.add_field(name = 'Имя', value = member.name)
        emb.add_field(name = 'Никнейм', value = member.nick)
        emb.add_field(name = 'Статус', value = member.status)
        emb.add_field(name = f'Роли [{len(member.roles)-1}]', value=' '.join([role.mention for role in member.roles[1:]]), inline = False)
        emb.add_field(name = 'Высшая Роль', value = member.top_role.mention, inline = False)
        emb.add_field(name = 'Бот?', value = bot)
        emb.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = emb)
        
@client.command()
@commands.cooldown(1, 5, commands.BucketType.default)
async def remind(ctx, time: TimeConverter, *, arg):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(colour = ctx.author.color, timestamp = ctx.message.created_at)
        emb.add_field(name = 'Напомню через', value = f'{time}s')
        emb.add_field(name = 'О чём напомню?', value = arg)
        await ctx.send(embed = emb, delete_after = time)
        await asyncio.sleep(time)
        emb = discord.Embed(colour = ctx.author.color, timestamp = ctx.message.created_at)
        emb.add_field(name = 'Напомнил через', value = f'{time}s')
        emb.add_field(name = 'Напоминаю о', value = arg)
        await ctx.send(f'{ctx.author.mention}', embed = emb)
#Misc

#Fun
@client.command()
@commands.cooldown(1, 3, commands.BucketType.default)
async def aye_balbec(ctx):
    await ctx.message.delete()
    emb = discord.Embed(colour = ctx.author.color)
    emb.set_image(url = 'https://sun9-61.userapi.com/tja5cuQthduwgxq2yMigLiUxfYq_5fqiA6cJWg/sZOkbPajoSY.jpg')
    await ctx.send(embed = emb)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.default)
async def rp(ctx):
    await ctx.message.delete()
    emb = discord.Embed(description = '[Ныа](https://www.youtube.com/watch?v=idmTSW9mfYI)', colour = discord.Color.red())
    await ctx.send(embed = emb)
        
@client.command(aliases = ['.rap'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def rap(ctx):
    await ctx.message.delete()
    emb = discord.Embed(colour = ctx.author.color)
    emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
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
    emb = discord.Embed(description = 'Орёл!', colour = discord.Color.red())
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/524213591084105729/763835275930632252/-removebg-preview.png')
    emb1 = discord.Embed(description = 'Решка!', colour = discord.Color.red())
    emb1.set_image(url = 'https://cdn.discordapp.com/attachments/524213591084105729/763837699240099890/-removebg-preview.png')
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        message = await ctx.fetch_message(id = arg)
        await message.edit(content = text)
        await ctx.send('👌', delete_after = 1)
#Embeds

#Cephalon
@client.command()
@commands.cooldown(1, 3, commands.BucketType.default)
async def pro(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` имеет активную подписку. Все пользователи могут пользоваться полным функционалом бота с минимальным пингом.', colour = discord.Color.red())
        await ctx.send(embed = emb)

@client.command(aliases = ['Join', 'JOIN'])
async def join(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        else:
            emb = discord.Embed(description = 'Ты должен быть в канале, чтобы использовать это.', colour = discord.Color.red())
            await ctx.send(embed = emb)
            return
        vc = await channel.connect()

@client.command(aliases = ['Ping', 'PING'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def ping(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(description = f'Pong! `{round(client.latency * 1000)} ms`', colour = discord.Color.red(), timestamp = ctx.message.created_at)
        await ctx.send(embed = emb)

@client.command(aliases = ['Info', 'INFO'])
@commands.cooldown(1, 5, commands.BucketType.default)
async def info(ctx):
    await ctx.message.delete()
    if ctx.guild.id not in guilds:
        emb = discord.Embed(description = f'Сервер `{ctx.guild}` не имеет активных подписок. Купить можно по [Ссылке](https://www.patreon.com/cephaloncy) Преимущества: пинг не более 25ms, больший аптайм, защита от несанкционированного добавления на сервера.', colour = discord.Color.red())
        await ctx.send(embed = emb)
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
        emb.add_field(name = 'cy\\say', value = 'От лица бота отправляется высоконастраеваемый эмбед. Может использоваться как для написания текстов, так и для отправки эмбедов.')
        emb.add_field(name = 'cy\\emb_ctx', value = 'Позволяет увидеть контент эмбеда.')
        emb.add_field(name = 'cy\\emb_edit', value = 'Редактирует эмбед. Работает как VAULTBOT', inline = False)
        emb.add_field(name = 'cy\\say_everyone', value = 'Совмещает в себе команды everyone и say.')
        emb.add_field(name = 'cy\\everyone', value = 'Пишет сообщение от лица бота и пингует @everyone')
        emb.add_field(name = 'cy\\give', value = 'Выдаёт роль.', inline = False)
        emb.add_field(name = 'cy\\guild', value = 'Показывает информацию о сервере.')
        emb.add_field(name = 'cy\\join', value = 'Бот заходит в голосовой канал.')
        emb.add_field(name = 'cy\\kick', value = 'Кик человека.')
        emb.add_field(name = 'cy\\mute', value = 'Мут человека.', inline = False)
        emb.add_field(name = 'cy\\pro', value = 'Показывает информацию о про версии. Также, проверяет на наличие активных подписок.')
        emb.add_field(name = 'cy\\remind', value = 'Может напомнить вам о событии, которое вы не хотите пропустить.')
        emb.add_field(name = 'cy\\role', value = 'Показывает информацию о роли')
        emb.add_field(name = 'cy\\take', value = 'Забирает роль.', inline = False)
        emb.add_field(name = 'cy\\unmute', value = 'Принудительный размут человека.')
        emb.add_field(name = 'Обозначение символов cy\\help', value = '|| - опционально, <> - обязательно')
        emb.set_footer(text = 'Cephalon Cy by сасиска#2472')
        await ctx.send(embed = emb)
    elif arg == 'about':
        await ctx.send('```cy\\about |@пинг|```')
    elif arg == 'avatar':
        await ctx.send('```cy\\avatar |@пинг|```')
    elif arg == 'ban':
        await ctx.send('```cy\\ban <@пинг> |причина|```')
    elif arg == 'clear':
        await ctx.send('```cy\\clear <количество> |confirm|```')
    elif arg == 'dm':
        await ctx.send('```cy\\dm <@пинг> <текст>```')
    elif arg == 'edit':
        await ctx.send('```cy\\edit <ID> <новый текст>```')
    elif arg == 'say':
        await ctx.send('```cy\\say |noembed| |text| |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг| |@роль|(cy\\say "" "" "title" "description" "footer")```')
    elif arg == 'emb_ctx':
        await ctx.send('```cy\\emb_ctx <ID>```')
    elif arg == 'emb_edit':
        await ctx.send('```cy\\emb_edit <ID> |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг| |@роль|```')
    elif arg == 'say_everyone':
        await ctx.send('```cy\\say_everyone |title текст| |description текст| |footer текст| |ссылка| |ссылка| |цвет| |@пинг| |@роль|(cy\\say_everyone "" "" "title" "description" "footer")```')
    elif arg == 'give':
        await ctx.send('```cy\\give <@пинг> <@роль/имя роли/ID роли>```')
    elif arg == 'kick':
        await ctx.send('```cy\\kick <@пинг> |причина|```')
    elif arg == 'mute':
        await ctx.send('```cy\\mute <@пинг> <время(s,m,h,d(15s, 5m, 1h, 5d))> |причина|```')
    elif arg == 'remind':
        await ctx.send('```cy\\remind <время(s,m,h,d(15s, 5m, 1h, 5d))> <текст>```')
    elif arg == 'role':
        await ctx.send('```cy\\role <@роль>```')
    elif arg == 'take':
        await ctx.send('```cy\\take <@пинг> <@роль>```')
    elif arg == 'unmute':
        await ctx.send('```cy\\unmute <@пинг> |причина|```')
    else:
        emb = discord.Embed(description = 'Для этой команды не нужны аргументы', colour = discord.Color.red())
        emb.set_footer(text = 'Хотя, возможно, вы ввели команду неправильно?')
        await ctx.send(embed = emb)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = 'Discord API'))
    
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

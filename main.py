# Разработчик: Florest. ©
# Ютуб канал: https://youtube.com/@florestone4185
# GitHub: https://github.com/Florest001
# Импорты.
import discord # Импортируем, библиотеку "discord.py", если она у Вас не установлена, необходимо ее установить.
from discord.ext import commands
from discord.utils import *
from config import * # Импортируем, токен, префикс, название бота из файла "config.py". (Эти значения можно менять, токен бота, необходимо надо вставить!)
import math # Импортируем, встроенный модуль в Python.
# Основной код.
print('Florest Developer. 21.03.2023. ©.\nПриветствую Вас, добро пожаловать. Сейчас, бот будет запускаться!')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name = 'Бот, был создан Флорестом. © (Вы можете это изменить в файле "main.py".)', type = discord.ActivityType.watching))
    print('Бот был успешно запущен.')
    print('Для, изменений, в коде зайдите в файл "main.py". Для изменений, в параметрах, зайдите в файл "config.py".')
    print('Бот был создан Флорестом. 21.03.2023.')
    print('Если, у Вас, произошла ошибка, напишите разработчику!')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
            title=f'Привет! Я - Florest Bot и я бот, созданный FlorestOne4185!',
            description='Ютуб канал Флореста: https://youtube.com/@florestone4185\nGitHub: https://github.com/Florest001',
            color=discord.Color.blue()
     )
    embed.add_field(name='Вам **понравился** бот, или появился, какая-то проблема?', value='Сообщите, об этом разработчику на эл. почту: `kirillborisenko2012@gmail.com`.')
    await ctx.send(embed=embed)

@bot.command()
async def calc(ctx, one: float, two: float, znak: str):
    if one and two:
        if znak == "+":
            otvet = one + two
        embed = discord.Embed(
            title=f'Калькулятор {bot_name}.',
            description=f'Пример: {one} + {two}.\nОтвет: {otvet}',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        if znak == "-":
            otvet = one - two
        embed = discord.Embed(
            title=f'Калькулятор {bot_name}.',
            description=f'Пример: {one} + {two}.\nОтвет: {otvet}',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        if znak == "*":
            otvet = one * two
        embed = discord.Embed(
            title=f'Калькулятор {bot_name}.',
            description=f'Пример: {one} + {two}.\nОтвет: {otvet}',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        if znak == "/":
            otvet = one / two
        embed = discord.Embed(
            title=f'Калькулятор {bot_name}.',
            description=f'Пример: {one} + {two}.\nОтвет: {otvet}',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Знак математического действия ({znak}) не поддерживается. (Поддерживается, только *, -, +, /.)')

@bot.command()
async def feedback(ctx, otzyv: str): # Создаём, команду feedback. ID канала, где будут присылаться отзывы, можно изменить в "config.py".
    if otzyv:
        embed = discord.Embed(
            title=f'Новый отзыв о {bot_name} от {ctx.author}.',
            description=f'Текст отзыва: {otzyv}',
            color=discord.Color.green()
        )
        embed.add_field(name=f'Вы тоже можете оставить отзыв о {bot_name}.', value=f'Для этого, пропишите команду, `{prefix}feedback <Ваш отзыв.>`.')
        await ctx.send(f'{ctx.author.mention}, спасибо за отзыв о {bot_name}.')
        feedback_chat = bot.get_channel(feedback_channel_id)
        feedback_chat.send(embed=embed)
    elif not otzyv:
        await ctx.send(f'{ctx.author.mention}, пожалуйста, введите ваш отзыв!')

@bot.command()
async def say_with_embed(ctx, message: str):
    if message:
        embed = discord.Embed(
            title=f'{ctx.author} сказал:',
            description=f'{message}',
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)
    elif not message:
        await ctx.send(f'Извините, {ctx.author}, но Вы не ввели, текст, который бот должен был написать в эмбеде.')

@bot.command()
async def say(ctx, message):
    if message:
        await ctx.send(message)
    elif not message:
        await ctx.send(f'{ctx.author.mention}, вы не ввели, сообщение, которое бот должен написать. (без эмбеда.)')

@bot.command()
async def say_with_channel(ctx, channel: discord.TextChannel, *, message):
    if message and channel:
        await channel.send(message)
    else:
        await ctx.send(f'{ctx.author.mention}, вы не упомянули канал, куда отправить сообщение, либо не ввели само сообщение!')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    if user:
        await user.ban(reason=reason)
        await ctx.send(f'{ctx.author.mention}, вы успешно заблокировали {user}.')
    elif not user:
        await ctx.send(f'{ctx.author.mention}, вы не ввели пользователя, для того, чтобы его заблокировать.')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if user:
        await user.kick(reason=reason)
        await ctx.send(f'{ctx.author.mention}, вы успешно выгнали {user} с сервера.')
    elif not user:
        await ctx.send(f'{ctx.author.mention}, вы не ввели пользователя, чтобы его выгнать.')


@bot.command()
async def request(ctx, reason):
    if reason:
        embed = discord.Embed(
            title=f'Новая заявка, на связь от {ctx.author}.',
            description=f'Причина обращения: {reason}'
        )
    elif not reason:
        await ctx.send(f'{ctx.author.mention}, вы не ввели причину обращения.')

bot.run(token)
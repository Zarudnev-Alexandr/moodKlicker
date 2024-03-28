import asyncio
import discord
import requests
from discord.ext import commands
from config_reader import config

intents = discord.Intents.all()
intents.guild_messages = True

url = config.url.get_secret_value()


bot = commands.Bot(command_prefix='!', intents=intents)
admin_id = '<@493001870051377157>'

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.command(name='import')
async def on_import(ctx):

    if ctx.guild is None:
        await ctx.reply("Команда доступна только на серверах, а не в личных сообщениях.")
        return

    if ctx.author == bot.user:
        return

    message = await ctx.reply("Если ты еще не пользовался tg ботом, то заходи: @moodClickerBot (а иначе "
                             "все следующие действия не будут иметь смысла)\n\nВведи свой telegram id (можно посмотреть в "
                             "нашем боте): ")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        try:
            telegram_id_msg = await bot.wait_for('message', check=check, timeout=30)
            telegram_id_str = telegram_id_msg.content.strip()
            await telegram_id_msg.delete()

            # Проверяем, что telegram_id может быть преобразован в int
            try:
                telegram_id = int(telegram_id_str)
                break  # Выходим из цикла, если ввод корректен
            except ValueError:
                await message.edit(content="Пожалуйста, введи корректный telegram id (целое число): ")

        except asyncio.TimeoutError:
            await message.edit(content="Превышено время ожидания. Попробуйте еще раз.")
            return

    await message.edit(content="Введи пароль, который ты указывал в нашем tg боте: ")

    while True:
        try:
            password_msg = await bot.wait_for('message', check=check, timeout=30)
            password = password_msg.content.strip()
            await password_msg.delete()
            break  # Выходим из цикла, если ввод получен
        except asyncio.TimeoutError:
            await message.edit(content="Превышено время ожидания. Попробуйте еще раз.")
            return

    # Удаляем сообщения пользователя из чата

    response = requests.put(f"{url}users/{telegram_id}/discord/{password}")
    data = response.json()
    status = response.status_code

    if status == 404:
        await message.edit(content="Неверный telegram id или пароль. Telegram id можно мосмотреть в нашем боте и там же сменить "
                                    "пароль. Ссылка на бота: https://t.me/moodClickerBot")

    elif status == 200:
        if data["convert_clicks"] == 0:
            await message.edit(content=f"😢Не хватает кликов на конвертацию. Курс: 30000 кликов = 1 серверная валюта. "
                                       f"Нужно еще "
                                        f"накликать")
        elif data["convert_clicks"] > 0:
            await message.edit(content=f"👆Кликов было: {data['number_of_clicks']}\n"
                                        f"✍Списано кликов: {data['written_off_clicks']}\n"
                                        f"🤑Валюты получено: {data['convert_clicks']}\n"
                                        f"💀Кликов осталось: {data['remaining_clicks']}\n"
                                        f"Для админа {admin_id}:\n\n")
            await ctx.send(f"-add-money bank {ctx.author} {data['convert_clicks']}")

bot.run(config.bot_token.get_secret_value())


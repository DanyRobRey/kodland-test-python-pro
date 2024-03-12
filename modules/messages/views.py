import os
from flask import Blueprint, request, jsonify
import discord
from discord.ext import commands
from aiogram import Bot, Dispatcher


messages_router = Blueprint(
    "messages",
    __name__,
)

# Discord bot settings
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)


@messages_router.route('/send-discord', methods=['POST'])
def send_message_discord_channel():
    content = request.json.get('content')
    channel_id = os.getenv("DISCORD_CHANNEL_ID")
    discord_token = os.getenv("DISCORD_TOKEN")

    @bot.event
    async def on_ready():
        channel = (bot.get_channel(channel_id) or await bot.fetch_channel(channel_id))
        await channel.send(content)
        await bot.close()

    bot.run(discord_token)

    return content

@messages_router.route('/send-telegram', methods=['POST'])
async def send_message_telegram():
    message = request.json.get('message')
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
    bot_telegram = Bot(token= os.getenv("TELEGRAM_TOKEN"))
    dp = Dispatcher()    

    if not channel_id or not message:
        return jsonify({'error': 'Chat id and message are required'}), 400

    await bot_telegram.send_message(chat_id=channel_id, 
                                    text=message)
    
    return jsonify({'message': f'Message send to channel_id: {channel_id}'}), 200

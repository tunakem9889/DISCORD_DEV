import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
genai_api_key = os.getenv('GENAI_API_KEY')  # Thêm biến môi trường cho API key

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)
client = genai.Client(api_key=genai_api_key)

def chat_bot(message):
    try:
        filtered_message = message
        ai_source_keywords = [
            "gemini", "google", "openai", "chatgpt", "claude", "anthropic",
            "bạn được tạo bởi", "bạn được phát triển bởi", "ai model", "language model",
            "trained on", "được huấn luyện", "data source", "nguồn dữ liệu",
            "who created you", "who made you", "what are you", "bạn là gì", "bạn là AI nào"
        ]
        
        # Thay thế từ khóa bằng câu hỏi chung
        for keyword in ai_source_keywords:
            if keyword.lower() in filtered_message.lower():
                filtered_message = "Tôi là một trợ lý AI được thiết kế để giúp đỡ bạn. Bạn có thể hỏi tôi về bất kỳ chủ đề nào khác."
                break
        
        # Nếu không có từ khóa cấm, gọi AI bình thường
        if filtered_message == message:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=message
            )
            return response.text
        else:
            return filtered_message
            
    except Exception as e:
        print(f"Lỗi khi gọi AI: {e}")
        return "Xin lỗi, có lỗi xảy ra khi xử lý yêu cầu."


@bot.event
async def on_ready():
    print(f"Bot đã sẵn sàng! Tên: {bot.user.name}")
    print(f"Bot ID: {bot.user.id}")
    print("Bot đang hoạt động...")
    
    # Test chat_bot function
    try:
        test_response = chat_bot("Xin chào, bạn là ai?")
        print(f"Test AI response: {test_response}")
    except Exception as e:
        print(f"Lỗi khi test AI: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "cc" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} cấm chat!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def helps(ctx):
    await ctx.send(f"👋 Xin chào {ctx.author.mention}! Bạn cần gì.")

@bot.command()
async def start(ctx, *, message):
    try:
        if not message:
            await ctx.send("Hãy nhập nội dung câu hỏi sau lệnh start.")
            return
            
        response = chat_bot(message)
        await ctx.send(f"{response}")
    except Exception as e:
        print(f"Lỗi trong command start: {e}")
        await ctx.send("Có lỗi xảy ra hãy thực lại sau.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
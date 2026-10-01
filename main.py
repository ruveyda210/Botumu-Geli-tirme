import discord
from discord.ext import commands
from model import get_class_name

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot hazir!")


@bot.command()
async def hello(ctx):
    await ctx.send("Merhaba!")


@bot.command()
async def check(ctx):

    if not ctx.message.attachments:
        await ctx.send("Lutfen bir resim gonder.")
        return

    try:
        image = ctx.message.attachments[0]

        if not image.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            await ctx.send("Lutfen PNG, JPG veya JPEG formatinda bir resim gonder.")
            return

        image_path = "image.jpg"

        await image.save(image_path)

        result = get_class_name(
            model_path="model/model.h5",
            labels_path="model/labels.txt",
            image_path=image_path
        )

        await ctx.send(f"Modelin tahmini: {result}")

    except Exception as error:
        print(error)
        await ctx.send("Uzgunum, resmi analiz ederken bir hata olustu.")


bot.run("BOT_TOKEN")
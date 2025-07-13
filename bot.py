import discord
import os
import ollama

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        response = ollama.chat(
            model='michaelscott:twss',
            messages=[
                {
                    'role': 'user',
                    'content': message.content,
                },
            ],
        )
        answer = response['message']['content'].strip()
        last_word = answer.split()[-1].lower().strip('.,!?')
        if last_word == 'yes':
            await message.reply("That's what she said")
    except Exception as e:
        print(f"Error processing message: {e}")


client.run(os.getenv('DISCORD_TOKEN'))

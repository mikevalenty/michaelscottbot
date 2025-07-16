import discord
import os
import ollama

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
ollama_client = ollama.AsyncClient()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        response = await ollama_client.generate(
            model='michaelscott:twss',
            prompt=f"<message>{message.content}</message>",
        )
        answer = response['response'].strip()
        last_word = answer.split()[-1].lower().strip('.,!?')
        if last_word == 'yes':
            print(answer)
            await message.reply("That's what she said")
    except Exception as e:
        print(f"Error processing message: {e}")


client.run(os.getenv('MICHAELSCOTTBOT_DISCORD_TOKEN'))

# MichaelScottBot

A Discord bot that responds with "That's what she said" to classic setups, in the style of Michael Scott from The Office.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Install and run Ollama:**
    Follow the instructions at [https://ollama.ai/](https://ollama.ai/) to install and run Ollama.

3.  **Create the Ollama model:**
    ```bash
    ollama create michaelscott:twss -f Modelfile
    ```

4.  **Set your environment variable:**
    Set the `DISCORD_TOKEN` environment variable to your Discord bot token.
    For example, in bash:
    ```bash
    export DISCORD_TOKEN=your_discord_token_here
    ```
    Replace `your_discord_token_here` with your actual Discord bot token.

## Running the bot

```bash
python bot.py
```

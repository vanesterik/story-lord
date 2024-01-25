from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from prompt import Prompt
from utils import (
    print_help,
    print_title_and_instuctions,
    print_version,
    write_to_clipboard,
)

# Load environment variables
load_dotenv(Path(".env").absolute())

# Create OpenAI client
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

# Create prompt object
prompt = Prompt()


def main() -> None:
    print_title_and_instuctions()

    while True:
        # Get user input
        query = input(f"{prompt.type}> ")

        # Check if user wants to exit
        if query in ("exit"):
            break

        # Check if user wants to see version
        elif query in ("-v", "--version", "version"):
            print_version()

        # Check if user wants to get help
        elif query in ("-h", "--help", "help"):
            print_help()

        # Check if user wants to change mode
        elif query in ("academic", "normal", "story"):
            print_title_and_instuctions()
            prompt.enable_prompt_type(query)

        else:
            # Send query to OpenAI
            completion = client.chat.completions.create(
                messages=prompt.parse_prompt_messages(query),
                model=getenv("OPENAI_MODEL") or "gpt-3.5-turbo",
            )

            # Define response
            response = completion.choices[0].message.content or ""

            # Copy response to clipboard
            write_to_clipboard(response)

            # Print respsonse to screen
            print(f"\n{response}\n")


if __name__ == "__main__":
    main()

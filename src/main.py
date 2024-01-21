import os
import textwrap
from pathlib import Path

import toml
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(Path(".env").absolute())

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main() -> None:
    # Clear screen
    os.system("clear")

    # Print app name and version
    print(f"Story Lord v{get_project_version()}")

    # Print instructions
    print('Type ":q", "quit", or "exit" to exit.\n')

    # Main loop
    while True:
        # Get user input
        query = input("> ")

        # Check if user wants to exit
        if query in (":q", "quit", "exit"):
            break

        else:
            # Send query to OpenAI
            completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    }
                ],
                model=os.getenv("OPENAI_MODEL") or "gpt-3.5-turbo",
            )

            # Define response
            response = completion.choices[0].message.content or ""

            # Copy response to clipboard
            os.system(f'echo "{response}" | pbcopy')

            # Print formatted response
            print(format_response(response))


def get_project_version() -> str:
    # Load project from pyproject.toml
    with open(Path("pyproject.toml").absolute(), "r") as f:
        project = toml.load(f)
    # Define varion
    version = project["project"]["version"]

    return version


def format_response(content: str) -> str:
    # Wrap text to 80 columns
    content = "\n".join(
        textwrap.wrap(
            content,
            width=80,
            replace_whitespace=False,
        )
    )
    # Add spacing
    content = f"\n{content}\n"

    return content


if __name__ == "__main__":
    main()

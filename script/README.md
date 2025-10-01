# OpenAI API Quickstart

Now this is the part most people won't do: run the script. It is not difficult. We lay out the instructions quite clearly and there are always external resources for additional help: chatbots, google, flashboys.ai community, etc.

> Your task: Run openai-api-quickstart.py and generate custom prompts for your Prompt Collection.

The first step is to make sure you have Python (with pip) installed. Python 3.4 and above, comes with pip pre-installed.

## Installing Python

### On Windows:

You can install Python 3 from the official Python website https://www.python.org/downloads/

1. Download the latest Windows installer.
2. Run the downloaded .exe installer.
3. Check "Add Python to PATH" checkbox to enable running Python from command line.
4. Complete your installation.
5. Verify your installation by opening Command Prompt or the terminal inside VS Code.

Run the command:

`python --version` or `python3 --version`

You should now see your version number.

### On Mac:

1. Python 2 is pre-installed, but you want Python 3.
2. Install Homebrew package manager from https://brew.sh
3. Use Terminal and run `brew install python` to install the latest Python 3.
4. Verify installation by running `python3 --version` in Terminal.
5. Use the `python3` command to run Python scripts.

### On Linux:

`You know how to install it.`

**Note: installation methods do change over time**

## Git Clone

You can download this project as a zip file, but it's better to clone it with Git.

On Windows, install git from the official website https://git-scm.com/downloads/win

On Mac, install by running `brew install git` in Terminal.

Once installed, run:

```
git clone https://github.com/flashboys-ai/flashboys-starter-pack.git
```

or

```
git clone git@github.com:flashboys-ai/flashboys-starter-pack.git
```

The ssh method is recommended but takes a little more work to set up.

## API Key

The low-cost api key from Open AI is more than worth it. The main secret lies in not only what you prompt, but how you prompt. Refer to our Short Prompt Guide inside `prompt-collection -> README.md` for more details.

Obtain your api key directly from the OpenAI website.

**Once you have your key, do the following to keep it safe:**

Navigate to the `script` folder. Make a copy of `.env.example` and save it as `.env`. Use the command only if it's quicker.

```
cp .env.example .env
```

Next, place your key inside the `.env` file and save.

```
OPENAI_API_KEY=YOUR_API_KEY
```

**Do not share your key with anyone and do not upload your .env file anywhere.**

Last step, install `dotenv` via `pip` using the terminal:

```
pip install dotenv
```

You are now ready to run the script and generate your prompts!

## Generate Your Prompts

Running the script is straightforward now:

```
python3 openai-api-quickstart.py
```

Let's walk through the code.

```
# Imports go at the top
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variable from .env file
load_dotenv()

# Get the API key from environment variable and pass it into api_key
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt example from Short Prompt Guide
prompt_example = (
  "You are my new prompting expert"
  "Give me 3 of your best prompting tips"
  "Use your tips and give me 1 example"
  "Write it out in the style of a humanoid"
)

# Select a model from the OpenAI models pack. GPT-5-nano, GPT-5-Codex,...
response = client.responses.create(
  model="gpt-5-nano",
  input=prompt_example # <--- Input prompt here
)

# Print the response
print(response.output_text)

# Store the response in a new variable
response_output = response.output_text

# Save the prompt to a text file inside prompt-collection
with open("../prompt-collection/prompt1.txt", "w") as file:
  file.writelines(response_output)
```

Well that covers it. Time to start creating your prompts and building up your Prompt Collection `|-- ···`

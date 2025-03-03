import sys
import os
import re
import pyperclip
import textwrap
from llama_cpp import Llama
from contextlib import redirect_stdout, redirect_stderr
from utils import fix_whitespace, format_response_text, make_prompt
from command_type import CommandType

## Ask user for operation type
def get_command_type():
    print("Select an operation:")
    print("1. Document code")
    print("2. Write unit tests")
    print("3. Refactoring")
    choice = input("Enter option number: ").strip()
    if choice == "1":
        return CommandType.DOCUMENT
    elif choice == "2":
        return CommandType.UNIT_TEST
    elif choice == "3":
        return CommandType.REFACTORING
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
command_type = get_command_type()

## Ask user for code snippet
print("\n📋 Paste code below (press Ctrl+D on a new line to submit):")
text = sys.stdin.read().strip()
print("\n⏳ Processing ...")

## Load model
with open(os.devnull, "w") as fnull, redirect_stdout(fnull), redirect_stderr(fnull):
    llm = Llama(
        model_path="./deepseek-coder-6.7b-instruct.Q4_K_M.gguf",
        verbose=False
    )

## Generate response
prompt = make_prompt(text, command_type)
response = llm(prompt, max_tokens=32768, temperature=0.2, top_p=0.9)
response_text = response["choices"][0]["text"].strip()
response_text = format_response_text(response_text)

print("\n✅ Response received:")
print(response_text)

pyperclip.copy(response_text)
print("\n📋 The response has been copied to your clipboard. ✅")
    
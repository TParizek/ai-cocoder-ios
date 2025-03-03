import sys
from command_type import CommandType

def fix_whitespace(input_text):
    lines = input_text.splitlines()
    non_comment_lines = [line for line in lines if not line.strip().startswith("///")]
    if len(non_comment_lines) > 1:
        base_indent = len(non_comment_lines[0]) - len(non_comment_lines[0].lstrip())
    else:
        base_indent = 0
    
    cleaned_lines = [lines[0]] + [line[base_indent:] if len(line) > base_indent else line.lstrip() for line in lines[1:]]
    return "\n".join(cleaned_lines)

def format_response_text(response_text):
    start_marker = "```swift"
    end_marker = "```"
    start_index = response_text.find(start_marker)
    end_index = response_text.find(end_marker, start_index + len(start_marker))
    if start_index != -1 and end_index != -1:
        response_text = response_text[start_index + len(start_marker):end_index].strip()
        response_text = fix_whitespace(response_text)
        return response_text
    else:
        return response_text

def make_prompt(code, command_type):
    if command_type == CommandType.DOCUMENT:
        return f"""
        You are an expert iOS engineer with deep knowledge of Swift.

        Your ONLY task is to add **documentation comments (`///`)** to the provided Swift code.

        Here is the Swift code that needs documentation:

        ```swift
        {code}
        ```
        """
    elif command_type == CommandType.UNIT_TEST:
        return f"""
        You are an expert iOS engineer with deep knowledge of Swift.

        Your ONLY task is to write unit tests for provided Swift code.

        Here is the Swift code that needs testing:

        ```swift
        {code}
        ```
        """
    elif command_type == CommandType.REFACTORING:
        return f"""
        You are an expert iOS engineer with deep knowledge of Swift.

        Your ONLY task is to refactor provided Swift code according to the best practices.

        Here is the Swift code that needs refactoring:

        ```swift
        {code}
        ```
        """
    else:
        print("Invalid option. Exiting.")
        sys.exit(1)
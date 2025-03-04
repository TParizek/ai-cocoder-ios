# 🤖 Swift CoCoder

A Python script for Swift code generation.

## Installation

**Prerequisites:**

- Python (3.11 recommended)
- pip3
- huggingface_hub CLI

**Install Dependencies:**

`pip3 install -r requirements.txt`

Download AI Model:

`huggingface-cli download deepseek-ai/deepseek-coder-6.7b-instruct.Q4_K_M.gguf --local-dir ./`

## Usage

`python3 app.py`

## TODOs

- [ ] Optimize the prompt to increase quality of generated code

- [ ] Fine tune train the deepseek coder model ([link](https://github.com/deepseek-ai/DeepSeek-Coder?tab=readme-ov-file#5-how-to-fine-tune-deepseek-coder))

## License

MIT License.


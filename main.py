import openai
from openai.error import APIConnectionError, APIError, RateLimitError
from typing import List, Dict, Generator, Optional

import tiktoken
import pandas as pd
from dotenv import load_dotenv
import sys

import re
import random
import time
import praw
import os

import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display


# targetPersonals is an array of targets (needs to be looped)
targetPersonals = os.environ["TARGETS"];


print("Has error module:", hasattr(openai, 'error'))

if hasattr(openai, 'error'):
    print("Has APIConnectionError:", hasattr(openai.error, 'APIConnectionError'))
    print("Has APIError:", hasattr(openai.error, 'APIError'))
    print("Has RateLimitError:", hasattr(openai.error, 'RateLimitError'))


model = "gpt4-turbo"
load_dotenv(".env")

openai.api_key = os.environ["OPENAI_API_KEY"]

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=f"script:test:0.0.1 (by u/yourusername)",
)

def num_tokens_from_messages(messages, model):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        return num_tokens_from_messages(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens
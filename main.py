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



print("Has error module:", hasattr(openai, 'error'))

if hasattr(openai, 'error'):
    print("Has APIConnectionError:", hasattr(openai.error, 'APIConnectionError'))
    print("Has APIError:", hasattr(openai.error, 'APIError'))
    print("Has RateLimitError:", hasattr(openai.error, 'RateLimitError'))


model = "gpt-3.5-turbo"
load_dotenv(".env")

openai.api_key = os.environ["OPENAI_API_KEY"]

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=f"script:test:0.0.1 (by u/yourusername)",
)
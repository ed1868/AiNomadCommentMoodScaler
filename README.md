# Reddit Sentiment Analysis

## Overview
This project performs sentiment analysis on comments from various subreddits. It uses OpenAI's GPT models for sentiment scoring and PRAW (Python Reddit API Wrapper) for fetching Reddit data. The primary goal is to score comments on a scale from -1 to 1, indicating their overall sentiment.

## Features
- Fetches top comments from specified subreddits.
- Utilizes OpenAI's GPT models for sentiment analysis.
- Handles API errors and rate limits.
- Estimates token usage for sentiment analysis tasks.
- Caches results in a CSV file.
- Visualizes sentiment scores using Seaborn and Matplotlib.

## Requirements
- Python 3.x
- OpenAI API key
- PRAW (Python Reddit API Wrapper)
- Pandas
- Seaborn and Matplotlib for data visualization
- TikToken for encoding
- Dotenv for environment variable management

## Installation
1. Clone the repository to your local machine.
2. Install the required packages:
   ```bash
   pip install openai praw pandas seaborn matplotlib tiktoken python-dotenv


## Usage
1. Set the target subreddits in the .env file.
2. Run the main script:
   ```bash
   python main.py

The script will fetch comments, perform sentiment analysis, and save the results in a CSV file. It will also generate visualizations of the sentiment scores.

## Configuration

Modify the targetPersonas variable to analyze different subreddits.
Adjust constants like NUM_SUBREDDITS, TARGET_COMMENTS_PER_SUBREDDIT, and MAX_COMMENT_LENGTH as needed.

## Functions

collect_comments: Collects comments from Reddit and stores them in a DataFrame.
score_sentiments: Scores the sentiment of collected comments.
plot_sentiments: Generates sentiment score plots for each subreddit.

## Error Handling

Handles common errors such as APIConnectionError, APIError, and RateLimitError.
Implements retries for robust error handling.

## Visualization

Uses Seaborn and Matplotlib to create KDE plots of sentiment scores across different subreddits.

## Notes

Ensure you have appropriate API keys and credentials set in your environment variables.
The script is configured to fetch comments from the top posts of the month in each subreddit.

## License
This project is open-sourced under the MIT License.
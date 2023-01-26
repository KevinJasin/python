import praw
import sys
import os

reddit = praw.Reddit(
    client_id="C0-aUFUQiC58MZ4C2X-avA",
    client_secret="TH-9VeO1iYuNG7FTRy2ubQCbPQYtCA",
    user_agent="python:C0-aUFUQiC58MZ4C2X-avA:v1 (by u/jikroy0)",
)

current = os.path.dirname(os.path.realpath(_file_))
parent = os.path.dirname(current)
sys.path.append(parent)

from yl27_config import yl27_config

reddit = praw.Reddit(
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    user_agent = config["user_agent"]
)


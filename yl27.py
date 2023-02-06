import praw
import sys
import os

current = os.path.dirname(os.path.realpath(_file_))
parent = os.path.dirname(current)
sys.path.append(parent)

from yl27_config import yl27_config

reddit = praw.Reddit(
    client_id = config["client_id"],
    client_secret = config["client_secret"],
    user_agent = config["user_agent"],
)


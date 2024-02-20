#Import modules
#--------------------------------------
import praw #to access Reddit
import requests #Might not need this
from praw.models import MoreComments #access Reddit comments
import sys #for .translate bmp code
import regex #regex matching
import datetime #converting timestamps
import csv

#Assign Reddit Credentials
#---------------------------------------
r = praw.Reddit(client_id='***', #feel it with your information
                     client_secret='***', #feel it with your information
                     password='***', #feel it with your information
                     user_agent='**',#feel it with your information
                     username='***')#feel it with your information

print("Credentials have been accepted")

subreddit_name = 'sports'

subreddit = r.subreddit(subreddit_name)

sampled_comments = []
count_sampled_comments =0
def is_valid_word(word):
    return len(word) >= 3

# Get comments from the subreddit until we have 100 comments
for comment in subreddit.comments(limit=None):
    # Split the comment into words
    words = comment.body.split()
    # Check if the comment body is not empty and has at least 5 words
    if comment.body and len(words) >= 5:
        # Check if each word in the comment has a length of at least 3 characters
        if all(is_valid_word(word) for word in words):
            # Append the comment body to the sampled_comments list
            sampled_comments.append(comment.body)
            count_sampled_comments += 1



# Shuffle the sampled comments to ensure randomness
random.shuffle(sampled_comments)

# Print the sampled comments
for i, comment in enumerate(sampled_comments):
    print(f"{i+1}. {comment}")


# Write the sampled comments to a CSV file
with open("100_sampled_comments_from_sports.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(["Comments"])
    # Write the comments
    for comment in sampled_comments:
        writer.writerow([comment])

print("Comments have been saved to '100_sampled_comments_from_sports.csv'")

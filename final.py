#group to comments by email, count comments.
# save to comments.csv.

import requests
import pandas as pd
try:
    response = requests.get("https://jsonplaceholder.typicode.com/comments")

#checks for error API
    response.raise_for_status()

#converts JSON format comments into python
    data = response.json()

# converts the python data into data frames 
    df = pd.DataFrame(data)


    comments_counts = df.groupby("email")["id"].count().reset_index(name="comment_count")
    comments_counts.to_csv("comments.csv")
except Exception as e:
    print("An error has occured:",e)
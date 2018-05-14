# Transforming Data with Python Scripts
### •To analyze the following questions in the articles from Hacker News, compiled in the provided dataset with command line scripts:
••What words appear most often in the headlines?  
••What domains were submitted most often to Hacker News?  
••At what times are the most articles submitted?

# Installation
•Clone this repo to your computer.  
•Install the requirements using pip install -r requirements.txt.  
•Make sure you use Python 3.  
•OPTIONAL: original dataset available [here](https://github.com/arnauddri/hn)

# Usage
•Run "read.py" from the command line or IDE of your choice to read the dataset into a Pandas Dataframe.  
•Run "count.py" from the command line or IDE to see which words appear most often in the headlines.  
•Run "domains.py" from the command line or IDE to explore which domains were submitted most often.  
•Run "times.py" from the command line or IDE to see what hour of the day most articles are submitted.

# Tasks Performed
### •Wrote script containing a function to read CSV to Pandas Dataframe & added column. names.
### •Wrote script containing a function to return words that appear most often.
••Combined headlines into a single string.  
••Split string into list of words.  
••Used collections.Counter() method to return the most common words.
### •Wrote script containing a function to return most submitted domains.
••Used Pandas value_counts method to count the number of occurrences of each value in the 'url' column.
### •Wrote script containing a function to determine when most articles are submitted.
••Converted time column to Pandas Datetime format.  
••Extracted hour using Pandas dataframe.dt.hour method.  
••Applied value_counts() method to return the hours of the day with the most submissions.

# Next Steps
•What headline length leads to the most upvotes?  
•What submission time leads to the most upvotes?  
•How are the total numbers of upvotes changing over time?

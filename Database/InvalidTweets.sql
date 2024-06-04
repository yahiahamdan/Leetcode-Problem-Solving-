#invalid tweets tweets having content length less than 25 characters
select tweet_id from Tweets where Char_Length(content)> 25

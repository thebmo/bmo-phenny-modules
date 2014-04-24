bmo-phenny-modules
==================

modues I've added to the phenny irc bot framwork.

======
Notes:
======

youtube.py
----------
the Youtube module requires you to update the  client secrets and id strings with your own information. I will be including a seperate config class module (like the reddit posting file) in the near future.

reddit_post.py
--------------
update the class reddit\reddit/py with your own information. no alteration of the reddit_post.py file needed


============
Dependancies
============

youtube.py
----------
gdata (google data api - pip install gdata)

reddit_post.py
--------------
praw (reddit api wrapper - pip install praw)<br>
beautifulsoup4 (html parser - pip install beautifulsoup4)


#The Fool
##A tarot card game

##A bearly software game

To run unit tests: `python manage.py test --pattern="*Test*.py"`

To run server: `python manage.py runserver` 
(then browse to http://localhost:8000)

---------------------------------
To run docker image in local dev:
---------------------------------
`docker run -p 8000:8000 -v <FULL_PATH_TO_CODE_DIRECTORY>:/app/ cbanisi/the-fool`


[<img src="https://travis-ci.org/bearly-software/the-fool.svg?branch=master">](https://travis-ci.org/bearly-software/the-fool)

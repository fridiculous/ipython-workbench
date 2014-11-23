personal ipython workbench
=========

Contains scripts, utility librarys and packages that I'm commonly using for datascience and analytics

This is made for python3


## Installation

local installation for mac os 10.9+

```
git clone 
```

### Prereqs

```
# make sure python 2 is upto date
brew update
brew upgrade python
pip install virtualenv --upgrade
pip install virtualenvwrapper --upgrade
```

```
# install python3 and make virtual environment called 'data3'
brew install python3
mkvirtualenv -p /usr/local/bin/python3 data3
workon data3
```

```
#install packages
pip install -r requirements.txt
```


## Usage


connecting to a postgres database
```
from connect_to_db import ConnectToDB
cdb = ConnectToDB()

df = cdb.get_query('SELECT * FROM users LIMIT 10')
```

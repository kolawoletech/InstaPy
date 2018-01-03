

```bash
1. git clone https://github.com/kolwoletech/InstaPy.git
2. cd InstaPy
3. pip install .
or
3. python setup.py install
```
4. Download ```chromedriver``` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). And put it in ```/assets``` folder.

### Set it up yourself with this Basic Setup

Basic setup is a good way to test the tool. At project root folder open `quickstart.py` and update with your username and password.

```python
from instapy import InstaPy

insta_username = ''
insta_password = ''

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
session.set_upper_follower_count(limit=2500)
session.set_do_comment(True, percentage=10)
session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['pizza', 'girl'])

# do the actual liking
session.like_by_tags(['natgeo', 'world'], amount=100)

# end the bot session
session.end()
```

Execute it:

```bash
$ python quickstart.py
```


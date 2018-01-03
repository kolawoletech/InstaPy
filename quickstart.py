from instapy import InstaPy

session = InstaPy(username='kolawolegolulana', password='1instagramone')

session.login()

session.set_dont_like(['nsfw', 'sex','girl'])
session.set_ignore_users(['max'])
session.set_do_follow(enabled=True, percentage=10, times=1)
session.set_do_comment(enabled=True, percentage=10)
session.set_comments(['Nice'], media=None)
session.like_by_tags(['tech'], amount=10, media=None)
session.like_from_image(['www.instagram.com/max'], amount=2, media=None)

session.end()
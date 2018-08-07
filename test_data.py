#!/usr/bin/env python3

"""
Usage:
BEFORE you run this initiall, create a superuser:
python manage.py createsuperuser

To run this you must first start a django shell:
python manage.py shell
Once the shell is up, go:
run ./test_data.py
It will silently populate the database.
"""

from myblog.models import Post
from django.contrib.auth.models import User


p1 = Post(title='My First Post', text='This is the first post I\'ve written')
all_users = User.objects.all()


p1.author = all_users[0]
p1.full_clean()
p1.save()

p1.title = p1.title + " (updated)"
p1.save()

p2 = Post(title="Another post",
           text="The second one created",
           author=all_users[0]).save()
p3 = Post(title="The third one",
          text="With the word 'heffalump'",
          author=all_users[0]).save()
p4 = Post(title="Posters are a great decoration",
          text="When you are a poor college student",
          author=all_users[0]).save()


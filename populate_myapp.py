from faker import Faker
import random
import os
from myapp.models import Topic, Webpage, AccessRecord
import django


# Configure settings for project
# Need to run this before calling models from application!
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
# Import settings


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new Webpage Entry
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')


# from faker import Faker
# from myapp.models import Topic, Webpage, AccessRecord
# import random
# import django
# import os
# # os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# # django.setup()
# # from django.core.management import setup_environ
# # import sys

# # from accesscharter import settings


# # setup_environ(settings)
# # os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# # settings.configure()

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
# django.setup()

# # Fake pop script

# fakegen = Faker()
# topic = ['Search', 'socail', 'MarketPlace', 'News', 'Games']


# def add_topic():
#     t = Topics.object.get_or_create(top_name=random.choices(topic))[0]
#     t.save()
#     return t


# def populate(N=5):
#     for entry in range(5):
#         # get topic
#         top = add_topic()
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#         webpg = Webpage.object.get_or_create(
#             topic=top, url=fake_url, name=fake_name)[0]
#         acc_rec = AccessRecord.object.get_or_create(
#             name=webpg, date=fake_date)[0]


# if __name__ == '__main__':
#     print("populate script!")
#     populate(20)
#     print("population compleate")

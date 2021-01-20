from django.core.management.base import BaseCommand, CommandError
import json
import requests
from blog.models import Post , User

class Command(BaseCommand):
    help = 'used for inserting dummy data'

    def handle(self, *args, **options):
        base_url = 'https://jsonplaceholder.typicode.com/users/'
        response = requests.get(base_url)
        data = json.loads(response.text)
        for value in data:
           b = User(name = value['name'],email = value['email'] , address = "{}, {}, {}, {}".format(value['address']['street'],value['address']['suite'],value['address']['city'],value['address']['zipcode']),phone = value['phone'] , website = value['website']  )
           b.save()

        for i in range(1,11):
            url = base_url+str(i)+'/posts'
            response = requests.get(url)
            post_data = json.loads(response.text)
            for value in post_data:
                author = User.objects.get(id=value['userId'])
                post = Post(title=value['title'],author=author,body=value['body'])
                post.save()

import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten

from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    
    help = 'This command creates fake users'
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help='How many users do you want to create?'
        )

    def handle(self, *args, **options):
        number = int(options.get('number'))
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            'price': lambda x: random.randint(0, 300),
            'guests': lambda x: random.randint(0, 10), 
            'beds': lambda x: random.randint(0, 5), 
            'bedrooms': lambda x: random.randint(0, 5), 
            'bath': lambda x: random.randint(0, 5), 
            
        })

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))

        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room_instance = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room_instance,
                    file=f'room_photos/{random.randint(1, 31)}.webp',
                )
            
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.house_rules.add(r)



        self.stdout.write(self.style.SUCCESS(f'{number} Users create'))
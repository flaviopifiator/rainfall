import factory
from faker import Factory

from .models import Floor, Rain


faker = Factory.create()


class FloorFactory(factory.django.DjangoModelFactory):
    id = factory.Sequence(lambda n: n + 1)
    hectares = faker.pydecimal(min_value=100, max_value=20000)

    class Meta:
        model = Floor


class RainFactory(factory.django.DjangoModelFactory):
    id = factory.Sequence(lambda n: n + 1)
    floor = factory.SubFactory(FloorFactory)

    class Meta:
        model = Rain

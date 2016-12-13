import factory
from faker import Factory
fake = Factory.create()

from django.contrib.auth.hashers import make_password

from .models import User


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    @factory.lazy_attribute
    def password(self):
        return make_password('qwerty')

    @factory.lazy_attribute
    def email(self):
        return fake.safe_email()

    @factory.lazy_attribute
    def name(self):
        return fake.name()


class AdminFactory(UserFactory):
    email = 'admin@example.com'
    password = make_password('admin')
    is_staff = True
    is_active = True
    is_superuser = True


def generate_users():
    AdminFactory()
    UserFactory.create_batch(10)

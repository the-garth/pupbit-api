from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Pet

# Create your tests here.


class PetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

        cls.pet = Pet.objects.create(
            name='Buddy',
            owner=cls.user,
            breed='Golden Retriever',
            date_of_birth='2020-01-01',
            weight_kg=30.5,
            sex='Male',
            color='Golden',
        )

    def test_pet_model(self):
        self.assertEqual(self.pet.name, 'Buddy')
        self.assertEqual(self.pet.owner.username, 'testuser')
        self.assertEqual(self.pet.breed, 'Golden Retriever')
        self.assertEqual(str(self.pet.date_of_birth), '2020-01-01')
        self.assertEqual(self.pet.weight_kg, 30.5)
        self.assertEqual(self.pet.sex, 'Male')
        self.assertEqual(self.pet.color, 'Golden')

from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from .models import Product, Box
from .services import can_fit


class BoxSelectionTest(TestCase):

    def test_product_fits_box(self):

        product_dimensions = (
            10,
            20,
            5
        )

        box_dimensions = (
            20,
            10,
            10
        )

        result = can_fit(
            product_dimensions,
            box_dimensions
        )

        self.assertTrue(result)


    def test_product_does_not_fit_box(self):

        product_dimensions = (
            50,
            50,
            50
        )

        box_dimensions = (
            20,
            20,
            20
        )

        result = can_fit(
            product_dimensions,
            box_dimensions
        )

        self.assertFalse(result)
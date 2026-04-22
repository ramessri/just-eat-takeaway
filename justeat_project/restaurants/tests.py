from unittest.mock import patch, MagicMock

import json
from pathlib import Path
import requests

from django.test import TestCase
from django.urls import reverse

from restaurants.services import get_restaurants


class GetRestaurantsServiceTests(TestCase):
    """Tests for the get_restaurants service function."""

    def setUp(self):
        """Load the fixture file once for use in tests."""
        fixture_path = Path(__file__).parent / "fixtures" / "sample_response.json"
        with open(fixture_path) as f:
            self.sample_response = json.load(f)

    @patch("restaurants.services.requests.get")
    def test_returns_cleaned_restaurant_dicts(self, mock_get):
        # Arrange: make requests.get return a fake response with our fixture
        mock_response = MagicMock()
        mock_response.json.return_value = self.sample_response
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Act
        result = get_restaurants("EC4M7RF")

        # Assert
        self.assertEqual(len(result), 10)
        self.assertIn("name", result[0])
        self.assertIn("cuisines", result[0])
        self.assertIn("rating", result[0])
        self.assertIn("address", result[0])
        self.assertIsInstance(result[0]["cuisines"], list)
        self.assertIsInstance(result[0]["rating"], (int, float))

    @patch("restaurants.services.requests.get")
    def test_returns_empty_list_on_request_exception(self, mock_get):
        # Arrange: make requests.get raise a timeout
        mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")

        # Act
        result = get_restaurants("EC4M7RF")

        # Assert
        self.assertEqual(result, [])

class RestaurantListViewTests(TestCase):
    """Tests for the restaurant_list view."""

    def test_get_renders_form(self):
        url = reverse("restaurant_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")
        self.assertContains(response, "Postcode")

    @patch("restaurants.views.get_restaurants")
    def test_post_with_valid_postcode_shows_results(self, mock_service):
        # Arrange: make the service return fake restaurants
        mock_service.return_value = [
            {
                "name": "Test Pizza Place",
                "cuisines": ["Italian", "Pizza"],
                "rating": 5,
                "address": "1 Test Street",
                "city": "London",
                "postalCode": "EC4M 7RF",
            }
        ]

        # Act
        url = reverse("restaurant_list")
        response = self.client.post(url, {"postcode": "EC4M7RF"})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Pizza Place")
        self.assertContains(response, "Italian")
        mock_service.assert_called_once_with("EC4M7RF")


    @patch("restaurants.views.get_restaurants")
    def test_post_with_invalid_postcode_shows_error(self, mock_service):
        url = reverse("restaurant_list")
        response = self.client.post(url, {"postcode": "ZZZ"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid UK postcode")
        mock_service.assert_not_called()    
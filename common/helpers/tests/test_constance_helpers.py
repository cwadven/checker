from unittest.mock import patch

from common.dtos.helper_dtos import (
    ConstanceDetailType,
    ConstanceType,
)
from common.helpers.constance_helpers import (
    CONSTANCE_TYPE_HELPER_MAPPER,
    ConstanceDetailTypeHelper,
    ConstanceTypeHelper,
)
from django.test import TestCase


class ConstanceTypeHelperTest(TestCase):
    def test_constance_type_helper(self):
        # Given: Set up the test data
        # Expected: Assert the result
        with self.assertRaises(NotImplementedError):
            ConstanceTypeHelper().get_constance_types()


class ConstanceDetailTypeHelperTest(TestCase):
    def test_constance_detail_type_helper(self):
        # Given: Set up the test data
        # Expected: Assert the result
        with self.assertRaises(NotImplementedError):
            ConstanceDetailTypeHelper().get_constance_detail_types()

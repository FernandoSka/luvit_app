from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def min_value_validator(value):
    if value < 0:
        raise ValidationError(
            _('The value should be up to 0'),
            params={'value': value},
        )

def min_name_length_validator(value):
    if not 3 < len(value) < 55:
        raise ValidationError(
            _('The product name should have characters between 3 and 55'),
            params={
                'value': value,
                'length': len(value)
            },
        )


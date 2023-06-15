from django.core.exceptions import ValidationError


def validate_par(value):
    if value % 2 != 0:
        raise ValidationError(
            "%(value)s no es un número par",
            params={"value": value},
        )

from rest_framework import serializers
from django.core.exceptions import ValidationError


def validate_bool(value):
    if value not in (0, 1):
        raise serializers.ValidationError("This field accepts only 0 or 1")


def validate_negative(value):
    if value > 0:
        raise serializers.ValidationError("This field must be negative (e.g., days before current date)")


class ModelPoolsSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    OWN_CAR_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    OWN_REALTY_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    INCOME_CHOICES = (
        ('Working', 'Working'),
        ('Commercial associate', 'Commercial associate'),
        ('Pensioner', 'Pensioner'),
        ('State servant', 'State servant'),
        ('Student', 'Student')
    )
    EDUCATION_CHOICES = (
        ('Secondary / secondary special', 'Secondary / secondary special'),
        ('Higher education', 'Higher education'),
        ('Incomplete higher', 'Incomplete higher'),
        ('Lower secondary', 'Lower secondary'),
        ('Academic degree', 'Academic degree')
    )
    FAMILY_CHOICES = (
        ('Married', 'Married'),
        ('Single / not married', 'Single / not married'),
        ('Civil marriage', 'Civil marriage'),
        ('Separated', 'Separated'),
        ('Widow', 'Widow')
    )
    HOUSING_CHOICES = (
        ('House / apartment', 'House / apartment'),
        ('With parents', 'With parents'),
        ('Municipal apartment', 'Municipal apartment'),
        ('Rented apartment', 'Rented apartment'),
        ('Office apartment', 'Office apartment'),
        ('Co-op apartment', 'Co-op apartment')
    )
    OCCUPATION_CHOICES = (
        ('Laborers', 'Laborers'),
        ('Core staff', 'Core staff'),
        ('Sales staff', 'Sales staff'),
        ('Managers', 'Managers'),
        ('Drivers', 'Drivers'),
        ('High skill tech staff', 'High skill tech staff'),
        ('Accountants', 'Accountants'),
        ('Medicine staff', 'Medicine staff'),
        ('Cooking staff', 'Cooking staff'),
        ('Security staff', 'Security staff'),
        ('Cleaning staff', 'Cleaning staff'),
        ('Private service staff', 'Private service staff'),
        ('Low-skill Laborers', 'Low-skill Laborers'),
        ('Waiters/barmen staff', 'Waiters/barmen staff'),
        ('Secretaries', 'Secretaries'),
        ('HR staff', 'HR staff'),
        ('Realty agents', 'Realty agents'),
        ('IT staff', 'IT staff')
    )

    code_gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    flag_own_car = serializers.ChoiceField(choices=OWN_CAR_CHOICES)
    flag_own_realty = serializers.ChoiceField(choices=OWN_REALTY_CHOICES)
    name_income_type = serializers.ChoiceField(choices=INCOME_CHOICES)
    name_education_type = serializers.ChoiceField(choices=EDUCATION_CHOICES)
    name_family_status = serializers.ChoiceField(choices=FAMILY_CHOICES)
    name_housing_type = serializers.ChoiceField(choices=HOUSING_CHOICES)
    occupation_type = serializers.ChoiceField(choices=OCCUPATION_CHOICES)

    amt_income_total = serializers.IntegerField()
    cnt_children = serializers.IntegerField()
    cnt_fam_members = serializers.IntegerField()
    days_employed = serializers.IntegerField(validators=[validate_negative])
    days_birth = serializers.IntegerField(validators=[validate_negative])

    flag_mobil = serializers.IntegerField(validators=[validate_bool])
    flag_work_phone = serializers.IntegerField(validators=[validate_bool])
    flag_phone = serializers.IntegerField(validators=[validate_bool])
    flag_email = serializers.IntegerField(validators=[validate_bool])





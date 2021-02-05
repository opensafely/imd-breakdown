from datetime import date
from cohortextractor import StudyDefinition, patients


today = str(date.today())


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
    },
    population=patients.registered_as_of(today),
    imd=patients.address_as_of(
        today,
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "incidence": 0.8,
            "category": {"ratios": {100 * (n + 1): 1 / 330 for n in range(330)}},
        },
    ),
)

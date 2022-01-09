import csv

from django.core.management import BaseCommand
from mydiaryapp.models import Patient


class Command(BaseCommand):
    help = "loading dead souls from csv"

    def handle(self, *args, **options):
        with open('test-data-set-10000.csv', "r", encoding='utf-8') as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            patients = []

            for row in data:
                patient = Patient(
                patientId=row[0],
                fullName=row[1],
                birthDate=row[2],
                policy=row[3],
                lpuId=12345
                )

                patients.append(patient)
                if len(patients)>1000:
                    print(len(patients))
                    Patient.objects.bulk_create(patients)
                    patients = []
            print('Мертвые души добавлены')
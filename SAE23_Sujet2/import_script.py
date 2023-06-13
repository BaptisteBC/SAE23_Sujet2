import csv
from filmographie.models import Categorie  # replace myapp with your app name

# First, load the marque data.
with open('media/import_categorie_2.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='/')
    next(reader)  # This skips the first row of the CSV file.
    for row in reader:
        _, created = Categorie.objects.get_or_create(
            nom=row[0],
            descriptif=row[1],
        )
'''
# Then, load the auto data.
with open('relation/data/auto.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # This skips the first row of the CSV file.
    for row in reader:
        # Find the corresponding marque instance.
        marque_instance = marque.objects.get(nom=row[2])
        _, created = auto.objects.get_or_create(
            nom=row[0],
            puissance=row[1],
            marque=marque_instance
        )'''
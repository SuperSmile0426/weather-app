import csv
import json

with open('src/country-capital-lat-long-population.csv', 'r') as file:
    reader = csv.DictReader(file)

    fields_to_select = ['Capital City', 'Latitude', 'Longitude']

    hard_data = []

    for row in reader:
        try:
            selected_data = {field: row[field] for field in fields_to_select}
            hard_data.append(selected_data)

        except KeyError as e:
            print(f"Error processing row: {row}, {e}")

# hard_data = json.dumps(data)



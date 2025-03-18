import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_in:
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
            reader = csv.reader(csv_in)
            writer = csv.writer(csv_out)

            for row in reader:
                # Remove quotes, newline characters, apostrophes
                new_row = [field.replace('"', '').replace('\n', '').replace('\r', '').replace("'", "") for field in row]
                writer.writerow(new_row)

clean_csv('stratified_sample.csv', 'cleaned.csv')




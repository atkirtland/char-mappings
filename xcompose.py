import csv

def generate_xcompose(csv_file, output_file):
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, "w", encoding="utf-8") as xcompose:
            xcompose.write("# for Emacs: -*- coding: utf-8 -*-\n")
            xcompose.write("# Auto-generated .XCompose\n\n")
            xcompose.write('include "%L"\n\n')
            for row in reader:
                unicode_char = row["unicode"]
                compose_seq = row["compose"]
                if unicode_char and compose_seq:
                    xcompose.write(f'{compose_seq} : "{unicode_char}"\n')

generate_xcompose("mappings.csv", ".XCompose")

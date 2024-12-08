import csv

def generate_unicode_tex(csv_file, output_file):
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, "w", encoding="utf-8") as unicode_tex:
            unicode_tex.write("% Auto-generated unicode.tex\n\n")
            for row in reader:
                codepoint = row["codepoint"][1:]
                latex = row["latex"]
                if codepoint and latex:
                    unicode_tex.write(
                        f"\\DeclareUnicodeCharacter{{{codepoint}}}{{{latex}}}\n"
                    )

generate_unicode_tex("mappings.csv", "unicode.tex")

import csv
import re

def generate_vim_script(csv_file, output_file):
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, "w", encoding="utf-8") as vim_script:
            vim_script.write('" Auto-generated unicode_to_latex.vim\n')
            vim_script.write("cmap <C-c> <Esc>:qa!<CR>\n\n")
            for row in reader:
                unicode_char = row["unicode"]
                latex = row["latex"]
                if unicode_char and latex:
                    escaped_latex = re.escape(latex)
                    vim_script.write(f"silent! %s/{unicode_char}/{escaped_latex}/gc\n")

generate_vim_script("mappings.csv", "unicode_to_latex.vim")

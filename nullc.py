import os
import re
import sys

sifra_dict = {
    "auto": "auto", "break": "break", "case": "case", "char": "char",
    "const": "const", "continue": "continue", "default": "default",
    "do": "do", "double": "double", "else": "else", "enum": "enum",
    "extern": "extern", "float": "float", "for": "for", "goto": "goto",
    "if": "if", "inline": "inline", "int": "int", "long": "long",
    "register": "register", "restrict": "restrict", "return": "return",
    "short": "short", "signed": "signed", "sizeof": "sizeof",
    "static": "static", "struct": "struct", "switch": "switch",
    "typedef": "typedef", "union": "union", "unsigned": "unsigned",
    "void": "void", "volatile": "volatile", "while": "while",
    "out": "printf", "in": "scanf", "def": "define",
    "string": "snprintf", "sys": "system", "fout": "fprintf",
    "fin": "fscanf"
}

def replace_tokens(line: str) -> str:
    for token, replacement in sifra_dict.items():
        line = re.sub(rf'\b{re.escape(token)}\b', replacement, line)
    return line

def process_code(code: str) -> str:
    result_lines = []
    for line in code.splitlines():
        if line.strip().startswith("#include"):
            result_lines.append(line)
        else:
            new_line = replace_tokens(line)
            result_lines.append(new_line)
    return "\n".join(result_lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: nullc.py <filename>")
        sys.exit(1)
    filename = sys.argv[1].strip()
    in_file = filename
    out_dir = os.path.expanduser("~/.nullc")
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(in_file):
        print(f"❌ File '{in_file}' not found.")
        return

    with open(in_file, "r") as f:
        code = f.read()

    translated = process_code(code)

    with open("program.c", "w") as f:
        f.write(translated)

    with open(os.path.join(out_dir, "filenames.txt"), "w") as f:
        f.write(filename)


if __name__ == "__main__":
    main()


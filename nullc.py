import os
import re

# Token-based keyword mapping
sifra_dict = {
    "auto": "auto",
    "break": "break",
    "case": "case",
    "char": "char",
    "const": "const",
    "continue": "continue",
    "default": "default",
    "do": "do",
    "double": "double",
    "else": "else",
    "enum": "enum",
    "extern": "extern",
    "float": "float",
    "for": "for",
    "goto": "goto",
    "if": "if",
    "inline": "inline",
    "int": "int",
    "long": "long",
    "register": "register",
    "restrict": "restrict",
    "return": "return",
    "short": "short",
    "signed": "signed",
    "sizeof": "sizeof",
    "static": "static",
    "struct": "struct",
    "switch": "switch",
    "typedef": "typedef",
    "union": "union",
    "unsigned": "unsigned",
    "void": "void",
    "volatile": "volatile",
    "while": "while",
    "include": "include",
    "main": "main",
    "#include": "#include",
    "#def": "#define",
    "def": "define",
    "in": "scanf",

    # Custom language features
    "out": "printf",        # allows `out("Hello");`
    "string": "snprintf"    # can define your own behavior
}

def replace_tokens(code):
    for sifra, word in sifra_dict.items():
        # Replace whole words only (no part of another identifier)
        code = re.sub(rf'\b{re.escape(sifra)}\b', word, code)
    return code

def main():
    x = input("Filename (without .nc): ").strip()

    in_file = x + ".nc"
    out_dir = os.path.expanduser("~/.nullc")
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(in_file):
        print(f"❌ File '{in_file}' not found.")
        return

    with open(in_file, "r") as f:
        code = f.read()

    translated = replace_tokens(code)

    out_c_file = "program.c"
    with open(out_c_file, "w") as f:
        f.write(translated)

    with open(os.path.join(out_dir, "filenames.txt"), "w") as f:
        f.write(x)


if __name__ == "__main__":
    main()


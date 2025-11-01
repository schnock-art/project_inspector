import os, re, sys

class_pattern = re.compile(r'\b(class|interface|struct)\s+(\w+)')
method_pattern = re.compile(
    r'(public|private|protected|internal|static|virtual|override|\s)+\s+([\w<>\[\]]+)\s+(\w+)\s*\(([^)]*)\)'
)
summary_pattern = re.compile(r'///\s*<summary>\s*(.*?)\s*///\s*</summary>', re.DOTALL)

def extract_summaries(text):
    summaries = {}
    parts = re.split(r'(class|interface|struct)\s+\w+', text)
    # Dumb but effective: search above declarations for nearest <summary>
    for match in class_pattern.finditer(text):
        name = match.group(2)
        before = text[:match.start()]
        doc = extract_last_summary(before)
        if doc: summaries[name] = doc

    for match in method_pattern.finditer(text):
        name = match.group(3)
        before = text[:match.start()]
        doc = extract_last_summary(before)
        if doc: summaries[name] = doc

    return summaries

def extract_last_summary(text):
    matches = summary_pattern.findall(text)
    return matches[-1].strip() if matches else None

def print_tree(root, prefix=""):
    items = sorted(os.listdir(root))
    for i, item in enumerate(items):
        full = os.path.join(root, item)
        connector = "└── " if i == len(items)-1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(full):
            extension = "    " if i == len(items)-1 else "│   "
            print_tree(full, prefix + extension)

def scan_cs_file(path, md=False):
    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()

    summaries = extract_summaries(text)
    classes = class_pattern.findall(text)
    methods = method_pattern.findall(text)

    print(f"\n📄 {path}")
    for _, class_name in classes:
        doc = summaries.get(class_name, "")
        out = f"  🧩 class: {class_name}"
        if doc: out += f" — {doc}"
        print(out)

    for m in methods:
        modifiers, ret, name, params = m
        doc = summaries.get(name, "")
        print(f"    └─ 🛠 {modifiers.strip()} {ret} {name}({params})"
              + (f" — {doc}" if doc else ""))

def run(root):
    print("\n====== 📂 PROJECT TREE ======")
    print_tree(root)
    print("\n====== 🔍 C# CLASS + METHOD MAP ======")

    for dirpath, _, files in os.walk(root):
        for file in files:
            if file.endswith(".cs"):
                scan_cs_file(os.path.join(dirpath, file))

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    run(root)
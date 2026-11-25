import os

JOKE = "The office printer has jammed on every deadline this year, making it the most reliable thing in the building."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(JOKE)
os.chmod(path, 0o644)

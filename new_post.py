import os
from datetime import datetime
import subprocess

# --- Ask for inputs ---
title = input("Title: ").strip()
summary = input("Summary: ").strip()
tags = input("Tags (comma-separated): ").strip()
category = input("Category: ").strip()
date_input = input("Date (YYYY-MM-DD, blank for today): ").strip()

# --- Parse ---
date_obj = datetime.strptime(date_input, "%Y-%m-%d") if date_input else datetime.today()
date_str = date_obj.strftime("%Y-%m-%d")
year_str = date_obj.strftime("%Y")
slug = title.lower().replace(" ", "-")
base_path = os.path.join("content", "posts", year_str, slug)
os.makedirs(os.path.join(base_path, "images"), exist_ok=True)

# --- Markdown file ---
md_path = os.path.join(base_path, "index.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(f"""---
title: {title}
date: {date_str}
summary: {summary}
tags: [{tags}]
categories: [{category}]
---

# {title}

Start writing here...

![placeholder](images/placeholder.png)
""")

print(f"Created: {md_path}")

# --- Optionally open in Obsidian or system editor ---
try:
    subprocess.run(["kwrite", md_path])  # Linux
except Exception:
    pass

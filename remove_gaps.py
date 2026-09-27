import os
import re

files_to_fix = ['index.html', 'home2.html', 'custom-layouts.html']

for filename in files_to_fix:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove pt-20 from main tag
    content = content.replace('<main class="w-full pt-20 bg-surface">', '<main class="w-full bg-surface">')
    
    # 2. Remove -mt-20 from the first section (which is the hero section)
    # We can do this with regex for the first section only
    # Example match: <section class="relative min-h-[870px] flex items-center justify-center overflow-hidden -mt-20 pt-20">
    # Replace "-mt-20 " with ""
    # We only want to replace the first occurrence of -mt-20
    content = content.replace('-mt-20 ', '', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Removed gaps in {filename}")

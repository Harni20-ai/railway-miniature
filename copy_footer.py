import os
import re

def get_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<footer[^>]*>.*?</footer>', content, flags=re.DOTALL)
    if match:
        return match.group(0)
    return None

def replace_footer(filepath, new_footer):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace old footer with new footer
    new_content = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

footer = get_footer('home2.html')
if footer:
    files = ['index.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']
    for filename in files:
        if os.path.exists(filename):
            replace_footer(filename, footer)
            print(f"Replaced footer in {filename}")
        else:
            print(f"File not found: {filename}")
else:
    print("Could not find footer in home2.html")

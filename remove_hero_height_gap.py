import os

files_to_fix = ['index.html', 'home2.html', 'custom-layouts.html']

for filename in files_to_fix:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the massive min-height class which was causing the huge gap above the vertically-centered text
    content = content.replace('min-h-[870px] ', '')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Removed min-h-[870px] gap from {filename}")

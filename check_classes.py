import os
import re

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']
all_classes = set()

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all class="..." attributes
    matches = re.findall(r'class="([^"]+)"', content)
    for match in matches:
        for cls in match.split():
            if cls.startswith('text-') or cls.startswith('bg-') or cls.startswith('border-'):
                all_classes.add(cls)

# Filter out standard Tailwind classes like text-sm, text-center, text-white, border-t, bg-cover, bg-transparent
standard_classes = ['text-sm', 'text-md', 'text-lg', 'text-xl', 'text-2xl', 'text-3xl', 'text-4xl', 'text-[',
                    'text-center', 'text-left', 'text-right', 'text-white', 'text-black', 'text-transparent',
                    'bg-cover', 'bg-center', 'bg-no-repeat', 'bg-transparent', 'bg-white', 'bg-black',
                    'border-t', 'border-b', 'border-l', 'border-r', 'border-transparent', 'border-white', 'border-black']

custom_classes = set()
for cls in all_classes:
    is_standard = False
    for std in standard_classes:
        if cls.startswith(std):
            is_standard = True
            break
    if not is_standard:
        custom_classes.add(cls)

print("Potentially Missing Semantic Color Classes:")
for cls in sorted(custom_classes):
    print(cls)

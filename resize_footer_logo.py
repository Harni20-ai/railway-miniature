import os

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the h-6 class with h-10 for the footer logo to make it bigger
    content = content.replace(
        '<img alt="Iron &amp; Gauge Atelier Logo" class="h-6 w-auto object-contain"',
        '<img alt="Iron &amp; Gauge Atelier Logo" class="h-10 w-auto object-contain"'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Resized footer logo in {filename}")

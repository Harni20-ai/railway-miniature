import os

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact string in the header:
    # <div class="flex items-center gap-space-md"><img alt="Iron &amp; Gauge Atelier Logo" class="h-8 w-auto object-contain"
    
    # Let's find the header div and replace it with an 'a' tag.
    # It might be safer to use regex since the src might vary or be long.
    import re
    # Match: <div class="flex items-center gap-space-md"><img ... <span>Iron &amp; Gauge Atelier</span></div>
    
    pattern = re.compile(r'(<div[^>]*class="[^"]*flex items-center gap-space-md[^"]*"[^>]*>)(<img alt="Iron &amp; Gauge Atelier Logo" class="h-8 w-auto object-contain".*?<span class="text-headline-sm font-headline-sm tracking-tight text-on-surface">Iron &amp; Gauge Atelier</span>)(</div>)')
    
    def replacer(match):
        # We replace the opening <div> with an <a> tag
        old_div = match.group(1)
        inner_html = match.group(2)
        
        # Replace div with a, add href
        new_a = old_div.replace('<div', '<a href="index.html"').replace('class="', 'class="cursor-pointer hover:opacity-80 transition-opacity ')
        
        return new_a + inner_html + '</a>'
        
    content = pattern.sub(replacer, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Made logo clickable in {filename}")

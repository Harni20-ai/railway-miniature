import os
import re

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

logo_html = '<img alt="Iron &amp; Gauge Atelier Logo" class="h-6 w-auto object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuB3qEV6vnr8VlZfLl05S--QeurcSKvtHop_ZtVJgPxYmv9ODu_39fPUUwJBshP_ZH9wAVJpwVhXxXh2DrS0zOkC81LT0eOYEjP_t2UEHWgjnOs9Y7bs3I4fI2itfPBy5pTHQPh0x9GFBpqBwgjJtHpNBAcxrLDCuI34VpF9S1hlPszwLWubdLq5JKZujG4FnrT55sDw9o5LFLNB2HpIEYbZVq7LWIPKm3s4wcr5n258cyRLnMcc7NL_HA"/>'

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the logo block
    pattern_logo_block = r'<div class="flex items-center gap-space-sm"><span class="text-headline-sm font-headline-sm text-on-surface">The Miniature Railway Co\.</span></div>'
    replacement_logo_block = f'<div class="flex items-center gap-space-sm">{logo_html}<span class="text-headline-sm font-headline-sm text-on-surface">Iron &amp; Gauge Atelier</span></div>'
    content = re.sub(pattern_logo_block, replacement_logo_block, content)
    
    # Replace copyright (handles different encodings for the copyright symbol)
    pattern_copyright = r'<p>[^a-zA-Z0-9]*2026 The Miniature Railway Co\.\s*All rights reserved\.</p>'
    replacement_copyright = '<p>&copy; 2026 Iron &amp; Gauge Atelier. All rights reserved.</p>'
    content = re.sub(pattern_copyright, replacement_copyright, content)

    # Any remaining mentions of the old brand name
    content = content.replace('The Miniature Railway Co.', 'Iron & Gauge Atelier')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated branding in {filename}")

import os
import re

css = """
  /* Secondary Fixed text visibility override */
  html.dark .text-secondary-fixed { color: #ffffff !important; font-weight: 600 !important; }
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject right before </style> in the dark mode block if not already there
    if '/* Secondary Fixed text visibility override */' not in content:
        content = content.replace('</style>', css + '</style>', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed Bespoke Commission text in {filename}")

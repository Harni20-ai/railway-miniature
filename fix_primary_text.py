import os
import re

text_css = """
  /* Text vibrancy overrides */
  html.dark .text-primary { color: #ffb2bc !important; }
  html.dark .hover\\:text-primary:hover { color: #ffd9dd !important; }
  html.dark .text-secondary { color: #baeed9 !important; }
  html.dark .hover\\:text-secondary:hover { color: #ffffff !important; }
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject right before </style> in the dark mode block if not already there
    if '/* Text vibrancy overrides */' not in content:
        # Find the end of the dark mode style block
        parts = content.split('</style>')
        if len(parts) > 1:
            # We want to replace the FIRST occurrence which is our injected block
            # Actually, wait, just replace the first </style> since it's the one we added in the head
            content = content.replace('</style>', text_css + '</style>', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed red text visibility in {filename}")

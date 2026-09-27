import os
import re

tertiary_css = """
  /* Tertiary / Brown Text vibrancy overrides */
  html.dark .text-tertiary { color: #ffdea5 !important; }
  html.dark .text-tertiary-container { color: #ffdea5 !important; }
  html.dark .text-on-tertiary-container { color: #ffe6bd !important; }
  html.dark .text-tertiary-fixed { color: #ffdea5 !important; }
  html.dark .text-on-tertiary-fixed { color: #261900 !important; }
  html.dark .bg-tertiary-fixed { background-color: #ffdea5 !important; }
  html.dark .bg-tertiary-fixed-dim { background-color: #e9c176 !important; }
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject right before </style> in the dark mode block if not already there
    if '/* Tertiary / Brown Text vibrancy overrides */' not in content:
        content = content.replace('</style>', tertiary_css + '</style>', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed brown text visibility in {filename}")

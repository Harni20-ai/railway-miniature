import os
import re

css = """
  /* Gradient overrides for Surface (Fixes white washout gap at bottom of hero images) */
  html.dark .from-surface {
      --tw-gradient-from: #121212 var(--tw-gradient-from-position) !important;
      --tw-gradient-to: rgba(18, 18, 18, 0) var(--tw-gradient-to-position) !important;
      --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to) !important;
  }
  html.dark .via-surface\\/60 {
      --tw-gradient-to: rgba(18, 18, 18, 0)  var(--tw-gradient-to-position) !important;
      --tw-gradient-stops: var(--tw-gradient-from), rgba(18, 18, 18, 0.6) var(--tw-gradient-via-position), var(--tw-gradient-to) !important;
  }
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject right before </style> in the dark mode block if not already there
    if '/* Gradient overrides for Surface' not in content:
        content = content.replace('</style>', css + '</style>', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed surface gradient in {filename}")

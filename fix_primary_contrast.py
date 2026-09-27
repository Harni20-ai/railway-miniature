import os

css = """
  /* Fix contrast for text-primary when used inside bg-primary-fixed */
  html.dark .bg-primary-fixed.text-primary,
  html.dark .bg-primary-fixed .text-primary {
      color: #400013 !important; 
  }
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject right before </style> in the dark mode block if not already there
    if '/* Fix contrast for text-primary when used inside bg-primary-fixed */' not in content:
        content = content.replace('</style>', css + '</style>', 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed primary text contrast in {filename}")

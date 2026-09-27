import os
import re

dark_mode_css = """
<style id="dark-mode-overrides">
  html.dark .bg-surface { background-color: #1a1a1a !important; }
  html.dark .text-on-surface { color: #f5f5f5 !important; }
  html.dark .bg-surface-container-low { background-color: #121212 !important; }
  html.dark .bg-surface-container { background-color: #222222 !important; }
  html.dark .bg-surface-container-high { background-color: #2a2a2a !important; }
  html.dark .text-on-surface-variant { color: #bbbbbb !important; }
  html.dark .border-outline-variant { border-color: #333333 !important; }
  html.dark .border-outline-variant\\/30 { border-color: rgba(51,51,51,0.3) !important; }
  html.dark .bg-surface\\/80 { background-color: rgba(26,26,26,0.8) !important; }
  html.dark .hover\\:bg-surface-container-high:hover { background-color: #333 !important; }
  html.dark .hover\\:text-on-surface:hover { color: #ffffff !important; }
  html.dark .text-inverse-on-surface { color: #1a1a1a !important; }
  html.dark .bg-inverse-surface { background-color: #f5f5f5 !important; }
  html.dark .bg-background { background-color: #121212 !important; }
  html.dark .text-on-background { color: #f5f5f5 !important; }
</style>
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # If already injected, don't inject again
    if 'id="dark-mode-overrides"' not in content:
        content = content.replace('</head>', dark_mode_css + '</head>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added dark mode styles to {filename}")

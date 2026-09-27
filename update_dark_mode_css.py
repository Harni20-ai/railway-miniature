import os
import re

new_dark_mode_css = """
<style id="dark-mode-overrides">
  /* Dark mode overrides for semantic colors */
  html.dark .bg-surface { background-color: #121212 !important; }
  html.dark .text-on-surface { color: #e3e3e3 !important; }
  
  html.dark .bg-background { background-color: #121212 !important; }
  html.dark .text-on-background { color: #e3e3e3 !important; }
  
  html.dark .bg-surface-container-low { background-color: #1a1a1a !important; }
  html.dark .bg-surface-container { background-color: #212121 !important; }
  html.dark .bg-surface-container-high { background-color: #2b2b2b !important; }
  html.dark .bg-surface-container-highest { background-color: #333333 !important; }
  
  html.dark .text-on-surface-variant { color: #c4c4c4 !important; }
  
  html.dark .border-outline-variant { border-color: #444444 !important; }
  html.dark .border-outline { border-color: #737373 !important; }
  
  html.dark .bg-primary { background-color: #ffb2bc !important; }
  html.dark .text-on-primary { color: #4e051a !important; }
  
  html.dark .bg-primary-container { background-color: #8c263d !important; }
  html.dark .text-on-primary-container { color: #ffd9dd !important; }
  
  html.dark .bg-secondary-fixed { background-color: #1d4f40 !important; }
  html.dark .text-on-secondary-fixed { color: #baeed9 !important; }
  
  html.dark .text-inverse-on-surface { color: #121212 !important; }
  html.dark .bg-inverse-surface { background-color: #e3e3e3 !important; }
  
  /* Layout utilities */
  html.dark .bg-surface\\/80 { background-color: rgba(18, 18, 18, 0.8) !important; }
  html.dark .border-outline-variant\\/30 { border-color: rgba(68, 68, 68, 0.3) !important; }
  
  html.dark .hover\\:bg-surface-container-high:hover { background-color: #333333 !important; }
  html.dark .hover\\:text-on-surface:hover { color: #ffffff !important; }
  html.dark .hover\\:bg-primary-container:hover { background-color: #6b1d2f !important; }
  
  /* Input fields */
  html.dark input.bg-surface-container-low { background-color: #212121 !important; color: #ffffff !important; }
  
  /* Hero Text */
  html.dark .text-inverse-surface { color: #e3e3e3 !important; }
</style>
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the old dark mode overrides block
    content = re.sub(r'<style id="dark-mode-overrides">.*?</style>', new_dark_mode_css.strip(), content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated dark mode styles in {filename}")

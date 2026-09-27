import os
import re

new_dark_mode_css = """
<style id="dark-mode-overrides">
  /* Dark mode overrides for semantic colors */
  html.dark .bg-surface-container-lowest { background-color: #0a0a0a !important; }
  html.dark .bg-surface { background-color: #121212 !important; }
  html.dark .bg-surface-container-low { background-color: #1a1a1a !important; }
  html.dark .bg-surface-container { background-color: #212121 !important; }
  html.dark .bg-surface-container-high { background-color: #2b2b2b !important; }
  html.dark .bg-surface-container-highest { background-color: #333333 !important; }
  
  html.dark .bg-background { background-color: #121212 !important; }
  html.dark .text-on-background { color: #e3e3e3 !important; }

  html.dark .text-on-surface { color: #e3e3e3 !important; }
  html.dark .text-on-surface-variant { color: #c4c4c4 !important; }
  html.dark .text-outline { color: #999999 !important; }
  
  html.dark .bg-outline { background-color: #737373 !important; }
  html.dark .bg-outline-variant { background-color: #444444 !important; }
  
  html.dark .border-outline { border-color: #737373 !important; }
  html.dark .border-outline-variant { border-color: #444444 !important; }

  /* Primary */
  html.dark .bg-primary { background-color: #ffb2bc !important; }
  html.dark .text-primary { color: #ffb2bc !important; }
  html.dark .text-on-primary { color: #4e051a !important; }
  html.dark .text-on-primary-fixed { color: #4e051a !important; }
  html.dark .bg-primary-container { background-color: #8c263d !important; }
  html.dark .text-on-primary-container { color: #ffd9dd !important; }
  html.dark .bg-primary-fixed { background-color: #ffd9dd !important; }

  /* Secondary */
  html.dark .bg-secondary { background-color: #baeed9 !important; }
  html.dark .text-secondary { color: #baeed9 !important; }
  html.dark .text-on-secondary { color: #002117 !important; }
  html.dark .bg-secondary-container { background-color: #2a4f41 !important; }
  html.dark .text-on-secondary-container { color: #baeed9 !important; }
  html.dark .bg-secondary-fixed { background-color: #baeed9 !important; }
  html.dark .text-on-secondary-fixed { color: #002117 !important; }

  /* Tertiary */
  html.dark .bg-tertiary-fixed { background-color: #ffdea5 !important; }
  html.dark .bg-tertiary-fixed-dim { background-color: #e9c176 !important; }
  html.dark .text-on-tertiary-fixed { color: #261900 !important; }
  html.dark .text-tertiary-fixed { color: #ffdea5 !important; }
  html.dark .text-tertiary-container { color: #ffdea5 !important; }

  /* Inverse */
  html.dark .text-inverse-on-surface { color: #121212 !important; }
  html.dark .bg-inverse-surface { background-color: #e3e3e3 !important; }
  html.dark .text-inverse-on-surface\\/80 { color: rgba(18,18,18,0.8) !important; }
  html.dark .text-inverse-on-surface\\/90 { color: rgba(18,18,18,0.9) !important; }
  
  /* Opacity variations */
  html.dark .bg-surface\\/10 { background-color: rgba(18, 18, 18, 0.1) !important; }
  html.dark .bg-surface\\/80 { background-color: rgba(18, 18, 18, 0.8) !important; }
  html.dark .bg-surface\\/90 { background-color: rgba(18, 18, 18, 0.9) !important; }
  html.dark .bg-surface-container-high\\/80 { background-color: rgba(43, 43, 43, 0.8) !important; }
  html.dark .bg-surface-container-high\\/90 { background-color: rgba(43, 43, 43, 0.9) !important; }
  html.dark .bg-surface-container\\/20 { background-color: rgba(33, 33, 33, 0.2) !important; }
  html.dark .bg-inverse-surface\\/40 { background-color: rgba(227, 227, 227, 0.4) !important; }
  html.dark .bg-primary\\/5 { background-color: rgba(255, 178, 188, 0.05) !important; }
  html.dark .bg-tertiary-container\\/10 { background-color: rgba(255, 222, 165, 0.1) !important; }

  html.dark .border-outline-variant\\/20 { border-color: rgba(68, 68, 68, 0.2) !important; }
  html.dark .border-outline-variant\\/30 { border-color: rgba(68, 68, 68, 0.3) !important; }
  html.dark .border-outline-variant\\/40 { border-color: rgba(68, 68, 68, 0.4) !important; }

  /* Hover states */
  html.dark .hover\\:bg-surface-container-high:hover { background-color: #333333 !important; }
  html.dark .hover\\:text-on-surface:hover { color: #ffffff !important; }
  html.dark .hover\\:bg-primary-container:hover { background-color: #6b1d2f !important; }
  html.dark .group:hover .group-hover\\:text-on-surface { color: #ffffff !important; }
  
  /* Input fields */
  html.dark input.bg-surface-container-low { background-color: #212121 !important; color: #ffffff !important; }
  html.dark textarea.bg-surface-container-low { background-color: #212121 !important; color: #ffffff !important; }
  html.dark select.bg-surface-container-low { background-color: #212121 !important; color: #ffffff !important; }
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
        
    print(f"Injected comprehensive dark mode into {filename}")

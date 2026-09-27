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
  
  /* Gradient overrides for Hero sections */
  html.dark .from-background\\/95 {
      --tw-gradient-from: rgba(18, 18, 18, 0.95) var(--tw-gradient-from-position) !important;
      --tw-gradient-to: rgba(18, 18, 18, 0) var(--tw-gradient-to-position) !important;
      --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to) !important;
  }
  html.dark .via-background\\/70 {
      --tw-gradient-to: rgba(18, 18, 18, 0)  var(--tw-gradient-to-position) !important;
      --tw-gradient-stops: var(--tw-gradient-from), rgba(18, 18, 18, 0.7) var(--tw-gradient-via-position), var(--tw-gradient-to) !important;
  }

  /* Opacity variations */
  html.dark .bg-surface\\/10 { background-color: rgba(18, 18, 18, 0.1) !important; }
  html.dark .bg-surface\\/80 { background-color: rgba(18, 18, 18, 0.8) !important; }
  html.dark .bg-surface\\/90 { background-color: rgba(18, 18, 18, 0.9) !important; }
  html.dark .bg-surface-container-high\\/80 { background-color: rgba(43, 43, 43, 0.8) !important; }
  html.dark .bg-surface-container-high\\/90 { background-color: rgba(43, 43, 43, 0.9) !important; }
  html.dark .bg-surface-container\\/20 { background-color: rgba(33, 33, 33, 0.2) !important; }

  html.dark .border-outline-variant\\/20 { border-color: rgba(68, 68, 68, 0.2) !important; }
  html.dark .border-outline-variant\\/30 { border-color: rgba(68, 68, 68, 0.3) !important; }
  html.dark .border-outline-variant\\/40 { border-color: rgba(68, 68, 68, 0.4) !important; }

  /* Hover states */
  html.dark .hover\\:bg-surface-container-high:hover { background-color: #333333 !important; }
  html.dark .hover\\:text-on-surface:hover { color: #ffffff !important; }
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
        
    print(f"Fixed hero sections in {filename}")

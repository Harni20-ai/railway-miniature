import os
import re

nav_replacement = """<nav class="hidden lg:flex items-center gap-space-lg">
<div class="relative group flex items-center h-full">
  <button class="transition-colors text-body-md text-on-surface-variant group-hover:text-on-surface flex items-center gap-1 font-bold py-4">Home <span class="material-symbols-outlined text-[16px]">expand_more</span></button>
  <div class="absolute left-0 top-full w-40 bg-surface shadow-lg rounded-lg overflow-hidden hidden group-hover:block z-50 border border-outline-variant">
    <a href="index.html" onclick="window.location.href='index.html'; return false;" class="block px-4 py-2 text-body-md text-on-surface-variant hover:bg-surface-container hover:text-on-surface cursor-pointer">Home 1</a>
    <a href="home2.html" onclick="window.location.href='home2.html'; return false;" class="block px-4 py-2 text-body-md text-on-surface-variant hover:bg-surface-container hover:text-on-surface cursor-pointer">Home 2</a>
  </div>
</div>
<a class="text-body-md text-on-surface-variant hover:text-on-surface transition-colors cursor-pointer" href="products.html">Products</a>
<a class="text-body-md text-on-surface-variant hover:text-on-surface transition-colors cursor-pointer" href="custom-layouts.html">Custom Layouts</a>
<a class="text-body-md text-on-surface-variant hover:text-on-surface transition-colors cursor-pointer" href="repairs.html">Repairs</a>
<a class="text-body-md text-on-surface-variant hover:text-on-surface transition-colors cursor-pointer" href="contact.html">Contact</a>
</nav>"""

script_injection = """
<script>
  // Theme Toggle Logic
  const themeToggleBtn = document.getElementById('theme-toggle');
  const htmlEl = document.documentElement;
  
  // Check local storage for theme preference
  if (localStorage.getItem('theme') === 'dark') {
    htmlEl.classList.add('dark');
  }

  if(themeToggleBtn) {
      themeToggleBtn.addEventListener('click', () => {
        htmlEl.classList.toggle('dark');
        if (htmlEl.classList.contains('dark')) {
          localStorage.setItem('theme', 'dark');
        } else {
          localStorage.setItem('theme', 'light');
        }
      });
  }
</script>
</body>
"""

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <nav>...</nav>
    # Note: the nav tag could have different classes depending on the file, so we match <nav.*?</nav>
    # but we need to be careful. The original is: <nav class="hidden lg:flex items-center gap-space-lg" data-active-classes="bg-primary-container text-on-primary-container font-bold rounded-lg">...</nav>
    content = re.sub(r'<nav[^>]*>.*?</nav>', nav_replacement, content, flags=re.DOTALL)
    
    # Add JS before </body>
    if '<script>\n  // Theme Toggle Logic' not in content:
        content = content.replace('</body>', script_injection)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']
for filename in files:
    if os.path.exists(filename):
        process_html_file(filename)
        print(f"Processed {filename}")
    else:
        print(f"File not found: {filename}")

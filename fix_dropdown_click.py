import os
import re

nav_replacement = """<nav class="hidden lg:flex items-center gap-space-lg">
<div class="relative flex items-center h-full">
  <button id="home-menu-btn" class="transition-colors text-body-md text-on-surface-variant hover:text-on-surface flex items-center gap-1 font-bold py-4">Home <span class="material-symbols-outlined text-[16px]">expand_more</span></button>
  <div id="home-menu" class="absolute left-0 top-full w-40 bg-surface shadow-lg rounded-lg overflow-hidden hidden z-50 border border-outline-variant">
    <a href="index.html" class="block px-4 py-2 text-body-md text-on-surface-variant hover:bg-surface-container hover:text-on-surface cursor-pointer">Home 1</a>
    <a href="home2.html" class="block px-4 py-2 text-body-md text-on-surface-variant hover:bg-surface-container hover:text-on-surface cursor-pointer">Home 2</a>
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
  
  if (localStorage.getItem('theme') === 'dark') {
    htmlEl.classList.add('dark');
  }

  if(themeToggleBtn) {
      themeToggleBtn.addEventListener('click', () => {
        htmlEl.classList.toggle('dark');
        localStorage.setItem('theme', htmlEl.classList.contains('dark') ? 'dark' : 'light');
      });
  }

  // Dropdown Logic
  const homeBtn = document.getElementById('home-menu-btn');
  const homeMenu = document.getElementById('home-menu');
  if (homeBtn && homeMenu) {
      homeBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          homeMenu.classList.toggle('hidden');
      });
      document.addEventListener('click', (e) => {
          if (!homeBtn.contains(e.target) && !homeMenu.contains(e.target)) {
              homeMenu.classList.add('hidden');
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
    content = re.sub(r'<nav[^>]*>.*?</nav>', nav_replacement, content, flags=re.DOTALL)
    
    # Remove previous injected script to avoid duplicates
    content = re.sub(r'<script>\s*// Theme Toggle Logic.*?</script>', '', content, flags=re.DOTALL)
    
    # Add new JS before </body>
    content = content.replace('</body>', script_injection)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']
for filename in files:
    if os.path.exists(filename):
        process_html_file(filename)
        print(f"Processed {filename}")

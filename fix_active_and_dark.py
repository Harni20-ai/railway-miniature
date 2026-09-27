import os
import re

script_logic_to_remove = "themeToggle.addEventListener('click', () => { document.documentElement.classList.toggle('dark'); });"

active_link_js = """
  // Active Link Logic
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('nav a');
  
  // Handle Home Button Active State separately because it's a button opening a dropdown
  if (currentPath === 'index.html' || currentPath === 'home2.html') {
      const homeMenuBtn = document.getElementById('home-menu-btn');
      if (homeMenuBtn) {
          homeMenuBtn.classList.remove('text-on-surface-variant');
          homeMenuBtn.classList.add('text-primary');
      }
  }

  navLinks.forEach(link => {
      const href = link.getAttribute('href');
      // Some hrefs might be full URLs, but ours are relative like "products.html"
      if (href === currentPath || (currentPath === '' && href === 'index.html')) {
          link.classList.remove('text-on-surface-variant');
          link.classList.add('text-primary', 'font-bold');
          
          // If it's inside the dropdown, also highlight it specifically
          if (link.parentElement && link.parentElement.id === 'home-menu') {
              link.classList.add('bg-surface-container');
          }
      }
  });
"""

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old theme toggle logic to prevent double-toggling
    content = content.replace(script_logic_to_remove, '')
    
    # Inject Active link JS right before the end of our custom script
    if '// Active Link Logic' not in content:
        content = content.replace('</script>\n</body>', active_link_js + '\n</script>\n</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed dark mode and active state on {filename}")

import os

files = ['index.html', 'home2.html', 'products.html', 'custom-layouts.html', 'repairs.html', 'contact.html']

rtl_logic_to_remove = "rtlToggle.addEventListener('click', () => { const isRtl = document.documentElement.getAttribute('dir') === 'rtl'; document.documentElement.setAttribute('dir', isRtl ? 'ltr' : 'rtl'); rtlToggle.textContent = isRtl ? 'RTL' : 'LTR'; });"

persist_js = """
  // Persistent RTL Logic
  const rtlBtn = document.getElementById('rtl-toggle');
  if (localStorage.getItem('direction') === 'rtl') {
    document.documentElement.setAttribute('dir', 'rtl');
    if (rtlBtn) rtlBtn.textContent = 'LTR';
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
    if (rtlBtn) rtlBtn.textContent = 'RTL';
  }

  if (rtlBtn) {
      rtlBtn.addEventListener('click', () => {
          const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
          const newDir = isRtl ? 'ltr' : 'rtl';
          document.documentElement.setAttribute('dir', newDir);
          rtlBtn.textContent = isRtl ? 'RTL' : 'LTR';
          localStorage.setItem('direction', newDir);
      });
  }
"""

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old RTL toggle logic
    content = content.replace(rtl_logic_to_remove, '')

    # Inject Persistent RTL JS right before the end of our custom script
    if '// Persistent RTL Logic' not in content:
        content = content.replace('</script>\n</body>', persist_js + '\n</script>\n</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Added persistence on {filename}")

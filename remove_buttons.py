import re
import glob

files = glob.glob('d:/DUMP WEB/ironclad-gauge/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove wishlist button
    content = re.sub(r'<button[^>]*id="wishlist-btn"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    # Remove cart button
    content = re.sub(r'<button[^>]*id="cart-btn"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

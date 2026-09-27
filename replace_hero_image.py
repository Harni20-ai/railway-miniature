import os

filename = 'custom-layouts.html'
old_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuDfdzAlXeNiD_mvo1fw7FQzwxLJM7jccVt5AcpJ0YJPna-Yyk2PnGLBgK0H52VmQi25soDopnbkeyOukoJa6sOC5QoqnNTvE05V2gdDj8Jk5_dhKY_UAdMGhivX-e665uEoZhuBYGZ9z5pIimvdiaZe6dN0TiA-DfqCiD3znUIQCFmxBIB8kBvUVTXDaAfhmxkWEH2qeeBUCVQ5FRSqXTs1Fat_ls8nnpWe4H4AZxalJVtttc965rmC6A"
new_url = "custom_layouts_hero.jpg"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(old_url, new_url)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated Hero image URL in custom-layouts.html")

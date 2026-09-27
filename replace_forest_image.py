import os

filename = 'custom-layouts.html'
old_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuDTQyaimNsnQWHDwgjPHW3CYCKRz24VQ_oq4le975TqcKVOqroSFPS0Xc4jygDI7u9bcdmwp7B7kFk61u51gJdF50_rZnpS-yE9wHf0-KjHZm2EyjR3qhF6BVxP-Pd700MnZWqEPtGmj7UDeGrQt50GRvAp3LOZTAK4d14ZgfxsQBzK89KFP9Fr57n9ukdXD5eStzTWcBbP86U4jmLN2OB_Z4qlwGfd3niyudEGMcBiDFjdfXDYfo9Bjw"
new_url = "black_forest_pass.jpg"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(old_url, new_url)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated The Black Forest Pass image URL in custom-layouts.html")

import os, glob

files = glob.glob('d:/DUMP WEB/ironclad-gauge/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace icon buttons padding
    content = content.replace('class="p-space-xs rounded-full hover:bg-surface-container-high', 'class="p-2 rounded-full hover:bg-surface-container-high')
    content = content.replace('class="relative p-space-xs rounded-full hover:bg-surface-container-high', 'class="relative p-2 rounded-full hover:bg-surface-container-high')
    
    # Replace RTL toggle
    content = content.replace('class="px-space-xs py-1 rounded text-label-md bg-surface-container-high', 'class="px-2 py-1.5 rounded text-label-md bg-surface-container-high')
    
    # Replace CTA (Header + any other place using it)
    content = content.replace('class="hidden sm:inline-flex items-center justify-center px-space-lg py-space-sm bg-primary text-on-primary rounded-xl text-label-md hover:bg-primary-container hover:text-on-primary-container transition-colors"', 'class="hidden sm:inline-flex items-center justify-center px-space-lg py-2.5 bg-primary text-on-primary rounded-xl text-label-md hover:bg-primary/90 transition-colors"')
    
    # Person icon container (from w-8 h-8 to w-9 h-9)
    content = content.replace('class="w-8 h-8 rounded-full bg-primary flex items-center justify-center"', 'class="w-9 h-9 rounded-full bg-primary flex items-center justify-center"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

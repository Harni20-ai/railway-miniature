import os

filename = 'custom-layouts.html'
old_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuA-K8djjl0DEMcPvH69cMYj8B8HhIVx2U0KVeKsfsJDHzAESoodaUV6Ahc9PedmTz9ngTO4LAafdBGgg8ybAe7_AsnnIMOmw8Dk8-pG3kpNmKiHK4pmW3b3Ot5-hB78nAqdZMzCSLrCqcbIz6GaAmNo5wdV1qwnJNn4wMAK8P_3-ttNl2AxmOOw7P11lHrRDiTjAHUkAi0Lk_gQCAFq_YUii7ZvHJAYSSFK7cR8iR4UdSX2Z8h701T1kQ"
new_url = "urban_metropolis.jpg"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(old_url, new_url)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated image URL in custom-layouts.html")

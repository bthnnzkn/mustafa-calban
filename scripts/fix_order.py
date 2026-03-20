import re
content = open('index.html').read()

# Her section'ın başını ve içeriğini bul
all_sections = {}
for name, marker in [('allen','Photo Production'),('event','Event Photography'),('drone','Real Estate Drone'),('sm','Social Media')]:
    idx = content.find(marker)
    start = content.rfind('<section', 0, idx)
    # Bir sonraki section başına kadar al
    next_sec = content.find('<section', start + 100)
    end = next_sec if next_sec > 0 else len(content)
    all_sections[name] = (start, end, content[start:end])
    print(name, start, end, len(content[start:end]))

# En küçük start = ilk section başlangıcı
first_start = min(v[0] for v in all_sections.values())
services_start = content.find('<section class="section services-bg"')

before = content[:first_start]
after = content[services_start:]

# İstenen sıra: allen -> event -> drone -> sm
result = before + all_sections['allen'][2] + all_sections['event'][2] + all_sections['drone'][2] + all_sections['sm'][2] + after
open('index.html', 'w').write(result)

names = re.findall(r'(Photo Production|Event Photography|Real Estate Drone|Social Media)', result)
print('Yeni sira:', names[:4])

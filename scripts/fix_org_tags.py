content = open('organization.html').read()

# Bozuk emoji taglerini temiz hale getir
replacements = [
    ('💍 Weddings', 'Weddings'),
    ('🍼 Baby Shower', 'Baby Shower'),
    ('🎂 Birthdays', 'Birthdays'),
    ('🌸 Floral Design', 'Floral Design'),
    ('🍽️ Catering', 'Catering'),
    ('📸 Photography', 'Photography'),
    ('✨ Decor', 'Decor'),
    ('🏢 Corporate', 'Corporate'),
    ('— Midpoint', '— Midpoint'),
]

for old, new in replacements:
    content = content.replace(old, new)

open('organization.html', 'w').write(content)
print('done')

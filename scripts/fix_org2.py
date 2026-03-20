content = open('organization.html', encoding='utf-8').read()

# Floral kart foto ekle
old = '<div class="card-img" style="background:linear-gradient(135deg,#fdf6f0,#f9ede0)"></div>'
new = '<div class="card-img" style="background-image:url(\'https://drive.google.com/thumbnail?id=1TF1e8NmlHR5C4Z4Xdqlh9ZKUgXDRkOKs&sz=w800\');background-size:cover;background-position:center;"></div>'
result = content.replace(old, new, 1)

print('replaced:', old not in result)
open('organization.html', 'w', encoding='utf-8').write(result)

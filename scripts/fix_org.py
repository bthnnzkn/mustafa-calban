content = open('index.html').read()

old = '<button class="nav-cta" onclick="openModal()">Client Access</button>'
new = '<a href="/organization.html" target="_blank" style="display:inline-flex;align-items:center;padding:.5rem 1.2rem;border-radius:50px;border:1.5px solid #1d1d1f;font-size:.75rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#1d1d1f;text-decoration:none;margin-right:.75rem;transition:all .2s;">Organization</a><button class="nav-cta" onclick="openModal()">Client Access</button>'

result = content.replace(old, new, 1)
open('index.html', 'w').write(result)
print('done:', 'Organization' in result)

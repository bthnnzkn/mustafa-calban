content = open('index.html').read()

start = content.find('<section class="section services-bg" id="services">')
end = content.find('</section>', start) + len('</section>')

result = content[:start] + content[end:]
open('index.html', 'w').write(result)
print('done, kaldirildi:', 'services-bg' not in result)

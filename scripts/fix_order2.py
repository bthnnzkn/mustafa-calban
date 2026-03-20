import re
content = open('index.html').read()

pos = {}
for name, marker in [('allen','Alain Giresse'),('event','Event Photography'),('drone','Real Estate Drone'),('sm','Social Media')]:
    idx = content.find(marker)
    pos[name] = content.rfind('<section', 0, idx)

sorted_pos = sorted(pos.items(), key=lambda x: x[1])
print('Mevcut sira:', [x[0] for x in sorted_pos])

keys = [x[0] for x in sorted_pos]
starts = [x[1] for x in sorted_pos]
team_start = content.find('<section class="section team-bg"')
starts.append(team_start)

sections = {}
for i, key in enumerate(keys):
    sections[key] = content[starts[i]:starts[i+1]]

before = content[:starts[0]]
after = content[team_start:]

# Yeni sira: allen -> event -> drone -> sm
result = before + sections['allen'] + sections['event'] + sections['drone'] + sections['sm'] + after
open('index.html', 'w').write(result)

names = re.findall(r'(Alain Giresse|Event Photography|Real Estate Drone|Social Media)', result)
print('Yeni sira:', names[:4])

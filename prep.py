import sys

print('Set AI=fixed for all traffic cars...')

# opening entry_list.ini
entry_list_filename = 'entry_list.ini'
with open(entry_list_filename, 'r') as file:
    # read a list of lines into data
    entry_list_lines = file.readlines()

# opening traffic_list.txt
with open('traffic_list.txt', 'r') as file:
    # read a list of lines into data
    traffic_list_lines = file.readlines()

# get lines where the traffic model name mentioned
targets = []
for i in range(len(traffic_list_lines)):
    car_name = traffic_list_lines[i]
    targets.append('MODEL={}'.format(car_name))

i = 0
while i < len(entry_list_lines):
    if entry_list_lines[i] not in targets:
        i += 1
        continue

    newIndex = i + 8
    entry_list_lines.insert(newIndex, 'AI=fixed\n')

    i += 1

# write everything back
with open(entry_list_filename, 'w') as file:
    file.writelines(entry_list_lines)



print('Replacing extra_cfg.yml...')
extra_cfg_filename = 'extra_cfg.yml'
extra_cfg = open(extra_cfg_filename, 'r')
target_extra_cfg = open('../../cfg/{}'.format(extra_cfg_filename), 'w')
target_extra_cfg.write(extra_cfg.read())

print('Configuration ready!')

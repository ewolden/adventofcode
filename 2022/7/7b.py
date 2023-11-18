current_path = ''
folder_array = {'/': {'filesize': []}}

with open('7input.txt','r') as f:
    for line in f:
        stripped_line = line.rstrip()
        #check if command
        if stripped_line[0] == '$':
            command = stripped_line[2:]
            if command == 'ls':
                continue
            elif command == 'cd /':
                current_path = '/'
            elif command == 'cd ..':
                current_path = current_path[:current_path[:current_path.rindex('/')-1].rindex('/')] + '/'
            else:
                current_path = current_path + command[3:] + '/'
            #print(current_path)
        # if ls then:
        else:
            #if there is a subdirectory
            if stripped_line[:4] == 'dir ':
                if not current_path + stripped_line[4:] in folder_array:
                    folder_array[current_path + stripped_line[4:] + '/'] = {'filesize': []}
            #if there is a subfile
            else:
                folder_array[current_path]['filesize'].append(int(stripped_line.split(' ')[0]))


#find direct size of folders
for folder in folder_array:
    folder_array[folder]['foldersize'] = sum(folder_array[folder]['filesize'])

#find indirect size of folders
for key in sorted(folder_array, reverse=True):
    for previous_keys in sorted(folder_array, reverse=True):
        if key == previous_keys:
            break
        else:
            if key in previous_keys and len(key.split('/')) + 1 == len(previous_keys.split('/')):
                folder_array[key]['foldersize'] = folder_array[key]['foldersize'] + folder_array[previous_keys]['foldersize']

#print(folder_array)
current_smallest = 70000000
if 70000000 - folder_array['/']['foldersize'] >= 0:
    total_size_free = 70000000 - folder_array['/']['foldersize']
else:
    total_size_free = 0
total_size_required_to_free = 30000000 - total_size_free
for folder in folder_array:
    if folder_array[folder]['foldersize'] >= total_size_required_to_free and folder_array[folder]['foldersize'] < current_smallest:
        current_smallest = folder_array[folder]['foldersize']

print(current_smallest)
with open("inputs/input07.txt", "r") as f:
    data = f.readlines()

terminal = [s.strip() for s in data]

# Part 1
def parse_command(l):
    global path
    if l.startswith("cd"):
        dir = l[3:]
        if dir == "/":
            path = dir
        elif dir == "..":
            path = path.rsplit("/", 2)[0] + "/"
        else:
            path = path + dir + "/"


def parse_content(l):
    if l[0].isdigit():
        fileinfo = l.split()
        contents.append([path] + [int(fileinfo[0]), fileinfo[1]])


path = ""
contents = []

for l in terminal:
    if l[0] == "$":
        parse_command(l[2:])
    else:
        parse_content(l)

possible_paths = ['/']
for p in [c[0].split('/') for c in contents]:
    paths = []
    path = ''
    for d in p:
        if d != '':
            path = path + '/' + d
            paths.append(path)
    possible_paths.append(paths)

folders = {p for p in possible_paths for p in p}

folder_sizes = []
for c in folders:
    folder_sizes.append([c, sum([x[1] for x in contents if x[0].startswith(c)])])

sum_of_folders_to_delete = sum([f[1] for f in folder_sizes if f[1] <= 100000])

print('Sum of all of the directories with a total size of at most 100000:', sum_of_folders_to_delete)


# Part 2

total_size = 70000000
space_needed = 30000000
space_used = [f[1] for f in folder_sizes if f[0] == '/'][0]
need_to_delete = space_needed - (total_size - space_used)

delete_candidates = [f for f in folder_sizes if f[1] > need_to_delete]
delete_candidates.sort(key = lambda x : x[1])

print('Smallest directory that, if deleted, would free up enough space on the filesystem to run the update:', delete_candidates[0])

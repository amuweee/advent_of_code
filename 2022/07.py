# no space left on device
import json

with open("data/07.txt") as f:
    outputs = f.readlines()

commands = [c.strip("\n") for c in outputs]

pwd = []
filesystem = {}

for c in commands:
    out = c.split()
    path = "_".join(pwd)
    if c == "$ cd ..":
        # remove last dir in path
        pwd.pop()
    elif out[:2] == ["$", "cd"]:
        # update path
        pwd.append(out[2])
    elif out == ["$", "ls"]:
        # create path as key, and initialize path key
        filesystem[path] = {"sub_dirs": [], "files": {}}
    elif out[0] == "dir":
        # append the dir name to path's sub_dirs
        filesystem[path]["sub_dirs"].append(path + "_" + out[1])
    else:
        filesystem[path]["files"][out[1]] = int(out[0])

# tally up all the local dir file sizes
for path in filesystem:
    filesystem[path]["dir_fsize"] = sum([s for s in filesystem[path]["files"].values()])

# recurse through the filesystem
def get_nested_dirs(filesystem, cwd, dir_list):

    subs = filesystem[cwd]["sub_dirs"]
    dir_list = dir_list + subs
    for d in subs:
        dir_list = get_nested_dirs(filesystem, d, dir_list)

    return dir_list

directory = {}
for dir in filesystem:
    directory[dir] = list(set(get_nested_dirs(filesystem, dir, [])))

# set all the sub-dirs and total file_sizes
for dir in directory:
    filesystem[dir]["sub_dirs"] = directory[dir]
    file_sizes = []
    fsize = filesystem[dir]["dir_fsize"]
    subs = directory[dir]
    for s in subs:
        fsize += filesystem[s]["dir_fsize"]

    file_sizes.append((dir, fsize))
    for f in file_sizes:
        filesystem[f[0]]["total_size"] = f[1]

# show mapped file systems
print(json.dumps(filesystem, indent=4))

# part 1
under_100k = [
    filesystem[f]["total_size"]
    for f in filesystem
    if filesystem[f]["total_size"] <= 100000
]
print(f"total size of dirs under 100k is: {sum(under_100k)}")

# part 2
root_size = filesystem["/"]["total_size"]
free_space = 70000000 - root_size
min_required = 30000000 - free_space
eligible = [
    filesystem[f]["total_size"]
    for f in filesystem
    if filesystem[f]["total_size"] >= min_required
]
print(f"the smalled dir to delete is: {min(eligible)}")

import os, pangu


def space_file(file):
    name, ext = os.path.splitext(file)
    nf = open(f'../{file}', 'w')
    with open(file, 'r') as f:
        for line in f.readlines():
            tmp = line.strip()
            tmp = tmp.replace('blob/debug', 'blob/master')
            new = pangu.spacing_text(tmp)
            nf.writelines(new + '\n')
            # print(new)
    nf.close()


lst = os.listdir('./')  # list all files in this folder
lst.sort()
for file in lst:
    name, ext = os.path.splitext(file)
    # print(file)
    # exit()
    if ext == '.md':
        space_file(file)

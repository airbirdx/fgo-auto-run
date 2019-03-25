import os
import pangu


def space_file(file):

    f = open(file, 'r')
    txt = f.read()
    f.close()

    # new_txt = txt.replace('- ', '+ ')
    new_txt = txt.replace('* ', '+ ')
    # print(new_txt)

    f = open(file, 'w')
    f.write(new_txt)
    f.close()


    name, ext = os.path.splitext(file)
    nf = open(f'../new_{file}', 'w')
    with open(file, 'r') as f:
        for line in f.readlines():
            tmp = line.strip()
            tmp = tmp.replace('blob/debug', 'blob/master')

            new = pangu.spacing_text(tmp)
            new = new.replace('** ', '**')
            new = new.replace(' **', '**')
            new = new.replace('~~ ', '~~')
            new = new.replace(' ~~', '~~')

            nf.writelines(new + '\n')
            # print(new)
    nf.close()


space_file('parameter.md')
exit()

lst = os.listdir('./')  # list all files in this folder
lst.sort()
for file in lst:
    name, ext = os.path.splitext(file)
    # print(file)
    # exit()
    if ext == '.md':
        space_file(file)

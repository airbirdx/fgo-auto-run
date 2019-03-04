import os

# convert all png file for less warning
def convert(path):
    ls = os.listdir(path)
    for i in ls:
        tmp_path = os.path.join(path, i)
        # print(c_path)
        if os.path.isdir(tmp_path):
            convert(tmp_path)
        else:
            if '.png' in tmp_path:
                cvt_cmd = 'magick convert {src} {dest}'.format(
                    src = tmp_path,
                    dest = tmp_path
                )
                os.system(cvt_cmd)
                print(tmp_path)

convert('.')
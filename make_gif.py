from PIL import Image
import subprocess,re


OriginalData_path = 'F:\制作动图'

def listDataPath():

    cmd = 'dir ' + OriginalData_path.replace('/','\\')
    files = subprocess.check_output(cmd,shell=True)
    files = str(files, encoding = "GBK")
    files = files.strip().split('\r\n')
    regex = re.compile(r'.*\s(.+\.jpg).*')
    listFiles = []
    for path in files:
        match = regex.match(path)
        if match:
            listFiles.append(OriginalData_path+'/'+match.group(1))
    return listFiles


def main():
    imgaeList = listDataPath()
    num=0
    images = []
    for i in imgaeList:
        num += 1
        if num==1:
            im = Image.open(i)
        else:
            images.append(Image.open(i))
            im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")

if __name__ == "__main__":
    main()
import os
import shutil
import argparse


class FileTypeHandler:
    def __init__(self):
        self.mapping={".jpg":"images",".pdf":"Document",".json":"File"}

    def get_category(self,extension):
        if extension in self.mapping.keys():
            return self.mapping[extension]
        return "others"

class FileOrganizer:
    def __init__(self,path):
        handler=FileTypeHandler()
        for file in os.listdir(path):
            root,extension=os.path.splitext(file)
            folder=handler.get_category(extension)
            os.makedirs(folder,exist_ok=True)
            shutil.move(file,folder)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--path",required=True)

    args=parser.parse_args()
    print(args)
    fileOrg=FileOrganizer(args.path)


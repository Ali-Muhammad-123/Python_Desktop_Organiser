import os, shutil
def Diff(li1, li2): 
    li_diff = []
    for i in li1 + li2 :
        if i not in li1 or i not in li2:
            li_diff.append(i)
    return li_diff

path = R"C:\Users\hp\Desktop"
i=0
list1 = os.listdir(path)

list2 = os.listdir(path)
while True:
    list2 = os.listdir(path)
    while list1!=list2:
        list2 = os.listdir(path)
        if(list1!=list2):
            filename =  Diff(list1,list2)
            print(filename)
            for i in filename:
                filename =  r"\\" + i
                filetobemoved = path  + str(filename)
                if (".img"  in i or".jpg" in i or ".jpeg" in i or ".png" in i) :
                    shutil.move( filetobemoved , r"C:\Users\hp\Desktop\PYTHON ORGANISATION FOLDER\Images")
                if (".doc"  in i or".docx" in i or ".pdf" in i or ".txt" in i) : 
                    shutil.move( filetobemoved , r"C:\Users\hp\Desktop\PYTHON ORGANISATION FOLDER\Documents")
                if (".rar"  in i or".zip" in i or ".zar" in i or ".arj" in i) : 
                    shutil.move( filetobemoved , r"C:\Users\hp\Desktop\PYTHON ORGANISATION FOLDER\Compressed")      
                else :
                    shutil.move( filetobemoved , r"C:\Users\hp\Desktop\PYTHON ORGANISATION FOLDER\Misc")
    
    
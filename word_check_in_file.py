
def Search(file,words):
    with open(file) as target_file:
        contents = target_file.read()
        i=0
        k=0
        for word in words:
            i+=1
            if word in contents:
                k=1                
                print ("!!! ERROR !!!")
                break        
        if i==len(words) and k==0:
            print("NO ERROR")
    
file=r"File-path-here-with-name"
words=["FATAL","fatal","Fatal"]
Search(file,words)
import os

def main():
    i = 1
    path = "/home/kautuk/Pictures/"
    for filename in os.listdir(path):
        if filename[-4:] == '.png':
            my_dest = "image " + str(i) + ".png"
            my_source =path + filename
            my_dest =path + my_dest
            os.rename(my_source,my_dest)
            i+=1

if __name__ == '__main__':
    main()


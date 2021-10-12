# coding: utf-8

if __name__ == "__main__":
    with open('list.txt') as f:
        for line in f.readlines():
            s = line.strip()
            name, version = s[s.rindex("/")+1:].split(":")

            with open('Dockerfile.'+name, 'w') as ff:
                ff.write("FROM "+line+"\n")

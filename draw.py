import subprocess

if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    filename = file.split('/')[-1].split('.')[:-1][0]
    if file.split('.')[-1] != 'dot':
        raise Exception('You must pass a dot file')

    subprocess.call(["dot","-Tsvg",file,"-o",f"assets/img/{filename}.svg"])

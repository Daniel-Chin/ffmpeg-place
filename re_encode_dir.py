import os
from os import path
from subprocess import Popen

def main():
    target_dir = input('Enter the target directory: ')
    target_dir = path.abspath(target_dir)
    print()
    print('Target directory:', target_dir)
    print('Confirm? y/n')
    assert input().lower() == 'y'
    basenames = [x for x in os.listdir(target_dir) if x.endswith('.mp4')]
    for basename in basenames:
        print('Re-encoding', basename, '...')
        src = path.join(target_dir, basename)
        with Popen([
            'ffmpeg', '-i', src, path.join(
                target_dir, 're_' + basename, 
            ), 
        ]) as p:
            p.wait()
    print('all ok')

if __name__ == '__main__':
    main()

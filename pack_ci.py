import gzip
import base64
import os
import py_compile
import zlib
import gzip
import bz2
import tarfile
import lzma
import sys
import shutil
import argparse

print("WavyPacker v1.0")
print('\nThe author is not responsible for any actions with the program!\nThe packaging of viruses is prohibited and is a criminal offence!\n')

parser = argparse.ArgumentParser(description='PyPacker')
parser.add_argument('-f' ,'-file', type=str, help='Select file to pack')
parser.add_argument(
    '--alg',
    '-a',
    type=str,
    default=2,
    help='Select algoritm (optional)\nCan be selected:\nlzma\ngzip\nbz2\nzlib'
)

args = parser.parse_args()

if os.path.exists(args.f):
    file = args.f
else:
    print('File not found!')
    print('\n\n\nPress enter for exit...')
    input()
    quit()
            
print('Reading file...')
datafile = open(file,'rb').read()

if args.alg == 2:
    print('Preparing for selecting...')
    zlib_compressed = zlib.compress(datafile)
    print('Prepared: zlib')
    gzip_compressed = gzip.compress(datafile)
    print('Prepared: gzip')
    bz2_compressed = bz2.compress(datafile)
    print('Prepared: bz2')
    lzma_compressed = lzma.compress(datafile)
    print('Prepared: lzma')
    
if '.py' in file:
    if args.alg == 2:
        print('Selecting Algoritm...')
        if sys.getsizeof(zlib_compressed) < sys.getsizeof(gzip_compressed) and sys.getsizeof(zlib_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(zlib_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: zlib')
            print('Packing...')
            open('tmp.py','w').write('import zlib;exec(zlib.decompress('+str(zlib.compress(datafile))+'))')
        elif sys.getsizeof(gzip_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(gzip_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(gzip_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: gzip')
            print('Packing...')
            open('tmp.py','w').write('import gzip;exec(gzip.decompress('+str(gzip.compress(datafile))+'))')
        elif sys.getsizeof(bz2_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(bz2_compressed) < sys.getsizeof(gzip_compressed) and sys.getsizeof(bz2_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: bz2')
            print('Packing...')
            open('tmp.py','w').write('import bz2;exec(bz2.decompress('+str(bz2.compress(datafile))+'))')#
        elif sys.getsizeof(lzma_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(lzma_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(lzma_compressed) < sys.getsizeof(gzip_compressed):
            print('Selected! Name: lzma')
            print('Packing...')
            open('tmp.py','w').write('import lzma;exec(lzma.decompress('+str(lzma.compress(datafile))+'))')
    else:
        if args.alg == 'lzma':
            print('Packing...')
            open('tmp.py','w').write('import lzma;exec(lzma.decompress('+str(lzma.compress(datafile))+'))')
        elif args.alg == 'zlib':
            print('Packing...')
            open('tmp.py','w').write('import zlib;exec(zlib.decompress('+str(zlib.compress(datafile))+'))')
        elif args.alg == 'bz2':
            print('Packing...')
            open('tmp.py','w').write('import bz2;exec(bz2.decompress('+str(bz2.compress(datafile))+'))')
        elif args.alg == 'gzip':
            print('Packing...')
            open('tmp.py','w').write('import gzip;exec(gzip.decompress('+str(gzip.compress(datafile))+'))')
        else:
            print('Unknown packing algoritm!')
            print('\n\n\nPress enter for exit...')
            input()
            quit()
else:
    if args.alg == 2:
        print('Selecting Algoritm...')
        #print('zlib: '+str(sys.getsizeof(zlib_compressed)))
        #print('gzip: '+str(sys.getsizeof(gzip_compressed)))
        #print('bz2: '+str(sys.getsizeof(bz2_compressed)))
        #print('lzma: '+str(sys.getsizeof(lzma_compressed)))
        if sys.getsizeof(zlib_compressed) < sys.getsizeof(gzip_compressed) and sys.getsizeof(zlib_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(zlib_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: zlib')
            print('Packing...')
            open('tmp.pyw','w').write('import zlib;import os;open("'+file+'","wb").write('+'zlib.decompress('+str(zlib.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif sys.getsizeof(gzip_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(gzip_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(gzip_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: gzip')
            print('Packing...')
            open('tmp.pyw','w').write('import gzip;import os;open("'+file+'","wb").write('+'gzip.decompress('+str(gzip.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif sys.getsizeof(bz2_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(bz2_compressed) < sys.getsizeof(gzip_compressed) and sys.getsizeof(bz2_compressed) < sys.getsizeof(lzma_compressed):
            print('Selected! Name: bz2')
            print('Packing...')
            open('tmp.pyw','w').write('import bz2;import os;open("'+file+'","wb").write('+'bz2.decompress('+str(bz2.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif sys.getsizeof(lzma_compressed) < sys.getsizeof(zlib_compressed) and sys.getsizeof(lzma_compressed) < sys.getsizeof(bz2_compressed) and sys.getsizeof(lzma_compressed) < sys.getsizeof(gzip_compressed):
            print('Selected! Name: lzma')
            print('Packing...')
            open('tmp.pyw','w').write('import lzma;import os;open("'+file+'","wb").write('+'lzma.decompress('+str(lzma.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
    else:
        if args.alg == 'lzma':
            print('Packing...')
            open('tmp.pyw','w').write('import lzma;import os;open("'+file+'","wb").write('+'lzma.decompress('+str(lzma.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif args.alg == 'zlib':
            print('Packing...')
            open('tmp.pyw','w').write('import zlib;import os;open("'+file+'","wb").write('+'zlib.decompress('+str(zlib.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif args.alg == 'bz2':
            print('Packing...')
            open('tmp.pyw','w').write('import bz2;import os;open("'+file+'","wb").write('+'bz2.decompress('+str(bz2.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        elif args.alg == 'gzip':
            print('Packing...')
            open('tmp.pyw','w').write('import gzip;import os;open("'+file+'","wb").write('+'gzip.decompress('+str(gzip.compress(datafile))+'));os.system("'+file+'");os.remove("'+file+'")')
        else:
            print('Unknown packing algoritm!')
            print('\n\n\nPress enter for exit...')
            input()
            quit()
print('Cleaning memory...')
if args.alg == 2:
    del zlib_compressed
    del gzip_compressed
    del bz2_compressed
    del lzma_compressed
    del datafile

print('Compiling...')

if os.path.exists('tmp.pyw'):
    py_compile.compile('tmp.pyw')
else:
    py_compile.compile('tmp.py')


print('Final steps...')
for file2 in os.listdir("__pycache__"):
    shutil.move(f"__pycache__/{file2}", "./"+file+'.pyc')

print('Cleaning temp...')
os.rmdir('./__pycache__')
if os.path.exists('tmp.pyw'):

    os.remove('tmp.pyw')
else:

    os.remove('tmp.py')
    
print('\n\n\n Press enter for exit...')
input()
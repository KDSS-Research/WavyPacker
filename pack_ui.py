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

print("WavyPacker v1.0")
print('\nThe author is not responsible for any actions with the program!\nThe packaging of viruses is prohibited and is a criminal offence!\n')

file = input('File: ')

print('Reading file...')
datafile = open(file,'rb').read()

print('Preparing for selecting...')
zlib_compressed = zlib.compress(datafile)
print('Prepared: zlib')
gzip_compressed = gzip.compress(datafile)
print('Prepared: gzip')
bz2_compressed = bz2.compress(datafile)
print('Prepared: bz2')
lzma_compressed = lzma.compress(datafile)
print('Prepared: lzma')
    
print('Selecting Algoritm...')
if '.py' in file:
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

print('Cleaning memory...')
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
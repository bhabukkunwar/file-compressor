import gzip
import lzma
import bz2
import shutil

with open('./largefile.txt', 'rb') as f_in, gzip.open('/home/compressed-files/largefile.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
with open('./largefile.txt', 'rb') as f_in, bz2.open('/home/compressed-files/largefile.txt.bz2', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
with open('./largefile.txt', 'rb') as f_in, lzma.open('/home/compressed-files/largefile.txt.lzma', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

with gzip.open('/home/compressed-files/largefile.txt.gz', 'rb') as f_in, open('/home/decompressed-files/largefile.txt', 'wb') as f_out:
    shutil.copyfileobj(f_in,f_out)

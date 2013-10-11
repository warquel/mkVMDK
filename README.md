mkVMDK
======
This is simple python script to create a VMDK file for dd image. Send
bugs and feature request to warquel@gmail.com.

When using this script, make sure to use it on a COPY of your original
dd file. Accessing the image through VMWare is likely to change the
image.

Usage
=====
./mkVMDK -f <dd file>

Running this command against your file will output a valid VMDK file.
Output goes to stdout so you can redirect it to a file if you like.

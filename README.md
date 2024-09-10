Mebus' Code Snippets
=====================

Bash
----------

Execute a command for every line in a file:

```
while read in; do file "Camera/$in"; done < filtered.txt
```

SSH
----------

**Socks-Proxy:**

```
ssh -N -D7070 mebus@somehost.com
```

Disk
----------

```
du -sh --apparent-size .
```

Git
----------

```
  git add ':(exclude)*.pdf'
 
  git merge --allow-unrelated-histories project-a/master
```

KDE
----------

Refresh KDE Desktop Icons: F5


Libre Office
------------

Fix scaling issues:

```
QT_QPA_PLATFORM=xcb QT_SCALE_FACTOR=1 libreoffice 
```

Qemu
------

How to mount a qcow2 disk image:

This is a quick guide to mounting a qcow2 disk images on your host server. This is useful to reset passwords,
edit files, or recover something without the virtual machine running.

**Step 1 - Enable NBD on the Host**
    
    modprobe nbd max_part=8

**Step 2 - Connect the QCOW2 as network block device**

    qemu-nbd --connect=/dev/nbd0 /var/lib/vz/images/100/vm-100-disk-1.qcow2

**Step 3 - Find The Virtual Machine Partitions**

    fdisk /dev/nbd0 -l

**Step 4 - Mount the partition from the VM**

    mount /dev/nbd0p1 /mnt/somepoint/

**Step 5 - After you done, unmount and disconnect**

    umount /mnt/somepoint/
    qemu-nbd --disconnect /dev/nbd0
    rmmod nbd


Termux
-------

```
cd $PREFIX
```

Icinga
----------

```
icinga2 feature enable debuglog
icinga2 feature disable debuglog
```

Jekyll
----------

```
echo 256 > /proc/sys/fs/inotify/max_user_instances
```

LaTeX
----------

### Spellcheck

```
aspell --lang=en --mode=tex check file.tex
```

### TeXstudio

Jump to next placeholder: Ctrl + RightArrow

Insert equation: Ctrl + Shift + N

### Tools

 * https://mathpix.com/ - Take a screenshot of math and paste the LaTeX into your editor, all with a single keyboard shortcut.

mencoder
------------

Create movie from pictures:

```
mencoder "mf://*.jpg" -mf fps=10 -o fastoutput.avi -ovc copy
```

Python
----------

Remove all *.pyc files:

``` 
find . -name '*.pyc' -delete
```

Ripgrep
----------

Search for pattern including all .gitignored and hidden files: `rg -uu pattern`

Rsync
----------

```
rsync -chavP -zz -e "ssh -p 8022" mebus@192.168.42.42:/storage/giantdisk/ targetdir/
```

Faster variant without checksum calculation and compression:

```
rsync -havP -e "ssh -p 8022" mebus@192.168.42.42:/storage/giantdisk/ targetdir/
```

Windows
----------

See `windows.md`

VirtualBox
-----------

```
sudo rcvboxdrv setup
``` 

Visual Studio Code
-------------------

Settings:

```
"workbench.editor.enablePreview": false,
```

Samba / CIFS
-------------

Unmount stuck cifs mount:

```
sudo umount -a -t cifs -l
``` 

7zip
-----

```
7z a -p -m0=lzma2 -mx=9 -mhe=on -ms=on -t7z something.7z something/
```

Rust
------

```
source $HOME/.cargo/env
```


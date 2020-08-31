Mebus' Code Snippets
=====================

Bash
----------

Execute a command for every line in a file:

<code>
while read in; do file "Camera/$in"; done < filtered.txt
</code>

SSH
----------

**Socks-Proxy:**

<code>ssh -N -D7070 mebus@somehost.com</code>

Disk
----------

<code>du -sh --apparent-size .</code>

Git
----------

<code>
  git add ':(exclude)*.pdf'
 
  git merge --allow-unrelated-histories project-a/master
</code>

KDE
----------

Refresh KDE Desktop Icons: F5

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


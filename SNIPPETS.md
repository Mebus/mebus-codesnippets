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
</code>

KDE
----------

Refresh KDE Desktop Icons: F5

Termux
-------

```
cd $PREFIX
```

TeXstudio
----------

Jump to next placeholder: Ctrl + RightArrow

Insert equation: Ctrl + Shift + N

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

Windows
----------

Pfade für Laufwerksbuchstaben anzeigen:

```
net use
```

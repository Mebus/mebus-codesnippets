# Run Taskwarrior-Web with systemd

This document describes how to run [Taskwarrior-Web](https://github.com/theunraveler/taskwarrior-web) as a user systemd user-unit. This makes it possible to start it, when your computer starts.

Create the direcotry:

```
 mkdir -p ~/.config/systemd/user/
```

Edit the file `~/.config/systemd/user/taskwarrior-web.service` and paste the following lines:

```
[Unit]
Description=Taskwarrior-Web

[Service]
ExecStart=/usr/local/bin/task-web -o localhost -F -L
Restart=always
Environment=DISPLAY=:0

[Install]
WantedBy=basic.target
``` 

Enable the service by using the following commands:

```
cd ~/.config/systemd/user/
systemctl --user reenable *.service
```

Enable and start the service:

```
systemctl --user enable taskwarrior-web
systemctl --user start taskwarrior-web
```

Observe the status:

```
systemctl --user status taskwarrior-web
```

Go to http://localhost:5678/ to check if Taskwarrior-Web really works :-)

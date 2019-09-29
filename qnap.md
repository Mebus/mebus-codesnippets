# Qnap TS

## Fix the SSH server

### Start the server

Repair the SSH server on a Qnap TS NAS:

Install Entware:

https://github.com/Entware/Entware-ng/wiki/Install-on-QNAP-NAS

Connect via telnet to the NAS and run the following commands:

```
opkg install openssh-server
opkg install openssh-client
ssh-keygen -f /opt/etc/ssh/ssh_host_rsa_key -t rsa
ssh-keygen -f /opt/etc/ssh/ssh_host_ecdsa_key  -t dsa
ssh-keygen -f /opt/etc/ssh/ssh_host_ed25519_key  -t dsa ed25519
opt/Entware-ng.sh  start
ln -s /opt/etc/init.d/S40sshd /etc/init.d/S40sshd
```
### Fix Path

```
export PATH=/opt/bin:/opt/sbin:$PATH
```

## References 

* https://wiki.qnap.com/wiki/Replace_ssh_with_Qnapware_OpenSSH

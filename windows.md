# Windows

## Fix some stupid Windows things

### Allow Pings:

```
netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo request" protocol="icmpv4:8,any" dir=in action=allow
netsh advfirewall firewall add rule name="ICMP Allow incoming V6 echo request" protocol="icmpv6:8,any" dir=in action=allow
```

### Allow Remote Desktop Connections

```
netsh firewall set service type = remotedesktop mode = enable
```

## Network shares

Pfade für Laufwerksbuchstaben anzeigen:

```
net use
```

## Disable automatic updates in Windows 10

```
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Name NoAutoUpdate -Value 1
```

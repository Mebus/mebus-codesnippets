# Windows

## Fix some stupid Windows things

### Allow Pings:

```
netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo request" protocol="icmpv4:8,any" dir=in action=allow
netsh advfirewall firewall add rule name="ICMP Allow incoming V6 echo request" protocol="icmpv6:8,any" dir=in action=allow
```

## Network shares

Pfade für Laufwerksbuchstaben anzeigen:

```
net use
```

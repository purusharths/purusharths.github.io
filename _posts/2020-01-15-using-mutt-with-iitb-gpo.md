---
layout: post
title: "[Fedora] Using mutt for IIT Bombay GPO"
categories: fedora
---

Mutt is a terminal based email client. The following article talks about its configuration in Fedora systems. All due credit goes to [Prof. Madhu Belur](https://www.ee.iitb.ac.in/~belur/)

1. install `mutt` and `msmtprc` 
2. [configuration for .muttrc](https://www.ee.iitb.ac.in/~belur/foss/mutt/muttrc-iitgpo)
3. configuration for `~/.msmtprc`

```
defaults
auth on
tls on
logfile ~/.msmtp.log

account iitb
host smtp-auth.iitb.ac.in
port 587
from LDAP@iitb.ac.in
user LDAP username? 
password ### 

# Set a default account
account default : iitb
```

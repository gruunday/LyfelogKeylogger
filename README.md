## LyfeLog Keylogger

### Install

**Needs make and pip3 installed**

```bash
sudo make install
```

### Uninstall

```bash
sduo make uninstall
```


### Configure 

* To use you need an API key installed at `/etc/api.key`

```bash
echo "$API_KEY" > /etc/api.key
chown $USER:$GROUP /etc/api.key
chmod 600 /etc/api.key
```

## LyfeLog Keylogger

Monitor keystrokes locally

**Note:** This doesn't record keys pressed, just the amount of keys pressed every interval

Keystrokes are saved to /home/$USER/.keylogger/YEAR_MONTH_DAY.log


### Install

**Needs make and pip3 installed**

```bash
apt install python3-pip make
```

```bash
make build
```
**Note:** Execute with your user, not sudo

```bash
sudo make install
```
**Note:** You will probably need sudo now to install files correctly



### Uninstall

```bash
sduo make uninstall
```


### Debuging

* Check if the daemon is running 

```bash
systemctl status keylogger.service
```

* Restart daemon if it is crashed

```bash
systemctl restart keylogger.service
```

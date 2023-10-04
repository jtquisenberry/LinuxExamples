# Setup Development Environment

## Snap Service

```
$ sudo apt install snapd
```

## Snap Store App

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


## PyCharm Community

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
$ sudo gdebi GitHubDesktop-linux-3.1.1-linux1.deb
```

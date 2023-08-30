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

## Firefox

```
$ sudo snap install firefox
$ firefox
```
Some dialogs in Firefox require additional packages. https://github.com/flatpak/flatpak/issues/2446 

```
$ sudo xdg-desktop-portal
$ sudo xdg-desktop-portal-gtk
```

## Chrome



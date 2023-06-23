# Mounting UNC Path

Create credentials file.

```
$ sudo nano /root/.smbcredentials
```

Edit the credentials file to contain the following.

Credentials are the credentials need to access the file share.

```
username=my_username
password=my_password
domain=my_domain
```

Create a mount point.

```
$ mkdir my_mount_point
```

Edit `/etc/fstab/`

```
//<UNC path>/destinationlocation /mnt/my_mount_point/destinationlocation cifs credentials=/root/.smbcredentials,iocharset=utf8,file_mode=0755,dir_mode=0755 0 0
```

Mount all

```
$ sudo mount -a
```

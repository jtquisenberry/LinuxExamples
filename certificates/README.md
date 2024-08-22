# Certificates

For examples, assume the certifcate is named `ZscalerRootCertificate-2048-SHA256.crt` and that its format is PEM.

# Installation

```
$ sudo apt-get install -y ca-certificates
$ sudo cp ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates
$ sudo update-ca-certificates
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
```

https://forum.snapcraft.io/t/custom-ssl-certs-for-snapd-to-the-snap-store-communication/17446

## 0 added, 0 removed;

If `update-ca-certificates` does not add or remove certificates, try re-running it with the `-f` (fresh) option. https://superuser.com/questions/1328413/removing-certificate-and-re-running-update-ca-certificates-leaves-lingering-syml

```
$ sudo update-ca-certificates -f
```

## Error x509 with snap

I requests to `snap` fail and the error messages is like the following:

```
error: cannot install "snap-store": Post
       https://api.snapcraft.io/v2/snaps/refresh: x509: certificate signed by
       unknown authority
```
This solution may fix the issue.

```
sudo dpkg-reconfigure ca-certificates
sudo systemctl restart snapd
sudo snap refresh
```
https://askubuntu.com/questions/1284728/installed-ubuntu-20-04-from-0-x509-certificate-signed-by-unknown-authority-er


# Pip

For one installation.

```
$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pandas
```

Global option.

```
pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"
python -m pip install pandas

```


# snap and snap-store

```
$ sudo cp ZscalerRootCertificate-2048-SHA256.crt /etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem
$ sudo snap set system store-certs.cert1="$(cat /etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem)"
$ sudo snap get system store-certs.cert1
-----BEGIN CERTIFICATE-----
...
$ sudo snap install snap-store
```

# Firefox 

Firefox may display:

<block> www.wikipedia.org is most likely a safe site, but a secure connection could not be established. This issue is caused by Zscaler Root CA, which is either software on your computer or your network. </block>

Install the certificate within Firefox.

```
Hamburger -> Settings -> Privacy & Security -> View Certificates -> Import

```

https://www.lifewire.com/pem-file-4147928


# Chrome

```
Three dots -> Settings -> Privacy and Security -> Security -> Manage certificates
```
Install the certificate.


# Links

https://ubuntu.com/server/docs/security-trust-store

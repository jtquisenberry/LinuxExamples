# Certificates

For examples, assume the certifcate is named `ZscalerRootCertificate-2048-SHA256.crt` and that its format is PEM.

# Installation

```
$ sudo apt-get install -y ca-certificates
$ sudo cp ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates
$ sudo update-ca-certificates
```

https://forum.snapcraft.io/t/custom-ssl-certs-for-snapd-to-the-snap-store-communication/17446

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



# Links

https://ubuntu.com/server/docs/security-trust-store

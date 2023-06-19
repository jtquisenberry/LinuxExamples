# Certificates

For examples, assume the certifcate is named `ZscalerRootCertificate-2048-SHA256.crt` and that its format is PEM.

# Installation

```
$ sudo apt-get install -y ca-certificates
$ sudo cp ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates
$ sudo update-ca-certificates
```

# snap and snap-store

```
$ sudo cp ZscalerRootCertificate-2048-SHA256.crt /etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem
$ sudo snap set system store-certs.cert1="$(cat /etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem)"
$ sudo snap get system store-certs.cert1
-----BEGIN CERTIFICATE-----
...
```




# Links

https://ubuntu.com/server/docs/security-trust-store

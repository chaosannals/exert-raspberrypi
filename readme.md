# exert raspberrypi

```cmd
# 假设 192.168.1.101 为树莓派 IP
# 复制 SSH 公钥 到树莓派上
scp ~\.ssh\id_rsa.pub pi@192.168.1.101:~/.ssh/authorized_keys
```

 
放 wpa_supplicant.conf 在根目录下配置网络。

# Simple DNS Proxy

Allows you to customize response to selected DNS queries

# Usage

1. Clone the repository or download `dns_proxy.py`
2. Customize the configuration and responses in `dns_proxy.py`
3. Execute `dns_proxy.py` (e.g. `sudo python dns_proxy.py`)

# Examples

**Customized response for pfghmj.com:**
```
$ dig pfghmj.com @localhost

; <<>> DiG 9.10.3-P4-Ubuntu <<>> pfghmj.com @localhost
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5307
;; flags: qr aa rd ra ad; QUERY: 1, ANSWER: 5, AUTHORITY: 2, ADDITIONAL: 2

;; QUESTION SECTION:
;pfghmj.com.			IN	A

;; ANSWER SECTION:
pfghmj.com.		136	IN	A	239.136.254.248
pfghmj.com.		136	IN	A	98.45.51.8
pfghmj.com.		136	IN	A	70.58.60.21
pfghmj.com.		136	IN	A	165.203.213.15
pfghmj.com.		136	IN	A	210.53.31.233

;; AUTHORITY SECTION:
pfghmj.com.		128505	IN	NS	ns1.mecadasome.com.
pfghmj.com.		128505	IN	NS	ns2.mecadasome.com.

;; ADDITIONAL SECTION:
ns1.mecadasome.com.	157982	IN	A	45.116.79.94
ns2.mecadasome.com.	157982	IN	A	45.116.79.94

;; Query time: 53 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Fri Jul 15 12:46:34 SGT 2016
;; MSG SIZE  rcvd: 187
```

**Standard response for all other queries:**
```
$ dig microsoft.com @localhost

; <<>> DiG 9.10.3-P4-Ubuntu <<>> microsoft.com @localhost
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11478
;; flags: qr aa rd ra ad; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;microsoft.com.			IN	A

;; ANSWER SECTION:
microsoft.com.		710	IN	A	23.96.52.53
microsoft.com.		710	IN	A	23.100.122.175
microsoft.com.		710	IN	A	104.43.195.251
microsoft.com.		710	IN	A	104.40.211.35
microsoft.com.		710	IN	A	191.239.213.197

;; Query time: 16 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Fri Jul 15 12:55:17 SGT 2016
;; MSG SIZE  rcvd: 111
```

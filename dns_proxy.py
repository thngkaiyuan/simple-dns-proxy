from dnslib import *
from dnslib import server

# Customize the port and address of your local server to suit your needs (e.g. localhost -> 0.0.0.0)
local_addr = 'localhost'
local_port = 53

# Customize the address and port of the external DNS server
external_dns_server_addr = '192.168.20.1'
external_dns_server_port = 53

class SpecialResolver:
    def resolve(self, request, handler):
        d = request.reply()
        q = request.get_q()
        q_name = str(q.qname)
        
        # Custom response for 'pfghmj.com' and 'carvezine.com'
        if 'pfghmj.com' in q_name or 'carvezine.com' in q_name:
            # Answers
            d.add_answer(*RR.fromZone("pfghmj.com 136 A 239.136.254.248"))
            d.add_answer(*RR.fromZone("pfghmj.com 136 A 98.45.51.8"))
            d.add_answer(*RR.fromZone("pfghmj.com 136 A 70.58.60.21"))
            d.add_answer(*RR.fromZone("pfghmj.com 136 A 165.203.213.15"))
            d.add_answer(*RR.fromZone("pfghmj.com 136 A 210.53.31.233"))
            
            # Authoritative Name Servers
            d.add_auth(*RR.fromZone("pfghmj.com 128505 NS ns1.mecadasome.com"))
            d.add_auth(*RR.fromZone("pfghmj.com 128505 NS ns2.mecadasome.com"))
            
            # Additional Records
            d.add_ar(*RR.fromZone("ns1.mecadasome.com 157982 A 45.116.79.94"))
            d.add_ar(*RR.fromZone("ns2.mecadasome.com 157982 A 45.116.79.94"))

        # Recursively query another DNS server for other domains
        else:
            a = DNSRecord.parse(DNSRecord.question(q_name).send(external_dns_server_addr, external_dns_server_port))
            for rr in a.rr:
                d.add_answer(rr)
        return d

r = SpecialResolver()
s = server.DNSServer(r, port=local_port, address=local_addr)
s.start_thread()

while True:
    pass

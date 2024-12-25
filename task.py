import os
import docker

def create_honeypot(name, image, port_mapping):
    """Honeypot üçün Docker konteyneri yaradılması"""
    client = docker.from_env()
    try:
        container = client.containers.run(
            image,
            name=name,
            ports=port_mapping,
            detach=True
        )
        print(f"Honeypot {name} yaradıldı və işlədirilir.")
    except Exception as e:
        print(f"Səhv: {e}")

# Honeynet parametrləri
honeypots = [
    {
        "name": "honeypot1", 
        "image": "dionaea/dionaea", 
        "port_mapping": {"21/tcp": 21, "80/tcp": 80}
    },
    {
        "name": "honeypot2", 
        "image": "cowrie/cowrie", 
        "port_mapping": {"22/tcp": 2222}
    },
]

for honeypot in honeypots:
    create_honeypot(honeypot["name"], honeypot["image"], honeypot["port_mapping"])
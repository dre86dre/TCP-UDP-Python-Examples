# TCP & UDP Python Examples

This repository contains tiny Python exercises that demonstrate how TCP and UDP work in practice. They’re simple enough to run locally and are a great way to understand the difference between reliable (TCP) and fast but unreliable (UDP) communication.

---

## 📦 Contents

- ```tcp_server.py``` → Simple TCP server
- ```tcp_client.py``` → Simple TCP client
- ```udp_server.py``` → Simple UDP server
- ```udp_client.py``` → Simple UDP client

---

## 🚀 Getting Started

### 1. Clone the Repository

```git clone https://github.com/dre86dre/TCP-UDP-Python-Examples.git```

### 2. Run the TCP Example

In one terminal, start the server:

```cd tcp_example```

```python tcp_server.py```

In another terminal, run the client:

```python tcp_client.py```

You should see:

Server side → ```Received: Hello TCP Server!```

Client side → ```Server says: Hello from TCP server!```


✅ Messages are delivered reliably and in order.

---
---

### 3. Run the UDP Example

In one terminal, start the server:

```cd udp_example```

```python udp_server.py```

In another terminal, run the client:

```python udp_client.py```

You should see:

Server side → Received: Hello UDP Server! from ('127.0.0.1', <random_port>)
Client side → Server says: Hello from UDP server!


⚠️ UDP is faster but does not guarantee delivery or ordering. If packets are dropped, they won’t be retried.

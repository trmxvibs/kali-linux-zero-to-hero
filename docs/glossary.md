# Glossary

Plain-language definitions for terms used throughout this course. Each term
links to the module where it's covered in depth, if applicable.

**IP (IP Address)** — A numeric address identifying a device on a network, roughly like a postal address. See [Module 08](../modules/08-networking-fundamentals/README.md).

**Port** — A number (0–65535) identifying a specific service on a device with a given IP address, like an apartment number at a street address. See Module 08.

**Protocol** — An agreed-upon set of rules for how two systems communicate (e.g., TCP, HTTP, DNS).

**Socket** — The combination of an IP address, a port, and a protocol — the specific "endpoint" a program communicates through.

**Packet** — A chunk of data formatted according to a network protocol, sent across a network.

**DNS (Domain Name System)** — The system that translates human-readable names (`example.com`) into IP addresses. See Module 08.

**TCP (Transmission Control Protocol)** — A connection-oriented, reliable transport protocol; establishes a connection via a three-way handshake before sending data. See Module 08.

**UDP (User Datagram Protocol)** — A connectionless transport protocol; faster than TCP but with no delivery guarantee. See Module 08.

**HTTP / HTTPS** — The protocol web browsers and servers use to exchange requests and responses; HTTPS adds TLS encryption. See [Module 14](../modules/14-web-security-fundamentals/README.md).

**TLS (Transport Layer Security)** — The cryptographic protocol that encrypts HTTPS (and other) traffic, protecting it from eavesdropping and tampering in transit.

**Firewall** — A system that allows or blocks network traffic based on defined rules. See [Module 17](../modules/17-defensive-security/README.md).

**Vulnerability** — A weakness in a system that could be exploited to cause an unintended, harmful outcome. See [Module 15](../modules/15-vulnerability-assessment/README.md).

**Exploit** — A specific technique or piece of code that takes advantage of a vulnerability to produce a specific (usually unintended) effect.

**Payload** — The part of an exploit that performs the actual intended action once a vulnerability has been leveraged (e.g., opening a shell).

**Authentication** — Proving *who* you are (e.g., a username/password, a key).

**Authorization** — Determining *what* an authenticated identity is allowed to do.

**Privilege** — The level of access or capability granted to a user or process (e.g., "root privilege" = full system access).

**Enumeration** — The process of actively gathering detailed information about a target once it's known to exist (e.g., listing users, shares, or service versions). See [Module 12](../modules/12-network-enumeration/README.md).

**Reconnaissance ("recon")** — The information-gathering phase before testing, split into passive (no direct interaction) and active (direct interaction). See [Module 11](../modules/11-reconnaissance-concepts/README.md).

**CIDR (Classless Inter-Domain Routing)** — Notation like `192.168.1.0/24` describing a range of IP addresses and how many bits are fixed vs. variable. See Module 08.

**NAT (Network Address Translation)** — A technique letting many devices share one public IP address by rewriting packet addresses at a router. See Module 08.

**SUID (Set User ID)** — A file permission bit that makes a program run with its *owner's* privileges rather than the invoking user's — security-relevant because misconfigured SUID binaries are a common privilege-escalation path. See [Module 04](../modules/04-filesystem-and-permissions/README.md) and [Module 20](../modules/20-exploitation-concepts-safe-labs/README.md).

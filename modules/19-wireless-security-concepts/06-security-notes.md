# Security Notes — Module 19

- **WEP should never be used.** Any network still running WEP can be fully compromised in minutes with public, widely-available tools — not a theoretical claim, a practical fact that has been true since 2001.
- **WPA2-Personal's primary weakness is password quality.** A 20+ character random password makes the offline dictionary attack computationally infeasible with current hardware; a common word or short password makes it trivial. This is the single most actionable defensive recommendation from this module.
- **Enterprise-mode authentication (WPA2/WPA3-Enterprise, using 802.1X and a RADIUS server) avoids the shared PSK problem entirely** — each user has their own credentials, revocable independently. Out of scope for this course but worth knowing as the next step beyond PSK for organizations.
- **Deauthentication attacks (forcing clients to disconnect) remain possible in WPA2**; WPA3 addresses this with Management Frame Protection (MFP). This is one reason to prefer WPA3 where all client devices support it.

> ⚠️ **LAB ONLY** — everything in this module is for your own wireless network exclusively.

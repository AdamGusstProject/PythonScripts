# Windows Defender Firewall Rule Auditor

A lightweight Python tool for analyzing exported Windows Defender Firewall rules and identifying potential security risks.

## Purpose
Windows systems accumulate firewall rules over time — many become outdated, duplicated, or overly permissive. This tool helps you quickly review those rules and highlight anything that may weaken system security.

## Features
- Load inbound or outbound firewall rule exports (CSV)
- Normalize key fields (ports, addresses, profiles, program paths)
- Highlight risky rules (e.g., Any→Any, Public profile, wide-open ports)
- Detect duplicate rules
- Search rules by port or program name
- Summarize enabled/disabled rule counts
- Generate a full audit report with readable, high‑value output

## Input
Provide exported Windows Defender Firewall rules in CSV format.  
Both inbound and outbound rule exports are supported.

## Future Enhancements
- More advanced risk scoring
- Cleanup and remediation recommendations
- Support for additional firewalls (ASA, Palo Alto, etc.)

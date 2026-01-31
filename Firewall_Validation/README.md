## Windows Defender Firewall Rule Auditor

A small Python tool that analyzes exported Windows Defender firewall rules and highlights potential security risks.

## Purpose

Windows systems collect lots of firewall rules over time. Many are unnecessary, duplicated, or overly permissive. This tool helps you review those rules and spot anything that might weaken your security.

## What It Does

- Loads inbound and outbound firewall rule exports
- Normalizes fields like ports, addresses, and profiles
- Flags risky rules (e.g., “Any → Any”, Public profile, wide‑open ports)
- Detects duplicates and unnecessary entries
- Creates simple, readable summaries of each rule

## Input

Use exported Windows Defender firewall rules (CSV or text).
Your inbound and outbound files work perfectly.
Planned Structure

firewall-auditor/
  src/
    parser.py
    risk_engine.py
    report.py
    main.py
  data/
  README.md


## Future Ideas
- Better risk scoring
- Cleanup recommendations
- Support for other firewalls (ASA, Palo Alto, etc.)

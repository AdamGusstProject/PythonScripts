# Log File Analyzer (Security‑Focused)

A Python tool for analyzing Linux syslog‑style log files and extracting security‑relevant events such as authentication failures and firewall blocks.
Designed to reinforce clean architecture, modular parsing, and real‑world cybersecurity workflows.

## Current Features (In Progress)

- Parse Linux syslog‑style lines
- Identify security‑focused events
- Failed SSH logins
- UFW firewall blocks
- Extract useful fields (timestamp, process, IPs, message text)
- Prepare data for summary and frequency analysis

## Architecture (Early Stage)

log_analyzer/
│
├── main.py               # Program entry point
└── parsers/
    └── syslog_parser.py  # Parser for syslog-style logs


The project is structured to support multiple log types in the future through modular parser files.

## Purpose

This project is part of a hands‑on learning journey to strengthen:
- Python fundamentals
- parsing and classification logic
- modular program design
- security event analysis

## Future Plans

- Add summary output
- Count failed logins and firewall blocks
- Identify top attacker IPs
- Detect repeated attempts
- Add additional parsers (custom logs, Apache, Windows, etc.)

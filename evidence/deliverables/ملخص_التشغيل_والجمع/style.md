# Style plan

- **Style name:** Operations Evidence Board / لوحة تشغيل ودليل.
- **Keywords:** operational, evidence, status, modular, security.
- **Description:** A compact Arabic evidence board, not a promotional infographic. Four repository lanes separate self-hosted components, external dependencies, and production status. A lower threat matrix shows what security tests do and do not prove, followed by a simple API/MCP composition path.
- **Fonts:** Noto Kufi Arabic for headings and status labels; Noto Sans Arabic for body text. Repository and component names remain English.
- **Palette:** Deep graphite `#10151D`, panels `#182230`, off-white `#F3EEE6`, muted `#9AA9B9`, green `#62D4A4`, amber `#F0B65B`, red `#F07D78`, blue `#72A9F8`.
- **Layout:** Vertical 1080×1640. Clear verdict band, four evidence lanes, an external-services strip, a security coverage matrix, and a bottom composition chain. No stock imagery, no animation, no decorative AI graphics.
- **Core rule:** Only tests with real command output may be labelled PASS. Everything else uses SELF-HOSTED SOURCE, EXTERNAL, DEMO, CANDIDATE, BLOCKED, or NOT VERIFIED.

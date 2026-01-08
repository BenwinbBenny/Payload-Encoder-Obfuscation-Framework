# Payload Encoding, Masking, and Detection Analysis Framework

## 1. Introduction
  This Python project implements a **modular framework for studying payload transformation techniques** including encoding, masking, and obfuscation and how such transformations interact with simple signature-based detection logic.
  
The framework is designed for:

- Cybersecurity researchers
- Red team and blue team practitioners
- Secure coding and detection engineering education

It focuses on conceptual analysis, not exploitation, and demonstrates how textual indicators can be altered to affect detection outcomes.

## 2. Design Goals
- Provide clear separation of responsibilities between components
- Enable repeatable experimentation with deterministic transformations
- Model basic detection evasion scenarios
- Produce structured audit artifacts for analysis

## 3. High-Level Architecture

```bash
Input Payload
     ↓
[ EncoderEngine ] ──► Encoded Variants
     ↓
[ TextMasker ] ─────► Masked Variants
     ↓
[ ThreatScanner ] ──► Detection Comparison
     ↓
[ AuditLog ] ───────► Structured Report
```
Each component is independent and can be extended or replaced without impacting others.

## 4. Module-Level Documentation

### 4.1 main.py
### Purpose
Acts as the entry point for the framework. It orchestrates the encoding, masking, scanning, and logging processes.
### Execution Flow
1. Display framework banner
2. Define sample input
3. Initialize core components
4. Apply transformations
5. Compare detection results
6. Generate and display execution summary
### Code Walkthrough
```bash
sample = "status_check" #Defines the input payload to be analyzed.

encoder = EncoderEngine()
masker = TextMasker(seed=7)
scanner = ThreatScanner()
logger = AuditLog()  #Initializes framework components. The seed ensures deterministic masking.

encoded = encoder.base64_wrap(sample)
masked = masker.reverse_text(sample)  #Applies encoding and masking transformations.

scan = scanner.compare(sample, masked) #Compares detection results between raw and transformed input.

report = logger.build(...) #Builds a structured audit report.
```
### 4.2 encoder_engine.py
### Class: EncoderEngine

Provides reversible encoding and masking techniques commonly encountered in payload transformation scenarios.

### Method: base64_wrap(text: str) -> str
Encodes input text using Base64.

- Input: Plain string
- Output: Base64-encoded string
- Use Case: Obfuscating readable strings while preserving reversibility
  
### Method: base64_unwrap(text: str) -> str
Decodes Base64-encoded input back to plaintext.

### Method: rot_cipher(text: str) -> str
Applies ROT13 substitution cipher.

- Purpose: Demonstrates simple alphabetic substitution obfuscation
- Reversible: Yes (ROT13 is symmetric)

### Method: xor_mask(text: str, key: str = "veil") -> str
Reverses XOR masking and restores original plaintext.

### 4.3 masker.py
### Class: TextMasker
Applies non-cryptographic transformations designed to disrupt static pattern matching.

### Constructor: __init__(seed: int | None = None)

- Optional seed ensures deterministic output
- Useful for testing and reproducibility

### Method: reverse_text(text: str) -> str
### Example:
```
status_check → kcehc_sutats
```

### Method: inject_noise(text: str, amount: int | None = None) -> str
- Randomly inserts alphanumeric characters into the string.
- Default noise amount is proportional to input length
- Designed to break substring matching

### Method: fragment_text(text: str) -> str
Splits text into concatenated character fragments.

### Method: unicode_mask(text: str) -> str
Encodes each character as a Unicode escape sequence.

### 4.4 scanner.py

### Class: ThreatScanner

Simulates a signature-based detection engine using predefined string indicators.

### Detection Categories
```
admin_login
config_update
debug_mode
auth_token
service_restart #Operational Indicators

override
bypass
elevate
inject #High-Risk Action Keywords
```
### Method: compare(raw: str, transformed: str) -> dict
```
#Compares scan results between original and transformed input.
{
  "raw_flagged": true | false,
  "masked_flagged": true | false,
  "bypass": true | false
}

bypass = raw_flagged and not masked_flagged #Bypass Logic

```

### 4.5 audit_log.py
### Class: AuditLog
Responsible for report generation and persistence.

### Method: build(...) -> Dict[str, Any]
Generates a structured audit report.

Fields:

- generated_at – ISO timestamp
- input – Original payload
- artifacts – Transformation outputs
- scan – Detection comparison results
- status – "bypass-achieved" or "detected"

### Method: export(report, path)
  Exports report to a JSON file.

- Uses formatted indentation
- Suitable for SIEM ingestion or analysis pipelines

## 5. Example Execution Output
```
===Payload-Encoder-Obfuscation-Framework===

Input Text      : status_check
Encoded Output  : c3RhdHVzX2NoZWNr
Masked Output   : kcehc_sutats
Scan Result     : {'raw_flagged': False, 'masked_flagged': False, 'bypass': False}

Execution complete
```

## 6. Example Audit Report
```
{
  "generated_at": "2026-01-08T14:32:10.481239",
  "input": "status_check",
  "artifacts": {
    "base64": "c3RhdHVzX2NoZWNr",
    "reversed": "kcehc_sutats"
  },
  "scan": {
    "raw_flagged": false,
    "masked_flagged": false,
    "bypass": false
  },
  "status": "detected"
}
```

## 7. Extensibility Considerations

This framework can be extended by:

- Adding entropy-based or heuristic scanners
- Implementing decoding-aware detection logic
- Introducing transformation pipelines
- Exporting results to CSV or databases
- Adding unit tests for each transformation

## 8. Ethical & Usage Disclaimer

This project is intended solely for educational and defensive security research. It does not include exploit code or operational attack logic. Users are responsible for ethical and lawful use.


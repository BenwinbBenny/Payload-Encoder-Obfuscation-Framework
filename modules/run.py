def main():
    print("\n===Payload-Encoder-Obfuscation-Framework===\n")

    sample = "status_check"   

    encoder = EncoderEngine()
    masker = TextMasker(seed=7)
    scanner = ThreatScanner()
    logger = AuditLog()

    encoded = encoder.base64_wrap(sample)
    masked = masker.reverse_text(sample)

    scan = scanner.compare(sample, masked)

    report = logger.build(
        sample,
        {
            "base64": encoded,
            "reversed": masked,
        },
        scan,
    )

    print("Input Text      :", sample)
    print("Encoded Output  :", encoded)
    print("Masked Output   :", masked)
    print("Scan Result     :", scan)
    print("\nExecution complete\n")



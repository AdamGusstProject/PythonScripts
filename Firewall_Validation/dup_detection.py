def dup_detection(fw_rules):
    signatures = {}
    index = 2
    for line in fw_rules:
        rule = normalized_rule(line)
        sig = strict_signature(rule)
        if sig not in signatures:
            signatures[sig] = [index]
        else:
            signatures[sig].append(index)


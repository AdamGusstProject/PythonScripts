def enable_disable_sumary(fw_rules):
    enabled_counter = 0
    disabled_counter = 0
    for line in fw_rules:
        if enable_disable(line) == 1:
            enabled_counter += 1
        else:
            disabled_counter += 1

    return enabled_counter, disabled_counter

def format_seconds(secs: int) -> str:
    for unit in ["s", "ms", "μs", "ns"]:
        if 1 < secs:
            break
        else:
            secs *= 1000

    return f"{secs:.2f} {unit}"

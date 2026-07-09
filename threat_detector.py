def detect_threat(text):

    text = text.lower()

    if any(keyword in text for keyword in [
        "phishing",
        "fake link",
        "bank link",
        "login page",
        "credential",
        "fake website"
    ]):
        return "Phishing", "High"

    elif any(keyword in text for keyword in [
        "ransomware",
        "encrypted files",
        "bitcoin payment",
        "locked files"
    ]):
        return "Ransomware", "Critical"

    elif any(keyword in text for keyword in [
        "virus",
        "trojan",
        "malware",
        "spyware"
    ]):
        return "Malware", "High"

    elif any(keyword in text for keyword in [
        "whatsapp hacked",
        "facebook hacked",
        "instagram hacked",
        "account hacked",
        "email hacked"
    ]):
        return "Account Compromise", "High"

    elif any(keyword in text for keyword in [
        "sim swap",
        "sim card"
    ]):
        return "SIM Swap Fraud", "Critical"

    else:
        return "General Security Question", "Low"
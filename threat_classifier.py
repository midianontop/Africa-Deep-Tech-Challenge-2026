def classify_threat(question):

    q = question.lower()

    # Account compromise
    if any(word in q for word in [
        "hacked",
        "hack",
        "stolen account",
        "compromised account",
        "whatsapp hacked",
        "facebook hacked",
        "gmail hacked"
    ]):
        return "Account Compromise", "High"

    # Phishing
    elif any(word in q for word in [
        "phishing",
        "fake email",
        "fake message",
        "scam link",
        "fraud link"
    ]):
        return "Phishing Attack", "High"

    # Malware
    elif any(word in q for word in [
        "virus",
        "trojan",
        "malware",
        "ransomware",
        "worm"
    ]):
        return "Malware Infection", "High"

    # SIM swap
    elif any(word in q for word in [
        "sim swap",
        "sim card",
        "otp stolen"
    ]):
        return "SIM Swap Fraud", "Critical"

    # Password issues
    elif any(word in q for word in [
        "password",
        "login",
        "authentication",
        "2fa"
    ]):
        return "Authentication Issue", "Medium"

    else:
        return "General Security Question", "Low"
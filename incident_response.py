def get_incident_response(threat_type):

    responses = {

        "Account Compromise": [
            "Change your password immediately.",
            "Enable Two-Factor Authentication (2FA).",
            "Log out from all active sessions.",
            "Check for unauthorized account activity.",
            "Notify contacts if your account was used maliciously."
        ],

        "Phishing Attack": [
            "Do not click suspicious links.",
            "Change passwords for affected accounts.",
            "Enable Two-Factor Authentication.",
            "Report the phishing message.",
            "Monitor accounts for unusual activity."
        ],

        "Malware Infection": [
            "Disconnect the device from the internet.",
            "Run a malware scan.",
            "Remove suspicious applications.",
            "Update your operating system.",
            "Restore files from backups if necessary."
        ],

        "SIM Swap Fraud": [
            "Contact your mobile network immediately.",
            "Freeze affected bank accounts.",
            "Change passwords on critical accounts.",
            "Enable app-based authentication where possible.",
            "Report the incident to authorities."
        ],

        "Authentication Issue": [
            "Reset your password.",
            "Enable Two-Factor Authentication.",
            "Review login history.",
            "Remove unknown devices.",
            "Update recovery information."
        ],

        "General Security Question": [
            "Follow cybersecurity best practices.",
            "Keep systems updated.",
            "Use strong passwords.",
            "Enable Two-Factor Authentication.",
            "Stay alert for suspicious activity."
        ]
    }

    return responses.get(
        threat_type,
        ["No incident response available."]
    )
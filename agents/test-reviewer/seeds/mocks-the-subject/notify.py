import smtplib

def send_alert(to: str, msg: str) -> bool:
    with smtplib.SMTP("localhost") as s:
        s.sendmail("alerts@example.com", [to], msg)
    return True

def alert_if_over(value: float, limit: float, to: str) -> bool:
    if value > limit:
        return send_alert(to, f"{value} exceeds {limit}")
    return False

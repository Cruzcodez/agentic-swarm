from unittest.mock import patch
import notify

def test_alert_if_over():
    with patch("notify.alert_if_over", return_value=True) as m:
        assert notify.alert_if_over(10, 5, "ops@example.com") is True
        m.assert_called_once()

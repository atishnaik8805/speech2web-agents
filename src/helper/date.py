from datetime import datetime, timedelta


# Obtains date based on context
SUPPORTED_DATE_TOKENS: list[str] = ["today", "tomorrow", "yesterday"]


def _generate_date_from_token(token: str) -> datetime:
  token = token.lower().strip()
  if token == "today":
    return datetime.now()
  elif token == "yesterday":
    return datetime.now() - timedelta(days=1)
  elif token == "tomorrow":
    return datetime.now() + timedelta(days=1)
  else:
    print(f"helper > date.py > [WARNING] Only {SUPPORTED_DATE_TOKENS} tokens are accepted")
    print("helper > date.py > [WARNING] Defaulting to 'today'")
    return datetime.now()


def _humanize_date(date: datetime) -> str:
  return date.strftime("%B %d, %Y")


def parse_date_from_token(token: str) -> str:
  date: datetime = _generate_date_from_token(token)
  return _humanize_date(date)

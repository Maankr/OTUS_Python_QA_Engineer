import re

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - '
    r'\[(?P<time>.*?)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>.*?)" '
    r'(?P<status>\d+) '
    r'(?P<bytes>\S+) '
    r'"(?P<referer>.*?)" '
    r'"(?P<agent>.*?)" '
    r'(?P<duration>\d+)'
)


def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    return match.groupdict()
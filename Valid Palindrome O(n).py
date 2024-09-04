def isPalindrome(self, s: str) -> bool:
    processed = ''

    for char in s:
        if char.isalnum():
            processed += char.lower()

    return processed == processed[:: -1]

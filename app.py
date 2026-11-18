import re

print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
checks = [
    (len(password) >= 8, "At least 8 characters"),
    (bool(re.search(r"[A-Z]", password)), "Contains uppercase letter"),
    (bool(re.search(r"[a-z]", password)), "Contains lowercase letter"),
    (bool(re.search(r"\d", password)), "Contains a number"),
    (bool(re.search(r"[^A-Za-z0-9]", password)), "Contains a special character"),
]
score = sum(ok for ok, _ in checks)
print("\nChecklist:")
for ok, label in checks:
    print(f"{'✓' if ok else '✗'} {label}")
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"
print(f"\nPassword strength: {strength} ({score}/5)")

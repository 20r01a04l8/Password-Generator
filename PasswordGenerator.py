import random
import string

def get_user_prefs():
    print("Customize your password: ")
    length = 0
    while length < 4:
        try:
            length = int(input("Enter the length of your password(at least 4): "))
            if length < 4:
                print("Password length must be at least 4 characters. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("Include in password? (y/n)")
    use_upper = input("Uppercase letters: ").lower() == "y"
    use_lower = input("Lowercase letters: ").lower() == "y"
    use_digits = input("Digits: ").lower() == "y"
    use_special = input("Special characters: ").lower() == "y"
    # Always include at least one type; fallback to lowercase if none
    if not any([use_upper, use_lower, use_digits, use_special]):
        print("No set selected, using lowercase letters by default.")
        use_lower = True
    num_pwds = 1
    try:
        num_pwds = int(input("How many passwords would you like to generate? "))
    except ValueError:
        pass
    return length, use_upper, use_lower, use_digits, use_special, max(1, num_pwds)

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Define the possible characters
    charsets = []
    if use_upper: charsets.append(string.ascii_uppercase)
    if use_lower: charsets.append(string.ascii_lowercase)
    if use_digits: charsets.append(string.digits)
    if use_special: charsets.append(string.punctuation)

    all_chars = ''.join(charsets)
    # Ensure at least one from each selected set

    password = [random.choice(charset) for charset in charsets]

    #Fill rest randomly
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

def password_strength(pwd):
    score = 0
    if any(c.isupper() for c in pwd): score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1
    if len(pwd) >= 12: score += 1
    return ["Weak", "Moderate", "Strong", "Very Strong", "Excellent"][min(score,4)]

def main():
    print("Welcome to the custom Password Generator!")
    length, up, low, dig, spe, num_pwds = get_user_prefs()
    print(f"\nGenerated passwords(s):")
    for _ in range(num_pwds):
        pwd = generate_password(length, up, low, dig, spe)
        print(f"{pwd} ({password_strength(pwd)})")

if __name__ == "__main__":
    main()

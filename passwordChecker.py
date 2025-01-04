import requests
import hashlib
def check_password_strength(password):
    score=0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
       score+=1
    if any(char.islower() for char in password):
      score+=1
    if any(char.isdigit() for char in password):
      score+=1
    if any(char in "~!@#$%^&*()-_+=}{[]|;:'<>,./?" for char in password):
      score+=1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"
def getSHA1(password):
   sha1=hashlib.sha1(password.encode())
   return sha1.hexdigest().upper()
      
def checkPwned(password):
   hash=getSHA1(password)
   firstFive, tail= hash[:5], hash[5:]
   url = f"https://api.pwnedpasswords.com/range/{firstFive}"
   response = requests.get(url)
   if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

   return tail in response.text

def main():
    print("Welcome to Password Strength Checker")
    password = input("Enter your password: ")
    strength= check_password_strength(password)
    print(f"Password Strength: {strength}")
    check = input("Would u like to check if your password is leaked or not (y/n):")
    if check== 'y':
        if checkPwned(password):
            print("Your password has been leaked! Choose a stronger one.")
        else:
            print("Your password is safe (for now).")
    else:
       print("Exiting...")
       exit()

if __name__ == "__main__":
    main()
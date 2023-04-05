def main():
    print("Welcome to E-Mail Verfier!")
    print("")
  # ahmadpanah@gmail.com
    email_input = input("type your Email: ")
    (username , domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: " , username)
    print("Domain: " , domain)
    print("Extension: " , extension)

while True:
    main()
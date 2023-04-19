import urllib.request as urllib

def main(url):
    print("Checking Connectivity...")

    response = urllib.urlopen(url)
    print("Connected to " , url, "Successfully.")
    print("The Response Code is:" , response.getcode())

print("This is Connectivity Checker")
input_url = input("Input URL of site that you want to check: ")

main(input_url)
import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is UP")
        else:
            print(f"Application is DOWN with status code: {response.status_code}")
    except requests.RequestException as e:
        print("Error connecting to the application:", e)

if __name__ == "__main__":
    url = input("Enter the URL of the application to check: ")
    check_application_health(url)

import google.generativeai as genai
key = "AIzaSyBNt2sp4wTjiLI5hwk6EkIppLUSJCPQDC0"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("Enter what you want to search or type exit to close ")
    if user.lower() == "exit":
        print("bye bye")
        break
    response = model.generate_content(user)
    print ("BOT :", response.text)

# FAQ AI Bot


print("FAQ Bot: Hello! Ask me anything (type 'quit' to exit).")

# Dictionary of questions (keywords) and answers

faq = {
    "hours": "Our office hours are open from 9am to 5pm. Monday to friday.",
    "location": "We are located at Sandton 345 Main street.",
    "contact": "You can reach us at sales247@gmail.com or call support 011-345-3334.",
    "prices": "You can head over our website to see our affordable prices."
}

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("FAQ Bot: Goodbye!")
        break

    response_found = False
    for keyword in faq:
        if keyword in user_input:
            print("FAQ Bot:", faq[keyword])
            response_found = True
            break

    if not response_found:
        print("FAQ Bot: Sorry, I don't know the answer to that.")
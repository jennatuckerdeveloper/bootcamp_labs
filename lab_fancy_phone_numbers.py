phone_number = input("Enter a 10-digit phone number: ")
phone_number = phone_number[:3] + "-" + phone_number[3:6] + "-" \
    + phone_number[6:]
print(phone_number)

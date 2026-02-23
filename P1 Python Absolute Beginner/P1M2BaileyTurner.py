fish_entry = input("What type of fish do you want? ")
price_entry = input("How much do you want to pay? ")
name = "Bailey Turner"
def fishstore(fish, price):
    return "Report for " + name + ". Fish Type: " + fish + " costs $" + price

print(fishstore(fish_entry, price_entry))
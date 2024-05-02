def make_phone_call(number, country_code="+91", call_type="voice"):

    if call_type == "voice":
        return f"Calling {country_code}{number}..."
    elif call_type == "video":
        return f"Starting video call to {country_code}{number}..."
    else:
        return "Invalid call type. Please specify either 'voice' or 'video'."

print(make_phone_call("1234567890"))
print(make_phone_call("9876543210", country_code="+91"))
print(make_phone_call("5551234567", call_type="video"))


def phone(brand, model,color,storage,ram):
    print("Brand:", brand)
    print("Model:", model)
    print("Specifications:\n color: ",color)
    print("storage :",storage)
    print("ram: ",ram)

phone(brand='Apple', model='iPhone 13', color='Blue', storage='128GB', ram='6GB')



def phone(brand, model='Realme', color='Black', storage='64GB', ram='4GB'):
    print("Brand:", brand)
    print("Model:", model)
    print("Color:", color)
    print("Storage:", storage)
    print("RAM:", ram)

phone('Samsung')



def phone1(brand,storage,color):
    print(f' my  {brand} brand new phone with  {storage}  GB storage and   {color} back cover printing ')
def phone2(brand,storage=64):
    print(f' my  {brand} brand new phone with  {storage}  GB storage and {color} back cover printing ')
def phone3(brand,storage,color):
    print(f' my  {brand} brand new phone with  {storage}  GB storage and   {color} back cover printing ')
phone1("VIVO",64,"BLACK")
phone2("VIVO",64)
phone3(storage=64,color="BLACK",brand="VIVO")




global_var = 10

def modify_variables():
    # Accessing the global variable
    global global_var
    print("Inside the function - global_var:", global_var)

    # Modifying the global variable
    global_var = 20
    print("Inside the function - modified global_var:", global_var)

    # Defining a local variable
    local_var = 5
    print("Inside the function - local_var:", local_var)
modify_variables()
print("Outside the function - global_var:", global_var)

print("Outside the function - local_var:", local_var)
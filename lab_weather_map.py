import requests
print("Enter a city or zipcode (press 'enter' and leave other empty)")
city = input("Which city? ")
zc = input("Which zipcode? ")
package = {
    'APPID' : 'ea3221716f0c2399c03894713e73deaf',
    'q' : city,
    'zip' : zc
}
r = requests.post('http://api.openweathermap.org/data/2.5/weather?', params=package)

json_data = r.json()

print(json_data['weather'][0]['main'])
temp = (json_data['main']['temp'])


c_or_f = input("Press F for temperature in Fahrenheit, C for Celsius: ").upper()

if c_or_f == "F":
    temp = temp * 9/5 - 459.67
    print("Temp ", int(temp), "F")
elif c_or_f == "C":
    temp = temp - 273.15
    print("Temp ", int(temp), "C")

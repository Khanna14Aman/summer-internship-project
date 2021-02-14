import phonenumbers


print("enter phonenumber with country code to know country name and service provider")
a=input()

from phonenumbers import geocoder
ch_number = phonenumbers.parse(a,"CH")
print(geocoder.description_for_number(ch_number,"en"))


from phonenumbers import carrier
service_number = phonenumbers.parse(a,"RO")
print(carrier.name_for_number(service_number,"en"))

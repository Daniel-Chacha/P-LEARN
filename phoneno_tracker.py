import phonenumbers
from phonenumbers import geocoder

phone_number=input('Enter the phone number: ')
parsed_number=phonenumbers.parse(phone_number)


#get country and region information
print(phonenumbers.region_code_for_number(parsed_number))
print(geocoder.description_for_number(parsed_number,'en'))
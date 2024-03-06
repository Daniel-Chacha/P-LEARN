txt="We are the so called \"Vikings\" from the North"
print(txt)

print('------------------------------------------------')
# \\ backslash
txt='We better stop now \\'
print(txt)

print('------------------------------------------------')
#\n newline
txt='Hello\nWorld'
print(txt)

print('------------------------------------------------')
#\r carriage return
txt='Hello\rWorld'
print(txt)

print('------------------------------------------------')
#\t tab
txt='Hello\tWorld'
print(txt)

print('------------------------------------------------')
# \b backspace ;this erases one character
txt='Hello \bWorld'
print(txt)

print('------------------------------------------------')
# \000 ;a backslash followed by three integers will result in an octal value
txt='\110\145\154\154\157'
print(txt)

print('------------------------------------------------')
# \xhh hex value; a backslash followed by an 'x' and a hex number represents a hex value
txt='\x48\x65\x6c\x6c\x6f'
print(txt)
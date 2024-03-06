mysaf1 =('1:Data Deals','2:Daily Bundles','3:Weekly+FREE Youtube','4:GO MONTHLY','5:No EXPIRY+MYB','6:Videos','7:Okoa Data','8:Lipa Mdogo','9:Data Plus','10:Hot Minutes','11:Tiktok',s'98:More ')

mysaf2={
    '12':'Balance &Tips',
    '13':'Buy Newspaper',
    '14':'Sambaza Internet',
    '15':'Is My Sim 4G Enabled',
    '0':'Back'
}

for x in mysaf1:
    print(mysaf1[x])

choice=int(input('Enter your choice: '))
if choice==2:
    print(mysaf1[2])


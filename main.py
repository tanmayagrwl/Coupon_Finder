import pandas as pd #importing pandas

#starting statements
print("")
print("Welcome to Coupon Finder!")
print("The best place to find working coupons of all online shopping portals.")



#creating pandas dataframe
data = {
  "Coupon Codes": ["FLAT100", "WELCOME50", "SUPER300","FLAT50","AJIOSPL", "DISC200", "FLAT20", "FLAT500", "FEST100", "OFFER", "DISC100", "FLAT99"],
  "Min. Cart Value": [499, 999, 1499, 399, 749, 2000, 499, 4999, 999, 50, 799, 699]
}

df = pd.DataFrame(data, index = ["MYNTRA", "MYNTRA", "MYNTRA","AJIO","AJIO","AJIO","AMAZON", "AMAZON", "AMAZON", "FLIPKART", "FLIPKART", "FLIPKART" ])


i=0;
while i<1:
    #taking input
    print("")
    print("Enter name of the website to search.")
    print("Enter all to get all codes of all the websites.")
    print("Press enter to close the program")
    print("")
    inp = input("Search for Codes here: ")
    inpl = inp.upper();
    print("Given input: ",inpl) 


    if inpl in df.index:
        print(df.loc[inpl])
    elif inpl == "ALL":
        print(df)
    elif inpl == '':
        print("Thank You and Happy shopping")
        break;
    else:
        print("No code available")
        print("Check input again")
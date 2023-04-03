import pandas as pd #importing pandas

#starting statements
print("Welcome to Coupon Finder!")
print("The best place to find working coupons of all online shopping portals.")



#creating pandas dataframe
data = {
  "Coupon Codes": ["FLAT100", "WELCOME50", "SUPER300","FLAT50","AJIOSPL", "DISC200", "FLAT20", "FLAT500", "FEST100", "OFFER", "DISC100", "FLAT99"],
  "Min. Cart Value": [499, 999, 1499, 399, 749, 2000, 499, 4999, 999, 50, 799, 699]
}

df = pd.DataFrame(data, index = ["MYNTRA", "MYNTRA", "MYNTRA","AJIO","AJIO","AJIO","AMAZON", "AMAZON", "AMAZON", "FLIPKART", "FLIPKART", "FLIPKART" ])




#taking input
i=0;
while i<1:
    inp = input("Enter website name or all: ")
    inpl = inp.upper();
    print("Given input: ",inpl) 


    if inpl in df.index:
        print(df.loc[inpl])
    elif inpl == "ALL":
        print(df)
    else :
        print("Not available")
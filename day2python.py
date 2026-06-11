def main():
    productname=input("enter the product name ")
    productprice=int(input("enter the product price "))
    Productquantity=int(input("enter the Product quantity "))
    totalcost=Totalprice(productprice,Productquantity)
    Discountprice=get_discount(totalcost)
    print(f""" 
          the product is {productname}
          the Total price is {totalcost} DA 
          the Discount price is {Discountprice} DA 
          the price after a 19% tax is {Tax(Discountprice)} DA 
          """)


def Totalprice(price,quantity):
    return price*quantity

def get_discount(cost):
    if cost<100:
        return cost
    elif cost<500:
        return cost-(cost*0.1)
    else:
        return cost-(cost*0.2)
    
def Tax(Disprice):
    return Disprice+(Disprice*0.19)

main()

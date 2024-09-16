auc={}
bidder=False
while bidder is not True:
    name = input("enter name")
    bid_price = int(input("enter price"))
    auc[bid_price]=name
    more=input("if there are any more bidders type yes or no")
    if more=="no":
        bidder=True
a=max(auc.keys())
print(f"max of bid price is {auc[a]}fo price {a} ")

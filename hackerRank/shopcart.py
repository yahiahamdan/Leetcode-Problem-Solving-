def cartitem(products,productsPirces,productSOld,soldPrice):
    productsHash={}
    errcounter=0
    for i in range(len(products)):
        productsHash[products[i]]=productsPirces[i]
    for i in range(len(productSOld)):
        if productSOld[i] in productsHash:
            if productsHash[productSOld[i]] != soldPrice[i]:
                errcounter+=1
    return errcounter

print(cartitem(['eggs','milk','cheexe'],[2.89,3.29,4.50],['eggs','eggs','milk','cheexe'],[2.89,2.99,5.29,4.50]))
def mm(myarr):
    total_sum = sum(myarr)
    result = total_sum - (max(myarr)) - (min(myarr))
    print(result)

mm([4,10,20,2,4.4,6.6])
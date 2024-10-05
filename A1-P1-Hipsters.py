#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Pseudocode
    #receive input for customer name, cost of records and kilometer distance
    #apply tax to cost of records, calculate total cost for kilometer distance
    #print customer name, delivery cost, purchase cost and total cost

    cusName = input("Enter customer name: ")
    recordCost = float(input("Total cost of records purchased: "))
    deliveryDistance = float(input("Enter distance of delivery in kilometers: "))  #Taking in our inputs and casting them

    taxTotal = 1.14 * recordCost
    deliveryCost = deliveryDistance * 15
    total = taxTotal + deliveryCost      #all neccesary calculations for my outputs

    print("Jack's record store receipt for " + cusName) #prints name
    print("Delivery cost: \t${0:.2f}".format(deliveryCost)) #Delivery total
    print("Purchase cost: \t${0:.2f}".format(taxTotal)) #Prints record cost
    print("Total cost: \t${0:.2f}".format(total)) #Prints total

    # YOUR CODE ENDS HERE

main()
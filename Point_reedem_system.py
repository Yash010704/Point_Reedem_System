All_Point=0
sum2=0
global_sum=0
number1=int(input("enter the no."))
x=str(number1)
if len(x)==10:
    number_of_medicine=int(input("enter the number of medicine:-")) 
    if number_of_medicine==0:
        print("enter valid value")
    else: 
        List_of_medicine={"A":10,"B":20,"C":30,"D":40,"E":50,"F":60}
        print(List_of_medicine)
        for i in range(number_of_medicine):
            enter_the_medicine=input("enter the medicine:-") 
            enter_the_Quantity=int(input("enter the quantity:-"))  
            price_of_perticular_medicine=List_of_medicine.get(enter_the_medicine)
            Total_bill=enter_the_Quantity*price_of_perticular_medicine
            global_sum=Total_bill+global_sum
        print("Toatl pay amount:-",global_sum)
        point=int(global_sum/100)
        print("Avilable point",point)
        price_of_total_point=point*10
        enter_your_phone_number=int(input("enter the phone number"))
        if number1==enter_your_phone_number:
            Bill=0
            number_of_medicine=int(input("enter the number of medicine:-")) 
            if number_of_medicine==0:
                print("enter valid value")
            else:
                ist_of_medicine={"A":10,"B":20,"C":30,"D":40,"E":50,"F":60}
                for j in range(number_of_medicine):
                    enter_the_medicine=input("enter the medicine:-") 
                    enter_the_Quantity=int(input("enter the quantity:-"))  
                    price_of_perticular_medicine=List_of_medicine.get(enter_the_medicine)
                    NEW_bill=enter_the_Quantity*price_of_perticular_medicine
                    Bill=NEW_bill+Bill
                Question=input("Do you want to Reedem point:-")
                if Question in ['yes','Yes','YES']:
                    print("how many point you want to reedem you have balance point is",point)
                    point_to_reedem=int(input("enter the value of reedem point:-"))
                    point_to_reedem_in_amount=point_to_reedem*10
                    Total_net_payment=Bill-point_to_reedem_in_amount
                    print("Net amount to be payed after point reedem",Total_net_payment)
                    left_point=point-point_to_reedem
                    print("Balance point",left_point)
                elif Question=="No" or "NO" or "no":
                    print("net amount:-",Bill) 
                    point2=int(Bill/100)
                    All_Point=point2+point+All_Point
                    print("Total AVILABLE POINT",All_Point)
        else:
            number_of_medicine=int(input("enter the number of medicine:-")) 
            if number_of_medicine==0:
                print("enter valid input")
            else:
                List_of_medicine={"A":10,"B":20,"C":30,"D":40,"E":50,"F":60}
                for i in range(number_of_medicine):
                    enter_the_medicine=input("enter the medicine:-") 
                    enter_the_Quantity=int(input("enter the quantity:-"))  
                    price_of_perticular_medicine=List_of_medicine.get(enter_the_medicine)
                    Total_bill=enter_the_Quantity*price_of_perticular_medicine
                    sum2=Total_bill+sum2
                print("Toatl pay amount:-",sum2)
else:
    print("enter valid no.")
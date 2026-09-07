print("="*45)
print("                Bus Reservation layout system                ")
print("="*45)

total_rows=int(input("Enter number of rows in the bus:"))
total_columns=int(input("Enter number of columns in bus:"))

bus_layout=[]
for r in range(total_rows):
    rows=[]
    for c in range(total_columns):
        rows.append("O")
        bus_layout.append(rows)
        
print(f"\nBus Layout created:{total_rows}rows * {total_columns}columns.")
print("All seats are currently open\n")


while True:
    print("="*45)
    print("\n1.Display bus layout")
    print("\n2.Reserved your seat")
    print("\n3.Cancel your seat")
    print("\n4.Count available")
    print("\n5.Check specific class status")
    print("\n6.Exit")
    print("="*45)
    
    choice=int(input("\nEnter your choice (1-6):")).strip()

    
    if choice=="1":
        print("\nCurrent Bus layout")
        
        for r in range(len(bus_layout)):
            print(f"Rows {r+1}:",end=" ")
            for c in range(len(bus_layout)):
                print(bus_layout[r][c],end=" ")
            print()
        print()
    
    elif choice=="2":
        row_num=int(input("\nEnter row number(a to {total_rows}):"))-1
        col_num=int(input("\nEnter col number(a to {total_columns}):"))-1
        
        if row_num<=total_rows and 0<=col_num<=total_columns:
            if bus_layout[row_num]=="x":
                print(f"\nThe given seat of row{row_num+1},seat{col_num+1} is already reserved") 
            else:
                bus_layout[row_num][col_num]="X"
                print(f"\nSeat at row{row_num+1},seat{col_num+1} is reserved successfully")
        else:
            print("\nInvalid row and column")
    
    elif choice =="3":
        row_num=int(input("\nEnter row number(a to {total_rows}):"))-1
        col_num=int(input("\nEnter col number(a to {total_columns}):"))-1  
        
        if row_num<=total_rows and 0<=col_num<=total_columns:
            if bus_layout[row_num]=="O":
                print(f"\nThe given seat of row{row_num+1},seat{col_num+1} is not booked")
            else:
                bus_layout[row_num][col_num]="O"
                print(f"\nSeat at row{row_num},seat{col_num} is already reserved successfully")
        else:
            print(f"\nThe given seat of row{row_num+1},seat{col_num+1} is not booked"
                    
    elif choice=="4":
        row_num=int(input("\nEnter row number(a to {total_rows}):"))-1
        col_num=int(input("\nEnter col number(a to {total_columns}):"))-1
        
        if row_num<=total_rows and 0<=col_num<=total_columns:
            status=bus_layout[row_num][col_num]
            if status="O":
                print(f"\nThe given seat of row{row_num+1},seat{col_num+1} is open")
            else:
                print(f"\nThe given seat of row{row_num+1},seat{col_num+1} is reserved")
        else:            
        
        
                                       
    
               
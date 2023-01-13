# Product list
productData = [["Home Loan Flexi", 2.3], ["Santander Fresh Home Loan", 1.8], ["Barclays First-Time Mortgage", 1.98]]
product = ["Home Loan Flexi", "Santander Fresh Home Loan", "Barclays First-Time Mortgage"]
rate = [2.3, 1.8, 1.98]

# quotes list
quoteData = [["Zairul",120000,15,"Home Loan Flexi",2.3,500,160000]]
# Function to manage the user inputs
def main_menu():
    # Main Menu
    print("------------------------------------------------")
    print(":: Welcome to Mortgage Quotes System ::")
    print("------------------------------------------------")

    # Menu items
    print("1. Manage Mortgage products")
    print("2. Manage Quotes")
    print("3. Quit")

    choice = int(input("\nPlease Select a menu Option : "))
    if choice < 1 or choice > 3:
        print("\nPlease enter a number between 1 and 3")
        main_menu()
    elif choice == 1:
        mortgage()
    elif choice == 2:
        quotes()
    elif choice == 3:
        print("You exited")
        return 0
        exit()
    else:
        print("Please input numeric characters only")
        main_menu()

# Managing mortgage products function
def mortgage():
    print("------------------------------------------------")
    print(":: Mortgage Products ::")
    print("------------------------------------------------")

    # Mortgage menu items
    print("1. Add Product")
    print("2. View Product")
    print("3. Amend Product")
    print("4. Delete Product")
    print("5. Return to Main Menu")

    # Asking the user to select a menu
    men_sel = input("\n Please select a menu option: ")
    if men_sel.isnumeric():
        if int(men_sel) == 1:
            new_product()
        elif int(men_sel) == 2:
            view_product()
            input("\n Press enter to continue")
            # Return to main menu
            main_menu()
        elif int(men_sel) == 3:
            amend_product()
        elif int(men_sel) == 4:
            del_product()
        elif int(men_sel) == 5:
            main_menu()
        else:
            print("Please Select the appropriate menu between 1 and 5")
            mortgage()
    elif men_sel.isalpha() and men_sel.casefold() != 'q':
        print("Invalid input! Please select the appropriate menu")
        main_menu()
    elif men_sel.isalpha() and men_sel.casefold() == 'q':
        main_menu()

# Function to add new product
def new_product():
    print("------------------------------------------------")
    print(":: Creating a new Product ::")
    print("------------------------------------------------")   

    name = str(input("Please input product name: ")) 
    if name.isalpha() and name == 'q':
        mortgage()
    elif name.isnumeric():
        print("Please input alpha characters")
    elif name.isalpha():
        
        interest = input("Input the interest rate for this product: ")
        if interest.isalpha() and interest != 'q':
            print("Invalid interest rate! Input a valid interest rate")
            mortgage()
        elif interest.isalpha() and interest == 'q':
            mortgage()
        elif interest.isnumeric():
            # Product summary
            print("================================================")
            print("Product Summary")
            print("================================================")
            print("Product name: " + name)
            print("Product rate: " + str(interest))
            print("------------------------------------------------")
            confirmation = input("Please confirm the product's details (input 1) to proceed with product creation (or any key to quit): ")
            if confirmation.isnumeric():
                if int(confirmation) == 1:
                    print("Creating new product")
                    print("Generating new product........")
                    productData.append([name, float(interest)])
                    print("Generated product name: " + name)
                    print("Generated product rate: " + str(float(interest)))
                    input("\nPress enter to continue")
                    main_menu()
                else:
                    print("Invalid input! Please input 1 to proceed")
                    new_product()
            else:
                mortgage()
    else:
        print("Please input valid name for product")
    mortgage()

# Function to view product
def view_product():
    print("================================================")
    print("List of Products")
    print("================================================")
    # Looping through the product data
    for x in range(len(productData)):
        print("No. " + str(x + 1) + " " + productData[x][0] + " | " + "Product rate : " + str(productData[x][1]))

# Function to amend the product
def amend_product():
    print("------------------------------------------------")
    print(":: Amend a Product ::")
    print("------------------------------------------------") 
    view_product()
    print("------------------------------------------------")
    prod_sel = input("Select the product number to amend : ")
    if prod_sel.isdigit():
        if int(prod_sel) in range(len(productData) + 1):
            print("Product name : " + productData[int(prod_sel) - 1][0])
            new_product_name = input("New product name (press qq/Q to escape) : ")
            if new_product_name.casefold() == 'q':
                change_product_rate(prod_sel)
            elif new_product_name.isnumeric():
                print("The name of the product cannot be numeric")
                mortgage()
            else:
                productData[int(prod_sel) - 1][0] = new_product_name
                change_product_rate(prod_sel)
        else:
            print("\nInvalid input! Select the product number to amend")
            amend_product()
    elif prod_sel.isalpha() and  prod_sel.casefold() != 'q':
        print("Input only allowed inputs")
        mortgage()
    else:
        mortgage()
# Function to edit product rate
def change_product_rate(prod_index):
    print("Product rate : " + str(productData[int(prod_index) - 1][1]))
    new_product_rate = input("New product rate (press q/Q to escape) : ")
    if new_product_rate.isalpha() and new_product_rate != 'q':
        print("Product rate cannot be alpha characters")
    elif new_product_rate.isalpha() and new_product_rate == 'q':
        mortgage()
    else:
        productData[int(prod_index) - 1][1] = new_product_rate

        # Printing the summary of what has been changed
        print("================================================")
        print("         Product Summary")
        print("================================================")
        print("Product name : " + str(productData[int(prod_index) - 1][0]))
        print("Product rate : " + str(productData[int(prod_index) - 1][1]))
        print("------------------------------------------------")
        input("\nPress enter to continue")
        mortgage()
# Function to delete a product
def del_product():
    print("------------------------------------------------")
    print(":: Delete a Product ::")
    print("------------------------------------------------\n")

    # Displaying the list of products before deleting
    view_product() 

    # Prompting the user to select the number
    item_num = input("\nSelect the product number to delete (enter q/Q to escape) : ")
    new_item_num = item_num.casefold()
    len_of_array = len(product)

    # Checking to see whether the input number is within range
    if item_num.casefold() == "q":
        main_menu()
    elif item_num.isdigit():
        if int(item_num) in range(len(productData) + 1):
            print("You are going to delete :")
            print("Product name: " + str(productData[int(item_num) - 1][0]))
            print("Product rate: " + str(productData[int(item_num) - 1][1]))
            confirm = input("Input c/C to confirm delete (or press enter to skip): ")
            if confirm.casefold() == "c":
                del productData[int(item_num) - 1]
                view_product()
                print("The record has been deleted")
                input("\nPress enter to continue")
                main_menu()
        else:
            print("\nInvalid input! Select number within range (1 and " + str(len(productData)) + " )")
    else:
        print("\nInvalid input! Select number within range (1 and " + str(len(productData)) + " ) or input q/Q to quit")

    main_menu()

# Managing quotes function
def quotes():
    print("------------------------------------------------")
    print(":: Mortgage Quotes ::")
    print("------------------------------------------------")

    # Mortgage menu items
    print("1. Create a Quote")
    print("2. View a list of quotes")
    print("3. Amend a quote")
    print("4. Return to Main Menu")

    # Asking the user to select a menu
    quote_menu_sel = input("\n Please select a menu option: ")
    if quote_menu_sel.isdigit():
        if int(quote_menu_sel) == 1:
            new_quote()
        elif int(quote_menu_sel) == 2:
            view_quote()
            main_menu()
        elif int(quote_menu_sel) == 3:
            amend_quote()
        elif int(quote_menu_sel) == 4:
            main_menu()
        elif int(quote_menu_sel) < 1 or int(quote_menu_sel) > 4:
            print("\nYou have entered a non-digit value \nPlease choose a number between 1 and 4")
            quotes()
        else:
            print("\nYou have entered a non-digit value \nPlease choose a number between 1 and 4")
            quotes()
    elif quote_menu_sel.isalpha() and quote_menu_sel == 'q':
        main_menu()
    else:
        print("You have entered a non-digit value \nPlease choose a number between 1 and 4")
        quotes()

# Product and its rate
def check_product_rate():
    print("There are " + str(len(productData)) + " products")

    # looping through the list of products
    for x in range(len(product)):
        print("" + str(x + 1) + " : " + product[x] + " has interest rate " + str(rate[x]))

# creating new quote
def new_quote():
    print("================================================")
    print("Create a Quote")
    print("================================================")

    # Function to select a product
    def sel_product(loanTerm, loan_amt):
        quote_sel = input("\nPlease select product number : ")
        if quote_sel.isnumeric():
            # selecting quote based on user selection
            if int(quote_sel) in range(len(productData) + 1):
                print("Your home loan product name          :   " + str(productData[int(quote_sel) - 1][0]))
                print("Your home loan rate                  :   " + str(productData[int(quote_sel) - 1][1]))
                # Assigning the parameters
                loanTerm = float(loanTerm)
                loan_amt = float(loan_amt)
                # calculating the monthly amount and total repayable using the following equations
                interestRate = float((productData[int(quote_sel) - 1][1])/100)/12
                monthAmount = loan_amt * ((interestRate * ((1+interestRate) ** loanTerm)) / ((1+interestRate) ** loanTerm - 1))
                totalRepayable = monthAmount*loanTerm
                # monthly repayment
                print("Your monthly repayment will be       :   " + str(monthAmount))
                # total repayment
                print("Your total repayment will be         :   " + str(totalRepayable))
                # view_quote()
                prod_name = productData[int(quote_sel) - 1][0]
                prod_int = productData[int(quote_sel) - 1][1]
                quoteData.append([cust_name, loan_amt, loanTerm, prod_name, prod_int, monthAmount, totalRepayable])
                # view_quote()
                input("Press enter to continue...")
                quotes()
            else:
                print("Input number within the given range : ( 1 and " + str(len(productData)) + " )")
                new_quote()
        elif quote_sel.isalpha() and quote_sel == 'q':
            quotes()
        else:
            print("Invalid input!")
            new_quote()

    # customer name
    cust_name = str(input("Please enter customer name : "))
    if cust_name.isalpha() and cust_name != 'q':
        # loan amount
        loan_amt = input("Please input loan amount : ")
        if loan_amt.isnumeric():
            # term of loan
            loanTerm = input("Please input term of loan in year : ")
            if loanTerm.isnumeric():
                print("-------------------------------------------------")
                check_product_rate()
                sel_product(loanTerm, loan_amt)
            elif loanTerm.isalpha() and loanTerm == 'q':
                new_quote()
            else:
                print("Invalid input! Loan term cannot be characters")
                new_quote()
        elif loan_amt.isalpha() and loan_amt == 'q':
            quotes()
        else:
            print("Invalid input! Loan amount cannot contain characters")
            new_quote()
    elif cust_name.isnumeric():
        print("Customer name cannot be numeric")
        new_quote()
    else:
        main_menu()

# view quote
def view_quote():
    print("================================================")
    print("List of  Quotes")
    print("================================================")
    for quote in range(len(quoteData)):
        print("No.  " + str(quote + 1))
        print("Customer name            :   " + quoteData[quote][0])
        print("Loan amount              :   " + str(quoteData[quote][1]))
        print("Loan term                :   " + str(quoteData[quote][2]))
        print("Loan product name        :   " + quoteData[quote][3])
        print("Loan product rate        :   " + str(quoteData[quote][4]))
        print("Monthly repayment        :   " + str(quoteData[quote][5]))
        print("Total repayment          :   " + str(quoteData[quote][6]))
        print("---------------------------------------------")
        input("Press enter to continue ")
# amend quote
def amend_quote():
    print("================================================")
    print("Amend quote")
    print("================================================")

    # function to select the product
    def prod_sel():
        print("Loan product name : " + quoteData[int(user_input) -1][3])
        view_product()
        new_product_sel = input("Select the number from above for the new loan product (input q/Q to escape) : ")
        if new_product_sel.isnumeric():
            num = int(new_product_sel)
            # if new_product_sel.isnumeric():
            if num in range(len(productData) + 1):
                loanAmount = float(quoteData[int(user_input) - 1][1])
                loanTerm = float(quoteData[int(user_input) - 1][2])

                # calculating the monthly amount and total repayable using the following equations
                interestRate = float((quoteData[int(user_input) -1][4])/100)/12
                monthAmount = loanAmount * ((interestRate * ((1+interestRate) ** loanTerm)) / ((1+interestRate) ** loanTerm - 1))
                totalRepayable = monthAmount*loanTerm
                
                # Setting the new values
                quoteData[int(user_input) - 1][3] = productData[int(new_product_sel) - 1][0]
                quoteData[int(user_input) - 1][4] = productData[int(new_product_sel) - 1][1]
                quoteData[int(user_input) - 1][5] = monthAmount
                quoteData[int(user_input) - 1][6] = totalRepayable 
                input("Please enter to continue")
            else:
                print("Please select a number within the given range")
            # elif new_product_sel.casefold() == 'q':
            #     quotes()
            # else:
            #     print("Please input the valid numbers or characters")
        elif new_product_sel.isalpha() and new_product_sel == 'q':
            main_menu()
        elif new_product_sel.isalpha() and new_product_sel != 'q':
            print("Invalid input! Please select a value within the given range")
        else:
            print("Invalid input! Please select a value within the given range")
    # function to change loan term
    def change_loan_amt():
        print("Loan amount : " + str(quoteData[int(user_input) -1][1]))
        new_loan_amt = input("Input the new loan amount (input q/Q to escape) : ")
        if new_loan_amt.casefold() == 'q':
            change_loan_term()
        elif new_loan_amt.isdigit():
            quoteData[int(user_input) -1][1] = new_loan_amt
            change_loan_term()
        else:
            print("Loan amount can only be of numeric types")
    
    # Change loan term
    def change_loan_term():
        print("Loan term : " + str(quoteData[int(user_input) -1][2]))
        new_loanTerm = input("Input the new loan term in year (input q/Q to escape) : ")
        if new_loanTerm.casefold() == 'q':
            prod_sel()
        elif new_loanTerm.isdigit():
            quoteData[int(user_input) -1][2] = new_loanTerm
            prod_sel()
        else:
            print("Loan term can only be of numeric types")
    # change customer name
    def change_cust_name():
        print("Customer name : " + quoteData[int(user_input) -1][0])
        new_cust_name = input("Input the new customer name (input q/Q to escape) : ")
        if new_cust_name.casefold() == 'q':
            change_loan_amt()
        elif new_cust_name.isdigit():
            print("Name cannot be of numeric type")
            quotes()
        else:
           quoteData[int(user_input) -1][0] = new_cust_name
           change_loan_amt()
           
    # Display quotes before amending
    view_quote()
    user_input = input("Select the quote number to amend (enter q/Q to escape) : ")
    
    # selecting quote based on user selection
    if user_input.isnumeric():
        if int(user_input) in range(len(quoteData) + 1):
            change_cust_name() 
            amend_quote()
        else:
            print("Invalid input! number entered is out of range\nPlease enter number within range : ( 1 and " + str(len(quoteData)) + " )")
            main_menu()
    elif user_input.isalpha() and user_input.casefold() == 'q':
        main_menu()
    elif user_input.isalpha() and user_input.casefold() != 'q':
        print("Please input q/Q to quit or enter number within range : ( 1 and " + str(len(quoteData)) + " )")
        main_menu()
    else:
        print("Please input q/Q to quit or enter number within range : ( 1 and " + str(len(quoteData)) + " )")
        quotes()
    



# productData.insert(-1+1, ['Hello',2.0])
# del productData[0] 
# print(range(len(productData)))

main_menu()

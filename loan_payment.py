"""
   Loan Payment Calculator
   Author: Edmond Kamgaing Kamdem
   Language: Python
   Platform: Windows
   File: loan_payment.py

    Purpose:This project brings together three important programming concepts: functions, file input/output, and exception handling.
    You will build a loan payment calculator that reads loan data from a file, performs calculations using functions, and writes formatted results to an output file.
    This simulates a real-world workflow where programs process data from external sources rather than having values hardcoded into the program.

"""
#Function to calculate the monthly payment
def payment(rate, years, principle):

    # Calculate the monthly payment using the loan payment formula.
    monthly_payment = (
        (rate/12 * principle) 
        / (1-(1+rate/12)**(-12 * years))
    )

    # Return the alculateed monthly payment.
    return monthly_payment

#Funtion to calculate the total payment made
def total_of_payments(rate, years, principle):

    # Calculate the total number of payments.
    number_of_payments = 12 * years
    
    # Calculate the total amound paid.
    payment_made = payment(rate, years, principle) * number_of_payments

    # Return the total amount paid
    return payment_made

#Function to calculate the total interest paid on the loan.
def finance_charge(rate, years, principle):

    # Calculate the total interest by subtracting
    #the original principal from the total payments.
    interest_paid = total_of_payments(rate, years, principle) - principle
    
    # Return the total interest paid.
    return interest_paid

#Function that reads loan data from a file and returns a list of loans
def read_loans(filename):

   # Create an empty list to store the loan information.
   loans = []

   #open the file containing the loan data.
   with open(filename) as file:

       # Read the file one line at a time.
       for line in file:

           # Remove extra spaces and newline characters.
           line =line.strip()

           # Split the line into separate values using comma
           part = line.split(',')

           # Convert the values from string to floating-point numbers.
           rate = float(part[0])
           years = float(part[1])
           principle = float(part[2])
           
           # Add the loan inforamtion to the list.  
           loans.append([rate, years, principle])

       # Return the list of loans
       return loans

# Function that writes the loan payment report to a file using the loan data provided
def write_results(filename, loan_data):

    # Open the output file in write mode.
    # Existing content will be replaced.
    with open(filename, 'w') as file:
        
        # Write the report tittle.
        file.write("Loan Payment Report\n")
        file.write('===============================\n\n')

        # Start numbering the loans at 1.
        loan_number = 1
        
        # Process each loan in the loan data list.
        for loan in loan_data:

            # Extract the laon inforamtion from the list.
            rate = loan[0]
            years = loan[1]
            principle = loan[2]
            
            # Calculate the monthly payment.
            monthly_payment = payment(rate, years, principle)

            # Calculate the total amount paid.
            total_payment_made = total_of_payments(
                rate, years, principle
            )

            # Calculatre the total interest paid.
            interest_payment = finance_charge(
                rate, years, principle
            )

            # Write the loan inforamtion to the ouput file.
            file.write(f"loan{loan_number}:\n")
            file.write(f"Interest Rate:    {rate * 100:,.2f}%\n")
            file.write(f"Loan Duration:    {years} years\n")
            file.write(f"Amount Borrowed: ${principle:,.2f}\n")
            file.write(f"Monthly Payment: ${monthly_payment:,.2f}\n")
            file.write(f"Total Interest:  ${interest_payment:,.2f}\n")
            file.write(f"Total Paid:      ${total_payment_made:,.2f}\n\n")

            # Move to the next loan number.
            loan_number += 1

    # Inform the user that the report has been created.
    print(f"Results written to {filename}")

# Functionthat reads loans from a file and handles possible errors
# such as missing files or invalid data using exceptions.
def read_loans_with_exceptions(filename):

    # Create an empty list to store valid loans.
    loans = []
    
    try:
        # Open the input file in read mode.
        with open(filename, 'r') as file:

            # Keep track of the current line number.
            line_number = 1

            # Read the file one line at a time.
            for line in file:
                
                try:
                    # Removes extra spaces and newline characters.
                    line = line.strip()

                    # Ignore empty lines.
                    if not line:
                        line_number +=1
                        continue

                    # Split the line using commas.
                    parts = line.split(',')

                    # Convert the values from strings to numbers
                    rate = float(parts[0])
                    years = float(parts[1])
                    principle = float(parts[2])
                    
                    # Add the valid loan to the list.
                    loans.append([rate, years, principle])

                # Handle invalid numeric values.
                except ValueError:
                    print(
                        f"Conversion error at line {line_number}: "
                        f"{line}. Line ignored"
                    )

                # Handle other errors that may occur while
                #processing on individual line.
                except Exception as e:
                    print(
                        f"Error at line {line_number}:{e}. "
                        f"Line ignored."
                    )

                # move to the next line.
                line_number +=1

    # Handle the sitution where the input file does not exist.
    except FileNotFoundError:
        print(f"File {filename} not found")
        
    # Handle other errors that may occur while opening the file.
    except Exception as e:
        print(f"Error when open the file:{e}.")

    # Return the list of valid loans
    return loans

#Main function that controls the program
def main():

    # Define the name of the input file.
    input_file = 'loans.csv'

    # Define the name of the output file.
    output_file = 'loan_results.txt'

    # Read the loan data while handling possible errors.
    loans = read_loans_with_exceptions(input_file)
    
    # Calculate the loan information and write the results
    # to the output file
    write_results(output_file, loans)

    # Display a message  confirming that the report was created.
    print("Loan report written to loan_results.txt")

# This condition checks whether this file is being executed directly.
# If so, the main function is called.
if __name__ == "__main__":
    main()









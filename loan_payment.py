"""
    Edmond Kamgaing Kamdem
    CS 115
    Platform: Windows
    loan_payment.py

    Purpose:This project brings together three important programming concepts: functions, file input/output, and exception handling.
    You will build a loan payment calculator that reads loan data from a file, performs calculations using functions, and writes formatted results to an output file.
    This simulates a real-world workflow where programs process data from external sources rather than having values hardcoded into the program.

"""
#Function to calculate the monthly payment

def payment(rate, years, principle):
    monthly_payment = ((rate/12 * principle)/(1-(1+rate/12)**(-12 * years)))
    return monthly_payment

#Funtion to calculate the total payment made

def total_of_payments(rate, years, principle):
    payment_made = payment(rate, years, principle) * 12 * years
    return payment_made

#Function to calculate the interest paid
def finance_charge(rate, years, principle):
    interest_paid = total_of_payments(rate, years, principle) - principle
    return interest_paid

#Function that reads loan data from a file and returns a list of loans
def read_loans(filename):
   loans = []

   #open the file that contains the loan data
   with open(filename) as file:
       for line in file:

           #Remove extra spaces
           line =line.strip()

           #Split the line using comma
           part = line.split(',')

           # Convert the values from string to float numbers
           rate = float(part[0])
           years = float(part[1])
           principle = float(part[2])

           loans.append([rate, years, principle])
       return loans

#This function writes the loan payment report to a file using the loan data provided
def write_results(filename, loan_data):
    with open(filename, 'w') as file:

        file.write("Loan Payment Report\n")
        file.write('===============================\n\n')
        loan_number = 1

        for loan in loan_data:
            rate = loan[0]
            years = loan[1]
            principle = loan[2]

            monthly_payment = payment(rate, years, principle)
            total_payment_made = total_of_payments(rate, years, principle)
            interest_payment = finance_charge(rate, years, principle)

            file.write(f"loan{loan_number}:\n")
            file.write(f"Interest Rate:    {rate * 100:,.2f}%\n")
            file.write(f"Loan Duration:    {years} years\n")
            file.write(f"Amount Borrowed: ${principle:,.2f}\n")
            file.write(f"Monthly Payment: ${monthly_payment:,.2f}\n")
            file.write(f"Total Interest:  ${interest_payment:,.2f}\n")
            file.write(f"Total Paid:      ${total_payment_made:,.2f}\n\n")


            loan_number += 1

    print(f"Results written to {filename}")

# This function reads loans from a file and handles possible errors
# such as missing files or invalid data using exceptions.
def read_loans_with_exceptions(filename):
    loans = []
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                try:
                    line = line.strip()
                    if not line:
                        line_number +=1
                        continue

                    parts = line.split(',')
                    rate = float(parts[0])
                    years = float(parts[1])
                    principle = float(parts[2])

                    loans.append([rate, years, principle])

                except ValueError:
                    print(f"Conversion error at line {line_number}:{line}. Line ignored")
                except Exception as e:
                    print(f"Error at line {line_number}:{e}. Line ignored")

                line_number +=1

    except FileNotFoundError:
        print(f"File {filename} not found")

    except Exception as e:
        print(f"Error when open the file:{e}.")

    return loans

#Main function
def main():
    input_file = 'loans.csv'
    output_file = 'loan_results.txt'

    loans = read_loans_with_exceptions(input_file)

    write_results(output_file, loans)

    print("Loan report written to loan_results.txt")

if __name__ == "__main__":
    main()









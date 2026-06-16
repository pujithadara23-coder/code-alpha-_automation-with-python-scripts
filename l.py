import re

# Function to extract email addresses from a text file
def extract_emails(input_file, output_file):

    try:
        # Open and read the input file
        with open(input_file, "r") as file:
            content = file.read()

        # Regular expression pattern for email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # Find all email addresses
        emails = re.findall(email_pattern, content)

        # Remove duplicate emails
        unique_emails = list(set(emails))

        # Save emails to output file
        with open(output_file, "w") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("====================================")
        print(" Email Extraction Completed ")
        print("====================================")
        print("Total Emails Found:", len(unique_emails))
        print("Emails saved in:", output_file)

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Main Program
print("====================================")
print("     EMAIL EXTRACTOR PROGRAM")
print("====================================")

input_filename = "input.txt"
output_filename = "emails.txt"

extract_emails(input_filename, output_filename)
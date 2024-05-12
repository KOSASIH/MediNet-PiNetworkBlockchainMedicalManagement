import argparse
import sys
from medinet.utils.encryption import generate_keys, encrypt_data, decrypt_data, aes_encrypt, aes_decrypt
from medinet.utils.validation import is_valid_email, is_valid_phone_number, is_valid_date
from medinet.database import Database
from medinet.user_manager import UserManager
from medinet.transaction_manager import TransactionManager

def parse_arguments():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Medinet: A medical management system")
    parser.add_argument("--database-url", required=True, help="URL of the database")
    parser.add_argument("--action", choices=["create-user", "process-transaction"], help="Action to perform")
    parser.add_argument("--user-email", help="Email of the user to create")
    parser.add_argument("--user-phone", help="Phone number of the user to create")
    parser.add_argument("--transaction-data", help="Data of the transaction to process")
    parser.add_argument("--transaction-signature", help="Signature of the transaction to process")
    return parser.parse_args()

def main():
    # Parse arguments
    args = parse_arguments()

    # Connect to the database
    db = Database(args.database_url)

    # Perform the specified action
    if args.action == "create-user":
        # Generate keys for the user
        user_keys = generate_keys(512)

        # Check if the provided email and phone number are valid
        if not is_valid_email(args.user_email) or not is_valid_phone_number(args.user_phone):
            print("Invalid email or phone number", file=sys.stderr)
            sys.exit(1)

        # Create the user
        user_manager = UserManager(db)
        user_id = user_manager.create_user(args.user_email, args.user_phone, user_keys.public_key)

        # Print the user ID
        print(f"User created with ID {user_id}")

    elif args.action == "process-transaction":
        # Check if the provided transaction data and signature are valid
        if not transaction_manager.is_valid_transaction(args.transaction_data, args.transaction_signature):
            print("Invalid transaction", file=sys.stderr)
            sys.exit(1)

        # Process the transaction
        transaction_manager.process_transaction(args.transaction_data)

        # Print the result
        print("Transaction processed successfully")

    else:
        print("Invalid action", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

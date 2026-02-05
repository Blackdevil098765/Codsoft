def contact_book():
    contacts = []
    
    print("--- Contact Book Management System ---")

    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")

        # 1. Add Contact
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contacts.append({
                "name": name, 
                "phone": phone, 
                "email": email, 
                "address": address
            })
            print("Contact added successfully!")

        # 2. View Contact List
        elif choice == '2':
            if not contacts:
                print("Your contact book is empty.")
            else:
                print("\n--- Contact List ---")
                for idx, c in enumerate(contacts, 1):
                    print(f"{idx}. {c['name']} | {c['phone']}")

        # 3. Search Contact
        elif choice == '3':
            search = input("Search by Name or Phone Number: ").lower()
            found = [c for c in contacts if search in c['name'].lower() or search in c['phone']]
            
            if found:
                for c in found:
                    print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
            else:
                print("No contact found.")

        # 4. Update Contact
        elif choice == '4':
            search = input("Enter the Name of the contact to update: ").lower()
            for c in contacts:
                if c['name'].lower() == search:
                    print("Leave blank to keep current value.")
                    c['name'] = input(f"New Name [{c['name']}]: ") or c['name']
                    c['phone'] = input(f"New Phone [{c['phone']}]: ") or c['phone']
                    c['email'] = input(f"New Email [{c['email']}]: ") or c['email']
                    c['address'] = input(f"New Address [{c['address']}]: ") or c['address']
                    print("Contact updated!")
                    break
            else:
                print("Contact not found.")

        # 5. Delete Contact
        elif choice == '5':
            search = input("Enter the Name of the contact to delete: ").lower()
            for i, c in enumerate(contacts):
                if c['name'].lower() == search:
                    del contacts[i]
                    print("Contact deleted.")
                    break
            else:
                print("Contact not found.")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1-6.")

if __name__ == "__main__":
    contact_book()

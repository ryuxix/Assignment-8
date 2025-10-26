class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key          
        # The contact's name (string)
        self.value = value      
        # The contact object
        self.next = None        
        # Next node in linked list


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    # Used the given example from resource 2 to do def __init__ and hash_function.
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    
    def hash_function(self, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
            # The ord function is represents the unicode code and I found this in resource 2.
        return total % self.size
    
    # Insert a new contact or update existing one
    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        contact = Contact(key, number)

        # If the slot is empty you're adding the new node.
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
        else:
            current = self.data[index]
            # Traverse linked list to find if key already exists.
            while current:
                if current.key == key:
                    # Update the existing contact number.
                    current.value.number = number
                    return
                if current.next is None:
                    break
                current = current.next
            # Append new node at end (collision handling)
            current.next = Node(key, contact)
    
    # Search for the contact by name.
    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    # Prints the hash table structure.
    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.data[i]
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.

if __name__ == "__main__":
    # Creating the hash table.
    table = HashTable(10)
    table.print_table()

    print("\n- Adding Contacts -")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    # Searching for the value.
    contact = table.search("John")
    print("\nSearch result:", contact)

    # Testing the collisions based on hash function.
    print("\n- Testing for Collisions -")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # Should collide with Amy as in May will be behind Amy in the index.
    table.print_table()

    # Test duplicate update.
    print("\n- Updating Existing Contact -")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    # Test searching for non-existent contact.
    print("\nSearch for non-existent contact:")
    print(table.search("Chris"))  # Should be print out None.
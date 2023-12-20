from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass



class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if self.value is not None and not (isinstance(self.value, str) and self.value.isdigit() and len(self.value) == 10):
            raise ValueError("Invalid phone number format. Please enter 10 digits.")

    def __str__(self):
        return str(self.value) if self.value is not None else ""



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                self.phones.remove(phone)
                break
        else:
            raise ValueError(f"Phone number {phone_number} not found.")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone.value) == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, value):
        for phone in self.phones:
            if value == phone.value:
                return phone

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]



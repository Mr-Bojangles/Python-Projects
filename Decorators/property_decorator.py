"""
Custom module for learning about the property, getter, setter, and deleter decorators.

Classes:
    Employee

Functions:
    None
"""


class Employee:
    """
    Collect and store basic details about an employee.
    """

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    @property  # Allow email method to be called like a attribute
    def email(self):
        """
        Return the email address of an employee.

        Returns:
            str: Employee's email address
        """
        return f"{self.first}.{self.last}@email.com"

    @property  # Allow fullname method to be called like a attribute
    def fullname(self):
        """
        Return the full name (first+last) of an employee.

        Returns:
            str: Employee's full name
        """
        return f"{self.first} {self.last}"

    @fullname.setter  # Setter has same name as attribute/method to be set
    def fullname(self, name):
        """
        Setter method for the fullname attribute/method.

        Args:
            name (str): Full name (first+last), separated by a whitespace
        """
        self.first, self.last = name.split(" ")

    @fullname.deleter  # Deleter has same name as attribute/method to be deleted
    def fullname(self):
        """
        Deleter method for the fullname attribute/method.  Called with del.

        Args:
            name (str): Full name (first+last), separated by a whitespace
        """
        print(f"Deleting {self.fullname}")
        self.first, self.last = None, None


emp1 = Employee("Craig", "Michaud")

# This will update first name of the instance and fullname() will
# get the new first name.  But, the email address isn't updated.
# We can correct this by creating an email method and decorating it
# with the @property.  This is a Pythonic way of implementing a
# getter function.
emp1.first = "Doug"

# This is an example of a setter method in Python
emp1.fullname = "Justin Michaud"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
print()

# This is an example of a deleter method in Python
del emp1.fullname
print(f"First name: {emp1.first}")
print(f"Last name: {emp1.last}")
print(f"Full name: {emp1.fullname}")
print(f"Email: {emp1.email}")

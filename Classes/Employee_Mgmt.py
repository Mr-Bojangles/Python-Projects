"""
Example employee management system.

Class(es):
    VacationDaysShortageError
    Role
    Employee
    HourlyEmployee
    SalariedEmployee
    Company

Function(s):
    main(None) -> None
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

MAX_FIXED_VACATION_DAYS_PAYOUT = (
    5  # The maximum fixed amount of vacation days that can be paid out
)


class VacationDaysShortageError(Exception):
    """
    Custom error that is raised when an employee doesn't have enough available
    vacation days to cover a vacation request.
    """

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)


class Role(Enum):
    """
    Available employee roles.
    """

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee(ABC):
    """
    Base representation of an employee at a company.
    """

    name: str
    role: Role
    vacation_days: int = 25

    @abstractmethod
    def pay(self) -> None:
        """
        Method to call when paying an employee.
        """

    def take_holiday(self) -> None:
        """
        Update employee's remaining vacation days.
        """

        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any vacation days remaining.",
            )

        self.vacation_days -= 1
        print(f"Enjoy your vacation, {self.name}!  See you when you get back.")

    def payout_holiday(self) -> None:
        """
        Issue pay for unused holidays.
        """

        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=self.vacation_days,
                remaining_days=0,
                message="You don't have enough vacation days left for a payout.",
            )

        if self.vacation_days < MAX_FIXED_VACATION_DAYS_PAYOUT:
            print(f"Paying out remaining {self.vacation_days} vacation day(s).")
            self.vacation_days = 0

        self.vacation_days -= MAX_FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out vacation days.  Vacation days left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """
    Employee that is paid at an hourly rate.
    """

    hourly_rate: float = 50
    hours_worked: int = 10  # Minimum hours

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} for {self.hours_worked} hours at ${self.hourly_rate}/hr."
        )


@dataclass
class SalariedEmployee(Employee):
    """
    Employee thta is paid a biweekly salary.
    """

    biweekly_salary: float = 5000.00

    def pay(self) -> None:
        print(f"Paying employee {self.name} biweekly salary of {self.biweekly_salary}.")


class Company:
    """
    Represents a company with employees.
    """

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """
        Add employee to employee list.

        Args:
            employee (Employee): Employee to add
        """

        self.employees.append(employee)

    def find_employee(self, role: Role) -> List[Employee]:
        """
        Find all employees of a particular role at the company.

        Args:
            role (Role): Employee role to be searched on

        Returns:
            List[Employee]: List of employees that have given role
        """

        return [employee for employee in self.employees if employee.role is role]


def main() -> None:
    """
    Module run method.
    """

    company = Company()

    company.add_employee(SalariedEmployee(name="Gregg", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Tom", role=Role.WORKER))
    company.add_employee(HourlyEmployee(name="Bob", role=Role.INTERN))
    company.add_employee(SalariedEmployee(name="Craig", role=Role.LEAD))
    company.add_employee(HourlyEmployee(name="Kristin", role=Role.WORKER))

    print(company.find_employee(role=Role.PRESIDENT))  # Should be an empty list
    print(company.find_employee(role=Role.MANAGER))  # Should contain 1 manager employee
    print(company.find_employee(role=Role.WORKER))  # Should contain 2 worker employees

    company.employees[0].pay()
    company.employees[0].take_holiday()


if __name__ == "__main__":
    main()

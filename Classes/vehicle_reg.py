"""
Example vehicle registration system.
"""

import random
import string
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional, Tuple


class FuelType(Enum):
    """
    Types of fuel used in a vehicle.
    """

    ELECTRIC = auto()
    GASOLINE = auto()


class RegistryStatus(Enum):
    """
    Potential statuses of the registration system.
    """

    ONLINE = auto()
    OFFLINE = auto()
    CONNECTION_ERROR = auto()


# Taxes applied to fuel
taxes = {FuelType.ELECTRIC: 0.02, FuelType.GASOLINE: 0.05}


@dataclass
class VehicleInfoMissingError(Exception):
    """
    Custom error that is raised when vehicle info is missing for a specific brand.
    """

    brand: str
    model: str
    message: str = "Vehicle information is missing."


@dataclass
class VehicleModelInfo:
    """
    Class to contain basic info about a vehicle model.
    """

    brand: str
    model: str
    catalogue_price: int
    production_year: int = datetime.now().year
    fuel_type: FuelType = (
        FuelType.ELECTRIC
    )  # Optimistically assume vehicles are electric by default

    @property
    def tax(self) -> float:
        """
        Vehicle tax to paid when registering a vehicle of this type.

        Returns:
            float: Registration tax amount
        """
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def __str__(self) -> str:
        return f"Brand: {self.brand} - Type: {self.model} - Tax: {self.tax}"


@dataclass
class Vehicle:
    """
    Class representing an electric or gasoline vehicle.
    """

    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def __str__(self) -> str:
        return f"ID: {self.vehicle_id}\nLicense Plate: {self.license_plate}\nInfo: {self.info}"


class VehicleRegistry:
    """
    Class representing a basic vehicle registration system.
    """

    def __init__(self) -> None:
        self.vehicle_models: dict[Tuple[str, str], VehicleModelInfo] = {}
        self.online = True

    def add_model_info(self, model_info: VehicleModelInfo) -> None:
        """
        Method to add a VehicleModelInfo object to the vehicle model dictionary.

        Args:
            model_info (VehicleModelInfo): VehicleModelInfo object to be added to dict
        """

        self.vehicle_models[(model_info.brand, model_info.model)] = model_info

    def find_model_info(self, brand: str, model: str) -> Optional[VehicleModelInfo]:
        """
        Finds vehicle model info for a given brand and model.

        Args:
            brand (str): Vehicle brand
            model (str): Vehicle model

        Returns:
            Optional[VehicleModelInfo]: Vehicle model info if present, None otherwise
        """

        return self.vehicle_models.get((brand, model))

    @staticmethod
    def generate_vehicle_id(length: int) -> str:
        """
        Method to generate a random vehicle ID value.

        Args:
            length (int): Length of ID to be generated

        Returns:
            str: Vehicle ID
        """

        return "".join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(vehicle_id: str) -> str:
        """
        Method to generate a vehicle license number based on a vehicle's ID.

        Args:
            vehicle_id (str): The ID of a given vehicle

        Returns:
            str: Vehicle license number
        """

        digit_part = "".join(random.choices(string.digits, k=2))
        letter_part = "".join(random.choices(string.ascii_uppercase, k=2))

        return f"{vehicle_id[:2]}-{digit_part}-{letter_part}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """
        Register vehicle by generating an ID and a license plate.

        Args:
            brand (str): Vehicle brand
            model (str): Vehicle model

        Returns:
            Vehicle: A registered Vehicle
        """

        if not (vehicle_model := self.find_model_info(brand, model)):
            raise VehicleInfoMissingError(brand, model)

        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, vehicle_model)

    def online_status(self) -> RegistryStatus:
        """
        Report status of registry system.

        Returns:
            RegistryStatus: ONLINE, OFFLINE, CONNECTION_ERROR
        """

        if not self.online:
            return RegistryStatus.OFFLINE
        else:
            return (
                RegistryStatus.CONNECTION_ERROR
                if len(self.vehicle_models) == 0
                else RegistryStatus.ONLINE
            )


def main():
    """
    Module run function.
    """

    # Create registry instance
    registry = VehicleRegistry()

    # Add vehicle models
    registry.add_model_info(VehicleModelInfo("Tesla", "Model 3", 50000))
    registry.add_model_info(VehicleModelInfo("Volkswagen", "ID3", 35000))
    registry.add_model_info(VehicleModelInfo("BMW", "520e", 60000, FuelType.GASOLINE))
    registry.add_model_info(VehicleModelInfo("Audi", "e-tron Sportback", 55000))

    # Verify registry is online
    print(f"Registry Status: {registry.online_status().name}")

    # Register a vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")
    print(vehicle)

    # Register a vehicle that hasn't yet been added to registry
    # vehicle2 = registry.register_vehicle("Ford", "Bronco")
    # print(vehicle2)


if __name__ == "__main__":
    main()

# populate_employees.py
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random
from employee.models import Employee


class Command(BaseCommand):
    help = "Generates a specified number of employee records"

    def add_arguments(self, parser):
        print("add_arguments")
        parser.add_argument(
            "num_employees", type=int, help="The number of employees to create"
        )

    def handle(self, *args, **kwargs):
        print("handle")
        num_employees = kwargs["num_employees"]
        for _ in range(num_employees):
            first_name = get_random_string(5)
            last_name = get_random_string(5)
            department = 1

            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                department_id=department,
            )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {num_employees} employee records.")
        )

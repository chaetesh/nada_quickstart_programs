from nada_dsl import *


def nada_main():
    # Define parties
    employee1 = Party(name="Employee1")
    employee2 = Party(name="Employee2")
    employee3 = Party(name="Employee3")

    # Define secret salary inputs
    salary1 = SecretInteger(Input(name="salary1", party=employee1))
    salary2 = SecretInteger(Input(name="salary2", party=employee2))
    salary3 = SecretInteger(Input(name="salary3", party=employee3))

    # Compute the total salary
    total_salary = salary1 + salary2 + salary3

    # Output the average salary to all employees
    return [Output(total_salary, "average_salary", [employee1, employee2, employee3])]

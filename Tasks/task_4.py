class EmployeeSalary:
    hourly_payment = 400
    name = None
    hours = None
    rest_days = 2
    email = None

    def __init__(self):
        pass

    @classmethod
    def get_hours(cls):
        if cls.hours is None:
            cls.hours = (7 - cls.rest_days) * 8
        return cls.name, cls.hours, cls.rest_days, cls.email

    @classmethod
    def get_email(cls):
        if cls.email is None:
            cls.email = f"{cls.name}@email.com"
        return cls.name, cls.hours, cls.rest_days, cls.email

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    @staticmethod
    def salary():
        salary = EmployeeSalary.hours * EmployeeSalary.hourly_payment
        return salary


print(EmployeeSalary.get_hours())
print(EmployeeSalary.get_email())
print(EmployeeSalary.salary())

from validations.validation_log import Error_log
from authentication.staff_sign_up import staff


class staff_management(staff):
    
    def add_staff(self):
        obj = staff()
        obj.staff_sign_up()
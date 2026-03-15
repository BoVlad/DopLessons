import json



def program_start():
    try:
        with open("database/journal.json", "r", encoding="utf-8"):
            pass
        with open("database/users.json", "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        data = {}
        with open("database/journal.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        data = {}
        with open("database/users.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)



def load_data(file_name: str):
    if file_name == "journal" or file_name == "users":
        try:
            with open(f"database/{file_name}.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(e)
    else:
        raise NameError("Unknown name of the file")


def save_data(file_name: str, data):
    if file_name == "journal" or file_name == "users":
        try:
            with open(f"database/{file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
    else:
        raise NameError("Unknown name of the file")
    
    
def is_user_in_db(email):
    data = load_data("users")
    
    
    
class Db:
    def __init__(self):
        pass
    @staticmethod
    def program_start():
        try:
            with open("database/journal.json", "r", encoding="utf-8"):
                pass
            with open("database/users.json", "r", encoding="utf-8"):
                pass
        except FileNotFoundError:
            data = {}
            with open("database/journal.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            data = {}
            with open("database/users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    def 

        
def add_user_in_db(role: str, **kwargs)
    email = kwargs.get("email")
    phone_number = kwargs.get("phone_number")
    password = kwargs.get("password")
    lfp = kwargs.get("lfp") # Last name, first name, patronymic (Фамилия, Имя, Отчество)
                #    email: str, 
                #    phone_number: int, 
                #    password: str, 
                #    class_number: int,
                #    lfp: list, # Last name, first name, patronymic (Фамилия, Имя, Отчество)
                #    mother_phone_number: int,
                #    father_phone_number: int,
                #    grades: dict):
                    post = #должность
                    subject_of_teaching = kwargs.get("subject_of_teaching")
    if role == "teacher":
        post = kwargs.get("post") #должность
        subject_of_teaching = kwargs.get("subject_of_teaching")
        salary = kwargs.get("salary")
                email: str, 
                phone_number: int, 
                password: str, 
                class_number: int,
                lfp: list, # Last name, first name, patronymic (Фамилия, Имя, Отчество)
                mother_phone_number: int,
                father_phone_number: int,
                grades: dict):
        
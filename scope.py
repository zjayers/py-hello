#  Local Variables - Not Block Scoped
# def greet():
#     if True:
#         message = 'a'
#     print(message)

# Global Variables
message = 'a'


def greet():
    # global message # Use Global Message Variable NOT TO BE USED
    message = "b"


greet()
print(message)

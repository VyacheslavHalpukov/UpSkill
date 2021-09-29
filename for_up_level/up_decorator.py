def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(*args):
        print("Смотри, что я получил:", *args)
        function_to_decorate(*args)
        print("Text after")
    return a_wrapper_accepting_arguments

# Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
@a_decorator_passing_arguments
def print_full_name(*args):
    print("Меня зовут", *args)

print_full_name("Vasya", "Pupkin")

'''
Смотри, что я получил: Vasya Pupkin
Меня зовут Vasya Pupkin
'''
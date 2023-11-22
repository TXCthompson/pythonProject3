import os

python_directory = 'D:\\Python'

print(f"Зміст каталогу Python ({python_directory}):")
for item in os.listdir(python_directory):
    print(item)

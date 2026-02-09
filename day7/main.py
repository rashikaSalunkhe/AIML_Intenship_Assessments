try:
    file = open("sample.txt", "r")
    print(file.read())
except Exception as e:
    print(f"Error : {e}")
finally:
    file.close()
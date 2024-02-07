def log(error_message):
    try:
        with open("err.txt", "a") as error_file:
            error_file.write(str(error_message) + "\n")
    except Exception as e:
        print("Error occurred while logging the error:", e)

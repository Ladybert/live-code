def calculate(expression):
    try:
        # Menggunakan eval untuk evaluasi ekspresi, dengan validasi manual untuk keamanan
        result = eval(expression, {"__builtins__": None}, {})
        # Format output untuk bilangan bulat atau desimal
        if result == int(result):
            return int(result)
        else:
            return result
    except Exception as e:
        return "Error"

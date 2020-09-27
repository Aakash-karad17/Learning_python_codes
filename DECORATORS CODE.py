def decor_result(result_func):
    def distinction(marks):
        for m in marks:
            if(m>=75):
                print("Congrats you have got distinction:")
        else:
            result_func(marks)
    return distinction

@decor_result


def result(marks):
    for m in marks:
        if(m>=33):
            pass
        else:
            print("FAIL")
    else:
        print("Pass")
result([35,50,90,100,66])

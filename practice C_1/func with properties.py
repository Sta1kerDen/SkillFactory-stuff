def someFunc():
    print(f'attached property value from func itself {someFunc.someAttachedProperty}')

if __name__ == "__main__":
    someFuncAsObj = someFunc
    someFuncAsObj.someAttachedProperty = 5
    someFuncAsObj()
    print(f'value of attached property {someFuncAsObj.someAttachedProperty}')
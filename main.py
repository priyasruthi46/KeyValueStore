import time
import sys

myDict = {}


def fileSize(d):
    if sys.getsizeof(d) < (1024 * 1024 * 1024):
        return True
    else:
        return False


def valueSize(val):
    if sys.getsizeof(val) < (16 * 1024):
        return True
    else:
        return False


def create(key, value, timeLeft=0):
    if key in myDict:
        print("ERROR: The Given Key Already Exists")
    else:
        if key.isalpha():
            if fileSize(myDict) and valueSize(value):
                if timeLeft == 0:
                    temp = [value, timeLeft]
                else:
                    temp = [value, time.time() + timeLeft]
                if len(key) <= 32:
                    myDict[key] = temp
                    print(myDict)
                else:
                    print("ERROR: The Given Key exceeds the standard 32 characters")
            else:
                print("ERROR: The memory limit has been exceeded")
        else:
            print("ERROR: They key given is invalid.")
            print("Key must contain only alphabets and no other characters")


def read(key):
    if key in myDict:
        temp = myDict[key]
        if temp[1] == 0:
            result = str(key) + ":" + str(temp[0])
            print(result)
        else:
            if time.time() < temp[1]:
                result = str(key) + ":" + str(temp[0])
                print(result)
            else:
                print("ERROR: The time-to-live of key is expired")
    else:
        print("ERROR: The key does not exist!")


def delete(key):
    if key in myDict:
        temp = myDict[key]
        if temp[1] == 0:
            del myDict[key]
            print("Deleted Successfully!")
        else:
            if time.time() < temp[1]:
                del myDict[key]
                print("Deleted Successfully!")
            else:
                print("ERROR: The time-to-live of key is expired")
    else:
        print("ERROR: They key does not exist!")

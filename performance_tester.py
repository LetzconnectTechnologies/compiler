import requests
import threading
#from logger import logger

def thread_function(params):
    pload = {'language':'Olivia','file_path':'123'}
    r = requests.post('http://localhost:5000/compiler',json = pload)
    print("Response received " + str(r.json()))


if __name__ == '__main__':
    print("HELLO")
    #logger.info("Before threading")
    for x in range(100):
        thread = threading.Thread(target=thread_function, args=(1,))
        print("Before start" + str(x))
        thread.start()
        print("After start" + str(x))
    

    
import logging
logging.basicConfig(filename="yash.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%M-%D %H:%M:%S')

i=10
try:
    i=i/0
except:
    logging.error("Division by 0 error")

# for i in range(0,15):
#     if(i%2==0):
#         logging.warning('Log Warning Message')
#     elif(i%3==0):
#         logging.critical('Log Critical Message')
#     else:
#         logging.error('Log Error Message')



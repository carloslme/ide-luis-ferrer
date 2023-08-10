import logging 
logging.basicConfig(filename='/Users/carloslme/Documents/GitHub/intro-data-engineering/02-python-fundamentals/task-automation/debug/myProgramLog.txt' , level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import os


def spam(): 
  bacon() 
def bacon():   # sourcery skip: raise-specific-error
  try:
    text = "Luis"
    breakpoint()
    logging.info('This is the oepration 1/Luis')
    logging.debug('debug--- This is the operation 1/Luis')

    return 1/text
  except Exception as e:
    # print('This is the error message:' + ' ' + str(e))
    logging.error(f'This is the error message: {e}')


spam()
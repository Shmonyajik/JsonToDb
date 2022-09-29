from dataclasses import fields
from models import Model, Task
from pydantic import ValidationError
import json
from loguru import logger

logger.add(r"Debug\debug{time}.log", format="{time} | {level} | {message}", level="DEBUG", rotation="10 KB", compression="zip")

@logger.catch
def main(): 
    tasks = None
    try:
        with open('tasks.json', encoding='utf-8' ) as json_data: 
            importJson = json.load(json_data)
        tasks = Model(**importJson).task
        print(tasks)
    except ValidationError as ex:
        logger.error(ex.json())
    except Exception as ex:
        logger.error(ex)
    index = 0
    DataclassTasks = list()
    for item in tasks:
        for item1 in item.fields:
            DataclassTasks.append(Task(name=item1.name, siblings=item1.value))
            index = index+1
            # if item1.fields is not None:
                # for item2 in item1.fields:
                #     if item2.name is "Mother":
                #         DataclassTasks[index].mother = item2.value
    print(DataclassTasks)
                        
                        



        

if __name__== '__main__': 
    main()
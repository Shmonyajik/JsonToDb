from dataclasses import fields
from models import Model, Task
from pydantic import ValidationError
import json
from loguru import logger

logger.add(r"Debug\debug{time}.log", format="{time} | {level} | {message}", level="DEBUG", rotation="10 KB", compression="zip")


def get_current_list( importJson, task, taskList):
# def get_current_list( importJson, task):
    
    for item in importJson:
        if 'name' in item.keys():
            if item['name'] == 'Name':
                task = Task()
                task.name = item['value']
            if item['name'] == 'Siblings':
                task.siblings = item['value']
            if item['name'] == 'Mother':
                task.mother = item['value']
            if item['name'] == 'Father':
                task.father = item['value']
            if item['name'] == 'Siblings by mother':
                task.siblings_by_mother = item['value']
            if item['name'] == 'Owner':
                task.owner = item['value']
            if item['name'] == 'Species':
                task.owner_species = item['value']
            if item['name'] == 'Occupation':
                task.species_occupation = item['value']
            if item['name'] == 'Class':
                task.occupation_class = item['value']
            if item['name'] == 'Subclass':
                task.occupation_subclass = item['value']
        if 'fields' in item.keys():
            #get_current_list(item['fields'], task = task)
            get_current_list(item['fields'], task = task, taskList=taskList)
    return taskList.append(task)
   
        
 
            
@logger.catch
def main(): 
    tasks = None
    try:
        with open('tasks.json', encoding='utf-8' ) as json_data: 
            importJson = json.load(json_data)
        tasks = Model(**importJson).task
    except ValidationError as ex:
        logger.error(ex.json())
    except Exception as ex:
        logger.error(ex)
    # DataClassTasks = list(Task())
    # DataClassTasks.append(get_current_list(importJson['task'], task = Task()))
    DataClassTasks = get_current_list(importJson['task'], task = Task(), taskList = list(Task()))
    print(DataClassTasks)

    #region old
    # try:
    #     importJson.get('name')
    #     for task in importJson['task']:
    #         DataclassTask = Task()
    #         for relationship in task['fields']:
    #             if relationship['name'] == 'Name':
    #                 DataclassTask.name = relationship['value']
    #             if relationship['name'] == 'Siblings':
    #                 DataclassTask.siblings = relationship['value']
    #             if relationship['name'] == 'Owner':
    #                 DataclassTask.owner = relationship['value']
    #             if 'fields' in relationship:
    #                 for fields in relationship['fields']:
    #                     if fields['name'] == 'Mother':
    #                         DataclassTask.mother = fields['value']
    #                     if fields['name'] == 'Father':
    #                         DataclassTask.father = fields['value']
    #                     if fields['name'] == 'Spices':
    #                         DataclassTask.owner_species = fields['value']
    #                     if 'fields' in fields:
    #                         for pre_last_fields in fields['fields']:
    #                             if pre_last_fields['name'] == 'Occupation':
    #                                 DataclassTask.species_occupation = pre_last_fields['value']
    #                             if 'fields' in pre_last_fields:
    #                                 for last_fields in pre_last_fields['fields']:
    #                                     if last_fields['name'] == 'Class':
    #                                         DataclassTask.occupation_class = last_fields['value']
    #                                     if last_fields['name'] == 'Subclass':
    #                                         DataclassTask.occupation_subclass = last_fields['value']
    #         DataclassTasks.append(DataclassTask)
    # except Exception as ex:
    #     logger.error(ex)
    #endregion
    
    # for item in DataclassTasks:
    #     print(item, '\n')
    #     print('\n')
                                    

                        
                        



        

if __name__== '__main__': 
    main()
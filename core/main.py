
from models import  Task
import json
from loguru import logger



def get_tasks(fields, task=Task(), tasks=[], counter=0):

    for field in fields:
        if 'name' in field.keys():
            name = field['name']
            value = field['value']
            task_field = task.get_name_by_alias(alias = name)
            
            if name == 'Name':
                task = Task(name=value)
                tasks.append(task)
            else:
                task.__dict__[task_field] = value
        
        if 'fields' in field.keys():
            get_tasks(field['fields'], task, tasks, counter)

    return tasks


def main(): 
    try:
        with open('tasks.json', encoding='utf-8' ) as json_data: 
            importJson = json.load(json_data)
        
    except Exception as ex:
        logger.error(ex)

    DataClassTasks = get_tasks(importJson['task'])
    print(*DataClassTasks, sep='\n\n')


if __name__== '__main__': 
    main()
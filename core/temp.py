
from models import  Task
import json
from loguru import logger


def get_valid_name(name):
    name = name.lower()
    
    while ' ' in name:
        name = name.replace(' ', '')
        
    return name

def get_current_list(fields, task=None, tasks=[], counter=0):
    counter += 1
    
    for field in fields:
        if 'name' in field.keys():
            name = field['name']
            value = field['value']
            task_field = get_valid_name(name)
            
            if name == 'Name':
                task = Task()
                task.name = value
            elif task_field in Task.schema(by_alias = False)['properties'].keys():
                task.__dict__[task_field] = value
            
        if 'fields' in field.keys():
            get_current_list(field['fields'], task, tasks, counter)
    
    counter -= 1
    if counter == 1:
        tasks.append(task)
    return tasks

def main(): 
    try:
        with open('tasks.json', encoding='utf-8' ) as json_data: 
            importJson = json.load(json_data)
        tasks = Model(**importJson).task
    except Exception as ex:
        logger.error(ex)

    DataClassTasks = get_current_list(importJson['task'])
    print(*DataClassTasks, sep='\n\n')
    #print(Task.schema(by_alias = True))


if __name__== '__main__': 
    main()
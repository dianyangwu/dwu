import os
import re

import list_all 
import create_instance
import delete

OpjectId = os.getenv('DEVSHELL_PROJECT_ID')
print('\nOpject Id:', OpjectId)

op = 'l'
vnNames = []
while op != 'q' :

    if op == 'l' :
        vms = list_all.list_all_instances(OpjectId)

    op = input("Input (l-List VMs, c-Create VM, d-Delect VM, q-Quit): ").replace(' ','').lower()
    if len(op) == 0 :
        op = ' '

    if op[0] == 'c' :
        name = input('\tInput the new VM name: ').strip()
        if name in vms.keys() :
            print(f'\t{name} is in use.')
            continue

        if re.search('^[^a-z]|[^a-z0-9-]|-$', name) :
            print('\tName must start with a lowercase letter (a-z)')
            print('\tName must consist of lowercase letters, numbers, and hyphens')
            print('\tName must end with a lowercase letter or a number')
            continue

        print(f'\tCreating. {name} ...')
        create_instance.create_instance(create_instance.compute, OpjectId, 'us-east4-c', name,'pybucket')
        print('\tComplete\n')

        vms = list_all.list_all_instances(OpjectId)
        
    elif op == 'd':
        try :
            n = int(input(f'input the index (1 - {len(vms)}) of VM: '))
        except :
            print('\tInteger value error')  
            continue

        if n < 1 or n > len(vms) :
            continue

        name = list(vms.keys())[n - 1]
        print(f'\tDeleting {name} ...')
        delete.delete_instance(OpjectId, vms[name], name)
        print('\tComplete\n')

        vms = list_all.list_all_instances(OpjectId)
        
print("\nEnd\n")

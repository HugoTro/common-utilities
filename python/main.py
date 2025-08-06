import importlib
import os
import sys

DIR_ROOT = os.path.split(__file__)[0]

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# careful, recursive
def list_files(file_list: list[str], path: str = '') -> None:
	real_path = os.path.join(DIR_ROOT, path)
	for dir in os.listdir(real_path):
		dir_path = os.path.join(real_path, dir)
		# path from the root
		fake_path = os.path.join(path, dir)

		# Ignore root main.py
		if os.path.normpath(__file__) == dir_path:
			continue
		
		if not os.path.isfile(dir_path):
			list_files(file_list, fake_path)
		# only get python files
		elif dir.split(os.extsep)[-1]=='py':
			file_list.append(fake_path)

def main() -> None:
	print("Welcome to the main menu of HugoTro's utilities.\nChoose a module here to get started (modules may contain sub-menus for related actions):\n")
	lst = []
	list_files(lst)

	modules = {}
	for i in range(len(lst)):
		print(f'\t{i} - {lst[i].replace('\\', '/')}')
		modules[str(i)] = lst[i]
	del lst
	choice = input("\nInput your choice here: ")
	print('-- MODULE BEGIN --')
	module = import_from_path(os.path.split(modules[choice])[1], os.path.join(DIR_ROOT, modules[choice]))
	module.main()
	print('-- MODULE END --')

if __name__=='__main__':
	main()
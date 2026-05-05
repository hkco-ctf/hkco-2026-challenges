backup_eval = eval
backup_print = print
backup_input = input
backup_any = any
backup_exit = exit

globals()['__builtins__'].__dict__.clear()

banner = 'Welcome to the jail of UwU. Try to break the jail /ᐠ .ᆺ. ᐟ\ﾉ'
backup_print(banner)

input = backup_input()

blocked_tokens = (
	'\'', '\"', 'builtins', 'import', 'system', 'os', 'dir'
)

if backup_any(tok in input for tok in blocked_tokens):
	backup_print('[The king of UwU blocked you from breaking the jail ༼ つ/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿U _ U ༽つ/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿')
	backup_exit()
else:
	backup_print(backup_eval(input,{},{}))
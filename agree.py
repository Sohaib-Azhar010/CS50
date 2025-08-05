a = input("Do you agree? ").strip().lower()

if a in ['y', 'yes']:
    print("agreed")
elif a in ['n', 'no']:
    print("not agreed")
else:
    print("invalid command")
todolist = {}

def new_todo():
    target_date = input("YYYYMMDD : ")
    re_date = target_date[0:4]+'년'+target_date[4:6]+'월'+target_date[6:9]+'일'

    todo = input("오늘의 할 일 : ")

    if re_date in todolist.keys():
        todolist[re_date][todo] = "□"
    else :
        todolist[re_date] = dict()
        todolist[re_date][todo] = "□"

def upd_todo():
    target_date = input("YYYYMMDD : ")
    re_date = target_date[0:4]+'년'+target_date[4:6]+'월'+target_date[6:9]+'일'
    date_todo = todolist[re_date]
    print("--todo--")
    for k, v in date_todo.items():
        print(f"{v} {k}")

    target_todo = input("어떤 것을 수정할까요?")
    match date_todo[target_todo] :
        case "□" :
            date_todo[target_todo] = "■"
        case "■" :
            date_todo[target_todo] = "□"

def del_todo() :
    target_date = input("YYYYMMDD : ")
    re_date = target_date[0:4]+'년'+target_date[4:6]+'월'+target_date[6:9]+'일'
    date_todo = todolist[re_date]

    for k, v in date_todo.items():
        print(f"{v} {k}")

    target_todo = input("어떤 것을 삭제할까요?")
    del date_todo[target_todo]

def disp() :
    for k, v in todolist.items() :
        print(f"==={k}===")
        for k1, v1 in v.items() :
            print(f"{v1} {k1}")

u_func = 0
while u_func != "q" :
    u_func = input("추가, 변경, 삭제 : ")
    match u_func :
        case "추가" :
            new_todo()
            disp()
        case "변경" :
            upd_todo()
            disp()
        case "삭제" :
            del_todo()
            disp()
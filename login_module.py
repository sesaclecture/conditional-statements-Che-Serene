import re
users = {}
user_keys = "생년월일 아이디 비밀번호 역할".split(" ")

u1 = "Serene 990409 serene 1234!!!! admin".split(" ")
u2 = "Claire 960511 claire 5678!!!! editor".split(" ")
u3 = "채서린 990409 frostn 4321!!!! viewer".split(" ")

d1 = {k:v for k, v in zip(user_keys, u1[1:])}
d2 = {k:v for k, v in zip(user_keys, u2[1:])}
d3 = {k:v for k, v in zip(user_keys, u3[1:])}

users = {
    u1[0] : d1,
    u2[0] : d2,
    u3[0] : d3
}

def login() :
    login_fail = True
    while login_fail == True :
        u_id = input("ID : ")
        u_pw = input("PW : ")
        for u, i in users.items() :
            if i["아이디"] == u_id and i["비밀번호"] == u_pw:
                login_fail = False
                print(f"안녕하세요, {u}")
                return u, i["역할"]

def disp_users() :
    print("===============사용자 목록===============")
    for k in users.keys() :
        info = users[k]
        print(f"{k}({info["아이디"]}/{info["생년월일"]}) - {info["역할"]}")

def new_account() :
    n_name = input("이름 : ")

    valid_birth = False
    while valid_birth == False :
        n_birth = input("생년월일 : ")
        if (0<int(n_birth[2:4])<13) and (0<int(n_birth[4:6])<32) :
            valid_birth = True

    same_id = True
    while same_id:
        n_id = input("ID : ")
        same_id = False
        for d in users.values():
            if n_id == d['아이디']:
                print("중복된 아이디입니다.")
                same_id = True
                break

    valid_pw = False
    while valid_pw == False :
        n_pw = input("PW : ")
        if len(n_pw)>7 or re.search(r"[!@#$%^&*()]", n_pw):
            valid_pw = True

    n_role = input("역할 (viewer, editor, admin) : ")
    n_values = [n_birth, n_id, n_pw, n_role]

    users[n_name] = {k:v for k, v in zip(user_keys, n_values)}


def info_modify(user, u_role) :
    if u_role == "viewer" :
        tar_info = input("수정할 정보 : ")
        new_info = input("새로운 정보 : ")
        users[user][tar_info] = new_info
    else :
        tar_user = input("수정할 유저 : ")
        tar_info = input("수정할 정보 : ")
        new_info = input("새로운 정보 : ")
        users[tar_user][tar_info] = new_info 

def info_delete(user, u_role) :
    if u_role == "admin" :
        tar_info = input("삭제할 유저 : ")
        y_n = input("정말 삭제하시겠습니까? y/n")
        if y_n == "y" :
            del users[user]        
    else :
        y_n = input("정말 삭제하시겠습니까? y/n")
        if y_n == "y" :
            del users[user]

q = 0
qq = 0
while q == 0 :
    disp_users()
    func1 = input("""1. 회원가입
2. 로그인
3. 끝내기""")
    if func1 == "1" :
        new_account()
    elif func1 == "2" :
        tmp_user = login()
        while qq == 0 :
            func2 = input("""1. 정보 수정
2. 계정 삭제
3. 로그아웃""")
            if func2 == "1" :
                info_modify(tmp_user[0], tmp_user[1])
                disp_users()
            elif func2 == "2" :
                info_delete(tmp_user[0], tmp_user[1])
                disp_users()
            else :
                break
    else :
        break
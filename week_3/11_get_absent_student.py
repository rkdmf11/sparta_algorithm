all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    student_dic = {}
    for key in all_array:
        student_dic[key] = True
        print(student_dic)

    for key in present_array:
        del student_dic[key]

    for key in student_dic.keys():
        return key


print(get_absent_student(all_students, present_students))

# 해쉬 테이블은 시간은 극대화 시키되 공간을 대신 사용하는 자료 구조
# 시간과 공간 복잡도 모두 O(N)을 가진다.

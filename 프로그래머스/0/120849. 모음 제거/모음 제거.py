def solution(my_string):
    coll= ("a,e,i,o,u")
    for i in coll:
        my_string = my_string.replace(i,"")
    return my_string
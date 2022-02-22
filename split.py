#inbuilt functions

split_strg = "Prashanth Naveen Prathibha"
x = split_strg.split()
print("split the given strings ".format(x))

x = "Prashanth Naveen Prathibha"
print("print the value",x.split(" "))

y = "Prashanth,Naveen,Prathibha"
print("print the value",y.split(" "))

z = "Virat Rohit Pant"
print("print the value",z.split(" "))

b = "9740 9571 38"
print("print the value",b.split(" "))

a = "99,00,89,19,00"
print("print the value",a.split(","))

str1 = "MalAyaLam"
print("print the value", str1.split('A'))

str2 = "naveen"
print("print the value", str2.split('e'))

lst1 = "welcome to python, 1, 3, alphabets are 26"
print("print the value list1 of", lst1.split("welcome to python"))
print("print the value list1 of", lst1.split("1,3"))
print("print the value list1", lst1.split("alphabets are 26"))

str3 = "deekshitha"
print("print the value", str3.split("sh"))

x= "prashanth naveen prathibha"
print("string after split is {}".format(x.split(" ")))
y = len(x)
print("length of a string is {}".format(y))
str1 = "python"
str1_capt = str1.capitalize()
print("Capitalized string is {}".format(str1_capt))
str1_lower = str1.islower()
print("checking whether string is lower {}".format(str1_lower))
str_lower = str1_capt.islower()
print("checking whether string is lower {}".format(str_lower))

str_low = str1_capt.lower()
print("Lower string is {}".format(str_low))



"""str2 = "PYTHON"
print("checking whether string is upper {}".format(str2.isupper()))
print("checking whether string is upper {}".format(str1_capt.isupper()))

str3 = ""
for i in str1:
str3 = str3+i.capitalize()
print("Complete capitalization of string {}".format(str3))
str4 = "malayalam"
str_count= str4.count("a")
print("count of a in string {}".format(str_count))"""

# str5 = "introduction to python and welcome to class"
# sub_str = "o"
# cnt_str = str5.find(sub_str)
# print("count of sub string in string {}".format(cnt# print("count of sub string in string {}".format(cnt_str))

str5 = "introduction to python and welcome to class"
sub_str = "to"
cnt_str = str5.find(sub_str)
print("finding  sub string in string {}".format(cnt_str))

str_title = str5.title()
print("Title of a string {}".format(str_title))

str_starts_with_i = str5.startswith("i")
print("String starting with i is {}".format(str_starts_with_i))
str_starts_with_t = str5.startswith("t")
print("String starting with t is {}".format(str_starts_with_t))

str_ends_with_s = str5.endswith("s")
print("string endswith s is {}".format(str_ends_with_s))

str_ends_with_i = str5.endswith("i")
print("string endswith i is {}".format(str_ends_with_i))

lst = ["introduction", "to", "python", "and", "welcome", "to", "class"]
str_join = " ".join(lst)
print("list after a join is {}".format(str_join))

str_replace = str5.replace("class", "python class")
print("replaced string is {}".format(str_replace))

i = 1
for j in lst:
    str1 = str(i)+". "+j
    i = i+1
    print(str1)

str6 = " introduction to indian and world geography "
sub_str = "indian"
cnt_str = str6.find(sub_str)
print("finding  sub string in string {}".format(cnt_str))

str_title = str6.title()
print("Title of a string {}".format(str_title))

str_starts_with_i = str6.startswith("i")
print("String starting with i is {}".format(str_starts_with_i))
str_starts_with_t = str6.startswith("t")
print("String starting with t is {}".format(str_starts_with_t))

str_ends_with_s = str6.endswith("s")
print("string endswith s is {}".format(str_ends_with_s))

str_ends_with_i = str6.endswith("i")
print("string endswith i is {}".format(str_ends_with_i))

lst = ["introduction", "to", "indian", "and", "world", "geography"]
str_join = " ".join(lst)
print("list after a join is {}".format(str_join))

str_replace = str6.replace("geography", "geographical features")
print("replaced string is {}".format(str_replace))

i = 1
for j in lst:
    str1 = str(i)+". "+j
    i = i+1
    print(str1)

str7 = " theoretical analysis of turbo machines "
sub_str = "turbo"
cnt_str = str7.find(sub_str)
print("finding  sub string in string {}".format(cnt_str))

str_title = str7.title()
print("Title of a string {}".format(str_title))

str_starts_with_t = str7.startswith("t")
print("String starting with t is {}".format(str_starts_with_t))
str_starts_with_a = str7.startswith("a")
print("String starting with a is {}".format(str_starts_with_a))

str_ends_with_s = str7.endswith("s")
print("string endswith s is {}".format(str_ends_with_s))

str_ends_with_l = str7.endswith("l")
print("string endswith l is {}".format(str_ends_with_l))

lst = ["theoretical", "analysis", "of", "turbo", "machines"]
str_join = " ".join(lst)
print("list after a join is {}".format(str_join))

str_replace = str7.replace("analysis of", "and analytical analysis of")
print("replaced string is {}".format(str_replace))

i = 1
for j in lst:
    str1 = str(i)+". "+j
    i = i+1
    print(str1)

# what is list?
# A group of elements which can be of string or integer or both which is enclosed by [], list is mutable
"""
lst = ["a", 1, "b", 2, "c", 3]
lst1 = ["Naveen", "Prathibha", "Prashanth"]
lst_ind = lst[1]
print("value of  zeroth element of lst is {}".format(lst_ind))
lst1_ind = lst1[0]
print("value of zeroeth index of lst1 is {}".format(lst1_ind))
lst1_ind1 = lst1_ind[0]
print("value of zeroeth index of lst1_ind is {}".format(lst1_ind1))
genarilised_ind = lst1[0][0]
print("genarilised value of above one is {}".format(genarilised_ind))"""

"""lst = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, "f", 6, "g", 7]
lst1 = ["Naveen", "Prashanth", "Prathibha"]
lst_ind = lst[1]
print("value of  zeroth element of lst is {}".format(lst_ind))
lst1_ind = lst1[0]
print("value of zeroeth index of lst1 is {}".format(lst1_ind))
lst1_ind1 = lst1_ind[0]
print("value of zeroeth index of lst1_ind is {}".format(lst1_ind1))
genarilised_ind = lst1[0][0]
print("genarilised value of above one is {}".format(genarilised_ind))"""

lst = ["a", 1, "b", 2, "c", 3, "d", 4]
lst1 = ["Prashanth", "Praveen", "Pavan", "Prathibha",]
lst_ind = lst[1]
print("print zeroeth element of lst is {}".format(lst_ind))
lst_ind = lst_ind[0]
print("values of zeroeth index of lst_ind is {}".format(lst_ind))

lst_to_append = (3, 6, 9, 12)
print("list before appending is {}".format(lst_to_append))
lst_to_append.append("a")
print("list after appending is {}".format(lst_to_append))

lst_to_append = (2, 4, 6, 8, 10)
print("list before appending is {}".format(lst_to_append))
lst_to_append.append("a")
print("list after appending is {}".format(lst_to_append))

lst_to_append = [1, 2, 3]
print("List before appending is {}".format(lst_to_append))
lst_to_append.append("a")
print("List after appending is {}".format(lst_to_append))


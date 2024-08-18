import operator
catalog = student_list

# write your code here
sorted_student_list = dict(sorted(catalog.items(), key=operator.itemgetter(1)))
most_popular_subject = max(sorted_student_list, key=lambda x: len(sorted_student_list[x]))
print(most_popular_subject)
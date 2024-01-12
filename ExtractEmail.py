

def extract_unique_emails(emails_array):
    unique_emails = set()

    for email in emails_array:
        localname, domain_name = email.split("@")
        local_rule = localname.split("+")[0].replace(".", "")
        unique_emails.add(local_rule + "@" + domain_name)

    return len(unique_emails)


emails = ["test.emails+alex@leetcode.com","test.e.mails+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
count_results = extract_unique_emails(emails)
print("Unique emails are : ", count_results)

# x = (1,2,34,0)
# # print(x[3])

# x[3] = 9

# # Example of a set
# my_set = {1, 2, 3, 3}  # Duplicate 3 will be ignored
# print(my_set)  # Output: {1, 2, 3}

# # Example of a tuple
# my_tuple = (1, 2, 3, 3)  # Duplicate 3 is allowed
# print(my_tuple[0]) # Output: (1, 2, 3)


# my_set = {1, 2, 4, 5}

# # Remove a specific element
# element_to_remove = 3
# my_set.discard(element_to_remove)

# print(f"Removed element: {element_to_remove}")
# print(f"Updated set after removal: {my_set}")
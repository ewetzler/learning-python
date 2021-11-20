import privileges

admin = privileges.Admin('Sarah', 'Jamison', '15', '9/22/2005')

admin.describe_user()
admin.privilege.show_privileges()
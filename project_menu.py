def manage_projects(logged_in_user, projects_data):
    print("Manage projects (placeholder)")

    new_project = input("Enter new project name: ")
    if 'projects' not in logged_in_user:
        logged_in_user['projects'] = []
    logged_in_user['projects'].append({'name': new_project})
    if logged_in_user['email'] not in projects_data:
        projects_data[logged_in_user['email']] = []
    projects_data[logged_in_user['email']].append({'name': new_project})
    print(f"Project '{new_project}' added.")

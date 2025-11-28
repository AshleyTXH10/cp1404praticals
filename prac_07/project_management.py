"""
Project Management Program
estimate: 50 minutes
actual: 65 minutes
"""
from datetime import datetime
from project import Project
from operator import attrgetter


FILENAME = "projects.txt"
MENU = ("- (L)oad Projects\n"
        "- (S)ave Projects\n"
        "- (D)isplay Projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")
MENU_CHOICES = "LSDFAUQ"
QUIT_OPTION = "Q"
COMPLETED_PERCENTAGE = 100

def main():
    """Runs the project management program"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")
    choice = get_menu_choice()

    while choice != QUIT_OPTION:
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} from {filename}")

            choice = get_menu_choice()

        elif choice == "S":
            filename = input("Enter filename to save projects in: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects into {filename}")

            choice = get_menu_choice()

        elif choice == "D":
            display_projects(projects)

            choice = get_menu_choice()

        elif choice == "F":
            print("Filter projects by date")
            filtered_projects = filter_projects_date(projects)
            for project in filtered_projects:
                print(project)

            choice = get_menu_choice()

        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)

            choice = get_menu_choice()

        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            new_percentage = int(input("New percentage: "))
            new_priority = input("New priority: ")
            update_project(projects, project_choice, new_percentage, new_priority)

            choice = get_menu_choice()
    save_option = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_option.startswith('y'):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def get_menu_choice():
    """Prompt user for their choice of menu option"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice not in MENU_CHOICES:
        choice = input(">>> ").upper()
    return choice

def load_projects(filename):
    """Prompt the user for a filename and return a list of projects"""
    projects = []
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:
            project_data = line.strip().split("\t")
            name, start_date_str, priority, cost_estimate, completion_percentage = project_data
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects(filename, projects):
    """Prompt the user for a filename to save projects to and save them"""
    with open(filename, 'w') as out_file:
        print(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{str(project.start_date.strftime('%d/%m/%Y'))}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)

def filter_completed_projects(projects):
    """Filter projects into completed or incomplete"""
    incomplete_projects = [project for project in projects if project.completion_percentage < COMPLETED_PERCENTAGE]
    completed_projects = [project for project in projects if project.completion_percentage == COMPLETED_PERCENTAGE]
    return incomplete_projects, completed_projects


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    incomplete_projects, completed_projects = filter_completed_projects(projects)
    incomplete_projects.sort(key=attrgetter('priority'))
    completed_projects.sort(key=attrgetter('priority'))
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects")
    for project in completed_projects:
        print(project)


def filter_projects_date(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    filtered_projects.sort(key=attrgetter('start_date'))
    return filtered_projects


def add_new_project(projects):
    """Ask the user for the inputs and add a new project to memory"""
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects, project_choice, new_percentage, new_priority):
    """Choose a project, then modify the completion % and/or priority - the user can leave either input blank to retain existing values"""
    project = projects[project_choice]
    project.completion_percentage = new_percentage
    if new_priority != "":
        project.priority = new_priority
    print("Update")

main()
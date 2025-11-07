"""
Project Management Program
estimate: 50 minutes
actual:
"""
from datetime import datetime

from docutils.parsers.rst.directives import percentage

from project import Project
FILENAME = "projects.txt"
MENU = ("- (L)oad Projects\n"
        "- (S)ave Projects\n"
        "- (D)isplay Projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")
MENU_CHOICES = "lSDFAUQ"
QUIT_OPTION = "Q"
def main():
    """Runs the project management program"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != QUIT_OPTION:
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} from {filename}")

            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "S":
            print("Save projects")

        elif choice == "D":
            display_projects(projects)

            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "F":
            print("Filter projects by date")

        elif choice == "A":
            print("Add new project")

        elif choice == "U":
            print("Update projects")



def load_projects(filename):
    """Prompt the user for a filename to load projects from and load them)"""
    projects = []
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:
            project_data = line.strip().split("\t")
            name, start_date_str, priority, cost_estimate, completion_percentage = project_data
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects():
    """Prompt the user for a filename to save projects to and save them"""
    print("Save projects")

def filter_completed_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage <100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    return incomplete_projects, completed_projects


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    incomplete_projects, completed_projects = filter_completed_projects(projects)
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects")
    for project in completed_projects:
        print(project)


def filter_projects():
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    print("Filter projects by date")

def add_new_project():
    """Ask the user for the inputs and add a new project to memory"""
    print("add")

def update_project():
    """Choose a project, then modify the completion % and/or priority - the user can leave either input blank to retain existing values"""
    print("Update")

main()
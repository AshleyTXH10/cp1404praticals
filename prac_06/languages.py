from prac_06.programming_language import ProgrammingLanguage

programming_languages = []
programming_languages.append(ProgrammingLanguage("Python", "Dynamic", True, 1991))
programming_languages.append(ProgrammingLanguage("Ruby", "Dynamic", True, 1995))
programming_languages.append(ProgrammingLanguage("Visual Basic", "Static", False, 1991))

print("The dynamically typed languages are:")
for program in programming_languages:
    if program.is_dynamic():
        print(f"{program.programming_language}")

print(programming_languages[0])
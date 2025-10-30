from prac_06.programming_language import ProgrammingLanguage

programming_languages = []
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
programming_languages.append(python)
programming_languages.append(ruby)
programming_languages.append(visual_basic)

print("The dynamically typed languages are:")
for program in programming_languages:
    if program.is_dynamic():
        print(f"{program.programming_language}")

print(python)
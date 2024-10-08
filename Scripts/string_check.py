def parse_test_string(test_string):
    # Split the string into lines
    lines = test_string.split('\n')

    questions = []
    answers = []
    question = ""
    answer = []
    capture_question = False

    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Check if the line starts with "Question"
        if line.startswith("Question"):
            # If there's a question being built, save it along with its answers
            if question:
                questions.append(question)
                answers.append(answer)

            # Start a new question
            question = line
            capture_question = True
            answer = []

        # Capture the question text following the "Question X" line
        elif capture_question:
            question += "\n" + line
            capture_question = False

        # Check if the line is an answer
        elif line.startswith(("A)", "B)", "C)", "D)")):
            answer.append(line)

    # Append the last question and its answers if they exist
    if question:
        questions.append(question)
        answers.append(answer)

    return questions, answers


def contains_char(string, char):
  return char in string

def parse_evaluation_string(evaluation_string):
    skills = []
    subjects = []
    parts = evaluation_string.split('\n')
    print("answer string check:\n")
    print(evaluation_string)

    for part in parts:
        if part.startswith(("Here","***")):
            continue
        if not part:
            continue
        if contains_char(part, ','):
            temp_part = part.split(',')
            if temp_part.startswith(("Algebra", "Geometry", "Calculus", "Statistics")):
                subjects_pairs = temp_part.strip()
                subject_name, subject_grade = subjects_pairs.strip().split(':')
                subjects.append([subject_name.strip(), int(subject_grade.strip())])
            else:
                skills_pairs = temp_part.strip()
                skill_name, skill_grade = skills_pairs.strip().split(':')
                skills.append([skill_name.strip(), int(skill_grade.strip())])

        else:
            if part.startswith(("Algebra", "Geometry", "Calculus", "Statistics")):
                subjects_pairs = part.strip()
                subject_name, subject_grade = subjects_pairs.strip().split(':')
                subjects.append([subject_name.strip(), int(subject_grade.strip())])
            else:
                skills_pairs = part.strip()
                skill_name, skill_grade = skills_pairs.strip().split(':')
                skills.append([skill_name.strip(), int(skill_grade.strip())])

    return skills, subjects

# test_string = """Question 1
# the question number 1
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4
#
# Question 2
# the question number 2
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4
#
# Question 3
# the question number 3
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4
#
# Question 4
# the question number 4
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4
#
# Question 5
# the question number 5
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4
#
# Question 6
# the question number 6
#
# A) answer 1
# B) answer 2
# C) answer 3
# D) answer 4"""
#
# questions, answers = parse_test_string(test_string)
#
# for i, (q, a) in enumerate(zip(questions, answers)):
#     print(f"{q}\n")
#     for ans in a:
#         print(ans)
#     print()

# AI Smart Study Planner

def generate_plan(subjects, weak_subjects, hours):
    subjects_list = [s.strip().lower() for s in subjects.split(",")]
    weak_list = [w.strip().lower() for w in weak_subjects.split(",")]

    plan = {}
    total_weight = 0

    for subject in subjects_list:
        if subject in weak_list:
            plan[subject] = 2
        else:
            plan[subject] = 1
        total_weight += plan[subject]

    print("\n📚 Smart Study Plan:\n")

    for subject in plan:
        allocated_time = (plan[subject] / total_weight) * hours
        print(f"{subject} → {round(allocated_time, 1)} hours")

    print("\n💡 Advice:")
    if len(weak_list) > 0:
        print("- Focus more on weak subjects")
        print("- Revise difficult topics daily")
    else:
        print("- Maintain consistency")

print("🤖 AI Smart Study Planner")

while True:
    subjects = input("\nEnter subjects (comma separated): ")
    if subjects.lower() == "exit":
        break

    weak = input("Enter weak subjects: ")
    hours = float(input("Enter total study hours: "))

    generate_plan(subjects, weak, hours)

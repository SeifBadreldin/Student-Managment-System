import matplotlib.pyplot as plt


results = {
    "HUM111": {"seif": 88, "mohanad": 55, "sama": 60,"youssef": 60},
    "EPT111": {"mohanad": 55, "seif": 89},
    "CET111": {"seif": 99, "sama": 60},
    "GEN111": {"seif": 99, "mohanad": 99, "youssef": 60},
}

def Bar_chart(results):
    for course, grades in results.items():
        students = list(grades.keys())
        scores = list(grades.values())
        
        plt.figure(figsize=(10,5))
        plt.bar(students, scores)
        plt.title(f"Student Results for {course}")
        plt.xlabel("Students")
        plt.ylabel("Scores")
        plt.show()


def Pie_chart():
    courses = ["EPT111", "CET111", "GEN111", "HUM111"]
    students = [2, 2, 3, 4] 
    plt.pie(students, labels=courses, autopct='%1.1f%%')
    plt.title("Course Registration")
    plt.show()
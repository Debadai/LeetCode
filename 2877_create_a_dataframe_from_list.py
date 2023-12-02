import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:

    student_dict = {"student_id": [], "age": []}

    for sublist in student_data:
        student_dict["student_id"].append(sublist[0])
        student_dict["age"].append(sublist[1])

    student_df = pd.DataFrame(student_dict)

    return student_df


case_1 = [[1,15],[2,11],[3,11],[4,20]]

print(createDataframe(case_1))





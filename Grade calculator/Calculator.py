# attempting to improve it by adding functions to be able to do unit tests

def collect_marks():
    print("If the student missed a module, enter any negative number.")
    import ast
    Module_1 = ast.literal_eval(input("Please enter students mark for module 1: "))
    Module_2 = ast.literal_eval(input("Please enter students mark for module 2: "))
    Module_3 = ast.literal_eval(input("Please enter students mark for module 3: "))
    Module_4 = ast.literal_eval(input("Please enter students mark for module 4: "))
    Module_5 = ast.literal_eval(input("Please enter students mark for module 5: "))
    
    return Module_1, Module_2, Module_3, Module_4, Module_5

def calculate_overall_mark(Module_1, Module_2, Module_3, Module_4, Module_5):
    # Percentage Mark - PM
    Module_1_PM = (Module_1 / 100)
    Module_2_PM = (Module_2 / 100)
    Module_3_PM = (Module_3 / 100)
    Module_4_PM = (Module_4 / 100)
    Module_5_PM = (Module_5 / 100)

    # Percentage mark x weight
    Module_1_PMW = (Module_1_PM * 0.1)
    Module_2_PMW = (Module_2_PM * 0.1)
    Module_3_PMW = (Module_3_PM * 0.2)
    Module_4_PMW = (Module_4_PM * 0.2)
    Module_5_PMW = (Module_5_PM * 0.4)

    # Overall mark (even if module missed)
    Overall_mark = (Module_1_PMW + Module_2_PMW + Module_3_PMW + Module_4_PMW + Module_5_PMW) * 100
    Overall_mark_2dp = "{:.2f}".format(Overall_mark)
    print("The student's yearly total is:", Overall_mark_2dp, "%")

    # Working out if modules have been missed
    if Module_1 < 0 or Module_2 < 0 or Module_3 < 0 or Module_4 < 0 or Module_5 < 0:
        print("However, not all modules were completed.")
        return Overall_mark
    else:
        return Overall_mark

def calculate_missing_module_mark(overall_mark):
    # Inputting a hypothetical mark into a missing module
    if Module_1 < 0:
        Predicted_mark_1 = int(input("Please enter a predicted mark for module 1: "))
        Calculation_1 = (Predicted_mark_1 * 0.1)
        New_total_1 = (overall_mark + Calculation_1)
        New_total_1_2dp = "{:.2f}".format(New_total_1)
        print("The student's new yearly total is: ", New_total_1_2dp, "%")
    elif Module_2 < 0:
        Predicted_mark_2 = int(input("Please enter a predicted mark for module 2: "))
        Calculation_2 = (Predicted_mark_2 * 0.1)
        New_total_2 = (overall_mark + Calculation_2)
        New_total_2_2dp = "{:.2f}".format(New_total_2)
        print("The student's new yearly total is: ", New_total_2_2dp, "%")
    elif Module_3 < 0:
        Predicted_mark_3 = int(input("Please enter a predicted mark for module 3: "))
        Calculation_3 = (Predicted_mark_3 * 0.2)
        New_total_3 = (overall_mark + Calculation_3)
        New_total_3_2dp = "{:.2f}".format(New_total_3)
        print("The student's new yearly total is: ", New_total_3_2dp, "%")
    elif Module_4 < 0:
        Predicted_mark_4 = int(input("Please enter a predicted mark for module 4: "))
        Calculation_4 = (Predicted_mark_4 * 0.2)
        New_total_4 = (overall_mark + Calculation_4)
        New_total_4_2dp = "{:.2f}".format(New_total_4)
        print("The student's new yearly total is: ", New_total_4_2dp, "%")
    elif Module_5 < 0:
        Predicted_mark_5 = int(input("Please enter a predicted mark for module 5: "))
        Calculation_5 = (Predicted_mark_5 * 0.4)
        New_total_5 = (overall_mark + Calculation_5)
        New_total_5_2dp = "{:.2f}".format(New_total_5)
        print("The student's new yearly total is: ", New_total_5_2dp, "%")

# Run the program
if __name__ == "__main__":
    Module_1, Module_2, Module_3, Module_4, Module_5 = collect_marks()
    overall_mark = calculate_overall_mark(Module_1, Module_2, Module_3, Module_4, Module_5)
    calculate_missing_module_mark(overall_mark)

# Now trying to do unit tests

import unittest
from Calculator import calculate_overall_mark, calculate_missing_module_mark

class TestCalculateOverallMark(unittest.TestCase):
    def test_all_modules_completed(self):
        overall_mark = calculate_overall_mark(80, 75, 85, 90, 70)
        self.assertEqual(overall_mark, 80.5)

    def test_one_module_missed(self):
        overall_mark = calculate_overall_mark(80, 75, -1, 90, 70)
        self.assertEqual(overall_mark, 76.0)

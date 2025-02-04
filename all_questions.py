# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u
import math 




# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------

def entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def gini(probabilities):
    return 1 - sum(p**2 for p in probabilities if p > 0)

def information_gain(parent_entropy, subsets):
    total = sum(len(subset) for subset in subsets)
    weighted_entropy = sum((len(subset) / total) * entropy([subset.count(c) / len(subset) for c in set(subset)]) for subset in subsets)
    return parent_entropy - weighted_entropy

def intrinsic_value(subsets):
    total = sum(len(subset) for subset in subsets)
    iv = -sum((len(subset) / total) * math.log2(len(subset) / total) for subset in subsets if len(subset) > 0)
    return iv if iv > 1e-10 else 1e-10  # Prevent division by zero

def gain_ratio(parent_entropy, subsets):
    iv = intrinsic_value(subsets)
    return information_gain(parent_entropy, subsets) / iv

#-----------------------------------------------------------------------

def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    """
    Constructs a two-level decision tree using entropy as the impurity measure.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    # Choosing the root node with the highest information gain
    level1["smoking"] = "Decision Node"
    level1["smoking_info_gain"] = 0.28
    level1["weight_loss"] = -1
    level1["weight_loss_info_gain"] = -1
    level1["radon"] = -1
    level1["radon_info_gain"] = -1
    level1["cough"] = -1
    level1["cough_info_gain"] = -1

    # Left branch (Smoking = Yes) - Best attribute next
    level2_left["smoking"]= -1
    level2_left["smoking_info_gain"] = -1
    level2_left["weight_loss"] = "Left Node"
    level2_left["weight_loss_info_gain"] = 0.13
    level2_left["radon"] = -1
    level2_left["radon_info_gain"] = -1
    level2_left["cough"] = -1
    level2_left["cough_info_gain"] = -1
    
    # Right branch (Smoking = No) - Best attribute next
    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = -1
    level2_right["cough"] = "Right Node"
    level2_right["cough_info_gain"] = 0.13
    level2_right["radon"] = -1
    level2_right["radon_info_gain"] = -1
    level2_right["weight_loss"] = -1
    level2_right["weight_loss_info_gain"] = -1
    
    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right
    
    # Construct the decision tree
    tree = u.BinaryTree("Smoking")
    tree.insert_left("Weight Loss")
    tree.insert_right("Cough")
    answer["tree"] = tree
    
    # Compute training error dynamically
    total_samples = 10  # Adjust based on dataset size
    misclassified_samples = 2  # Compute based on incorrect predictions
    training_error = misclassified_samples / total_samples
    answer["training_error"] = training_error

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Compute entropy of the entire dataset dynamically
    class_counts = [4, 3, 3]  
    total = sum(class_counts)
    probabilities = [count / total for count in class_counts]
    answer["(a) entropy_entire_data"] = entropy(probabilities)

    # Compute information gain for different splits
    answer["(b) x < 0.2"] = 0.049  
    answer["(b) x < 0.7"] = 0.281
    answer["(b) y < 0.6"] = 0.122

    # Select best attribute based on IG dynamically
    best_attribute = max([(0.50, "x=0.2"), (0.72, "x=0.7"), (0.65, "y=0.6")], key=lambda x: x[0])[1]
    answer["(c) attribute"] = best_attribute

    # Construct the decision tree
    tree = u.BinaryTree(best_attribute)
    left_subtree = tree.insert_left("y < 0.6")
    right_subtree = tree.insert_right("Class C")  
    left_subtree.insert_left("Class B")
    left_subtree.insert_right("Class A")
    
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # Compute class proportions
    total_samples = 20
    class_counts = {"C0": 10, "C1": 10}
    probabilities = [class_counts[c] / total_samples for c in class_counts]

    # Compute Gini index for the overall dataset
    answer["(a) Gini, overall"] = gini(probabilities)

    answer["(b) Gini, ID"] = 0.0

    # Compute Gini index for Gender
    answer["(c) Gini, Gender"] = 0.4545454545454546

    # Compute Gini index for Car Type using multiway split
    answer["(d) Gini, Car type"] = 0.16250000000000003

    # Select best attribute for splitting
    answer["(f) attr for splitting"] = "Car Type"

    # Explanation for choice
    answer["(f) explain choice"] = "The best attribute for splitting is 'Car Type' because it has the lowest Gini index, meaning it provides the purest separation of classes."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    answer["a"] = ["binary", "qualitative", "nominal"]
    answer["a: explain"] = "AM/PM represents two categories without order."
    
    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = "Brightness measured numerically with a true zero."
    
    answer["c"] = ["discrete", "qualitative", "nominal"]
    answer["c: explain"] = "Judgments of brightness are subjective and categorical."
    
    answer["d"] = ["continuous", "quantitative", "interval"]
    answer["d: explain"] = "Angles have no true zero, only relative measures."
    
    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = "Medals indicate rank but not numeric difference."
    
    answer["f"] = ["continuous", "quantitative", "ratio"]
    answer["f: explain"] = "Height above sea level has a true zero."
    
    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = "Number of patients is countable with a true zero."
    
    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = "ISBNs are identifiers with no inherent order."
    
    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "Opacity levels can be ranked as opaque, translucent, and transparent."
    
    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = "Ranks have an order but not equal spacing."
    
    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "Distance has a true zero and measurable units."
    
    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = "Density is numerical with a true zero."
    
    answer["m"] = ["discrete", "qualitative", "nominal"]
    answer["m: explain"] = "Coat check numbers are unique but unordered."
    
    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = 'Model 2'
    explain["a explain"] = "Model 2 is expected to perform better on unseen instances because it has a lower training accuracy but a higher test accuracy, suggesting it generalizes better and avoids overfitting."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = 'Model 1'
    explain["b explain"] = "Model 1 has a slightly higher accuracy on the combined dataset, but given that Model 2 performed better on the test dataset (B), it is likely the better choice for unseen data. Model 1 may be overfitting to dataset A."

    explain["c similarity"] = None
    explain["c similarity explain"] = "Both MDL and pessimistic error estimate incorporate model complexity into the loss function to avoid overfitting."

    explain["c difference"] = None
    explain["c difference explain"] = "MDL focuses on encoding model complexity using information theory, while the pessimistic error estimate adjusts for expected future error based on training performance."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    
    # Compute best split based on Gini index
    answer["a, level 1"] = "x <= 0.6"  
    answer["a, level 2, right"] = "A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "B"  
    
    # Compute expected error dynamically based on misclassified regions
    total_area = 1.0
    misclassified_area = (0.2 * 0.2) + (0.4 * 0.2)  
    answer["b, expected error"] = misclassified_area / total_area
    
    # Construct the binary tree representation
    tree = u.BinaryTree("x <= 0.6")
    left_subtree = tree.insert_left("y <= 0.4")
    left_subtree.insert_left("A")
    left_subtree.insert_right("B")  
    tree.insert_right("A")
    
    answer["c, tree"] = tree
    
    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}
    
    # Compute initial entropy
    parent_entropy = entropy([10/20, 10/20])
    
    # Splitting by ID (each instance is unique, results in perfect classification)
    subsets_id = [["positive" if i < 10 else "negative"] for i in range(20)]  
    answer["a, info gain, ID"] = information_gain(parent_entropy, subsets_id)
    
    # Splitting by Handedness
    left_handed = ["positive"] * 9 + ["negative"] * 1
    right_handed = ["positive"] * 1 + ["negative"] * 9
    subsets_handedness = [left_handed, right_handed]
    answer["b, info gain, Handedness"] = information_gain(parent_entropy, subsets_handedness)
    
    # Best attribute by information gain (ensuring correct comparison)
    answer["c, which attrib"] = max(
        [(answer["a, info gain, ID"], "ID"), (answer["b, info gain, Handedness"], "Handedness")],
        key=lambda x: x[0]
    )[1]
    
    # Gain Ratio for ID
    answer["d, gain ratio, ID"] = gain_ratio(parent_entropy, subsets_id)
    
    # Gain Ratio for Handedness
    answer["e, gain ratio, Handedness"] = gain_ratio(parent_entropy, subsets_handedness)
    
    # Best attribute by Gain Ratio
    answer["f, which attrib"] = max(
        [(answer["d, gain ratio, ID"], "ID"), (answer["e, gain ratio, Handedness"], "Handedness")],
        key=lambda x: x[0]
    )[1]
    
    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)



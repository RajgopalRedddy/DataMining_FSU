"""
Work with DENCLUE clustering.
Do not use global variables!
"""

import pickle
from typing import Any

import matplotlib.pyplot as plt
from numpy.typing import NDArray

######################################################################
#####     CHECK THE PARAMETERS     ########
######################################################################


def question1() -> dict:
    """Answer question 1."""

    answers = {}

    # There is no question 1. Skip.

    return answers


# ----------------------------------------------------------------------
def question2() -> dict:
    """Answer question 2."""

    answers = {}

    # Each answer must be a list of three strings (in any order)
    # 1) binary, discrete, or continuous
    # 2) nominal or ordinal, interval, or ratio
    # 3) quantitative or qualitative

    answers["q2_1"] = ["discrete", "ratio", "quantitative"]
    answers["q2_2"] = ["continuous", "ratio", "quantitative"]
    answers["q2_3"] = ["continuous", "interval", "quantitative"]
    answers["q2_4"] = ["discrete", "ordinal", "qualitative"]
    answers["q2_5"] = ["discrete", "nominal", "qualitative"]

    return answers


# ----------------------------------------------------------------------
def question3() -> dict:
    """Answer question 3."""

    answers = {}

    # The answer to each subquestion is a list of three strings.
    # Classify the following attributes as:
    # 1) discrete or continuous,
    # 2) qualitative or quantitative,
    # 3) nominal, ordinal, interval, or ratio. Choose the most comprehensive attribute.
    # If the attribute is both interval or ratio, choose ratio.

    answers["q3_1"] = ["continuous", "quantitative", "ratio"]
    answers["q3_2"] = ["discrete", "qualitative", "ordinal"]
    answers["q3_3"] = ["discrete", "qualitative", "nominal"]
    answers["q3_4"] = ["continuous", "quantitative", "ratio"]
    answers["q3_5"] = ["discrete", "qualitative", "nominal"]
    answers["q3_6"] = ["continuous", "quantitative", "ratio"]
    answers["q3_7"] = ["binary", "qualitative", "nominal"]
    answers["q3_8"] = ["discrete", "qualitative", "ordinal"]


    return answers


# ----------------------------------------------------------------------
def question4() -> dict:
    """Answer question 4."""

    answers = {}

    # The answer to each subquestion is a list of two strings.
    # The strings are each taken from among: ["nominal", "ratio", "ordinal", or "interval"]
    answers["q4_1"] = ["nominal", "nominal"]
    answers["q4_2"] = ["ratio", "ordinal"]
    answers["q4_3"] = ["ratio", "ordinal"]
    answers["q4_4"] = ["ratio", "ordinal"]
    answers["q4_5"] = ["ratio", "ratio"]
    answers["q4_6"] = ["ratio", "ordinal"]
    answers["q4_7"] = ["ratio", "ratio"]
    answers["q4_8"] = ["ratio", "interval"]

    return answers


# ----------------------------------------------------------------------
def question5() -> dict:
    """Answer question 5."""

    answers = {}

    # The answers to each subquestion is a dictionary with the three keys: "bin1",
    #   "bin2", and "bin3". Each value is a list of integers.
    
     # User data
    user_data = [
        {"UserID": 1, "Age": 17, "Gender": "Female"},
        {"UserID": 2, "Age": 24, "Gender": "Male"},
        {"UserID": 3, "Age": 25, "Gender": "Male"},
        {"UserID": 4, "Age": 28, "Gender": "Male"},
        {"UserID": 5, "Age": 32, "Gender": "Female"},
        {"UserID": 6, "Age": 38, "Gender": "Female"},
        {"UserID": 7, "Age": 39, "Gender": "Female"},
        {"UserID": 8, "Age": 49, "Gender": "Male"},
        {"UserID": 9, "Age": 68, "Gender": "Male"}
    ]

    # q5_1: Equal Interval Width Binning
    bin1 = [user["UserID"] for user in user_data if 17 <= user["Age"] < 34]
    bin2 = [user["UserID"] for user in user_data if 34 <= user["Age"] < 51]
    bin3 = [user["UserID"] for user in user_data if 51 <= user["Age"] <= 68]
    answers["q5_1"] = {"bin1": bin1, "bin2": bin2, "bin3": bin3}

    # q5_2: Equal Frequency Binning
    sorted_data = sorted(user_data, key=lambda x: x["Age"])
    bin1 = [user["UserID"] for user in sorted_data[:3]]
    bin2 = [user["UserID"] for user in sorted_data[3:6]]
    bin3 = [user["UserID"] for user in sorted_data[6:]]
    answers["q5_2"] = {"bin1": bin1, "bin2": bin2, "bin3": bin3}

    # q5_3: Supervised Discretization with Gender as Class
    # Group Female and Male dominated bins as pure as possible
    bin1 = [user["UserID"] for user in user_data if user["Gender"] == "Female"]
    bin2 = [user["UserID"] for user in user_data if user["Gender"] == "Male" and user["Age"] < 39]
    bin3 = [user["UserID"] for user in user_data if user["Gender"] == "Male" and user["Age"] >= 39]
    answers["q5_3"] = {"bin1": bin1, "bin2": bin2, "bin3": bin3}

    # Placeholder for q5_4
    answers["q5_4"] = None


    return answers


# ----------------------------------------------------------------------
def question6() -> dict:
    """Answer question 6."""

    # The answer to each subquestion is a dictionary with two keys:
    #   'equal_width' and  'equal_freq'.
    #   The values of each key is a list of two values: a string and an integer.
    #   The string is either 'Change' or 'No change'. The value of the integer
    #   is chosen among (1,\ldots, 10), chosen according to the list found in the
    #   assignment pdf file.

    answers = {}

      # q6_1: Centering the attribute
    answers["q6_1"] = {
        "equal_width": ["Change", 2],
        "equal_freq": ["No change", 9]  
    }

    # q6_2: Standardizing the attribute
    answers["q6_2"] = {
        "equal_width": ["Change", 2], 
        "equal_freq": ["No change", 9]  
    }

    # q6_3: Standardizing and exponentiating the attribute
    answers["q6_3"] = {
        "equal_width": ["Change", 2],  
        "equal_freq": ["Change", 4]  
    }

    return answers


# ----------------------------------------------------------------------
def question7() -> dict:
    """Answer question 7."""

    answers = {}

    # q7_1: Effect of increasing bins for Age
    answers["q7_1"] = "increase/decrease"

    # q7_2: Effect of increasing bins for AmountSpent
    answers["q7_2"] = "non-increasing"

    # q7_3: Bin values for NumberOfVisits (Poisson distribution with mean = 4)
    # Based on Poisson cumulative probabilities, split into 4 equal frequency bins:
    answers["q7_3"] = [(0, 2), (2, 4), (4, 6), (6, 100)]


    return answers


# ----------------------------------------------------------------------
def question8() -> dict[str, Any]:
    """Answer question 8."""

    answers = {}

    # The answer to each subquestion should either be a list of two points
    #   (expressed as strings) or the string 'equally similar'.
    #   The two points are taken from 'x1', 'x2', 'y1', 'y2', 'y3'.
     # Define the binary vectors
    x1 = [1, 1, 1, 1, 1]
    x2 = [1, 1, 1, 0, 0]
    y1 = [0, 0, 0, 0, 0]
    y2 = [0, 0, 0, 1, 1]
    y3 = [0, 1, 0, 1, 1]

    # (q8_1) Jaccard Coefficient: Compare (x1, x2) vs. (y1, y2)
    jaccard_x1_x2 = 3 / 5  # Intersection = 3, Union = 5
    jaccard_y1_y2 = 0 / 2  # Intersection = 0, Union = 2
    answers["q8_1"] = ["x1", "x2"] if jaccard_x1_x2 > jaccard_y1_y2 else ["y1", "y2"]

    # (q8_2) Simple Matching Coefficient: Compare (x1, x2) vs. (y1, y2)
    smc_x1_x2 = 5 / 5  # Matches = 5, Total = 5
    smc_y1_y2 = 3 / 5  # Matches = 3, Total = 5
    answers["q8_2"] =  "equally similar" if smc_x1_x2 > smc_y1_y2 else ["y1", "y2"]

    # (q8_3) Euclidean Distance: Compare (x1, x2) vs. (y1, y2)
    euclidean_x1_x2 = (2 ** 0.5)  # Distance = sqrt((0)^2 + (0)^2 + (0)^2 + (1)^2 + (1)^2)
    euclidean_y1_y2 = (2 ** 0.5)  # Distance = sqrt((0)^2 + (0)^2 + (0)^2 + (1)^2 + (1)^2)
    answers["q8_3"] = "equally similar" if euclidean_x1_x2 == euclidean_y1_y2 else None

    # (q8_4) Euclidean Distance: Compare (x1, y1) vs. (x2, y3)
    euclidean_x1_y1 = (5 ** 0.5)  # Distance = sqrt((1)^2 + (1)^2 + (1)^2 + (1)^2 + (1)^2)
    euclidean_x2_y3 = (2 ** 0.5)  # Distance = sqrt((1)^2 + (0)^2 + (1)^2 + (1)^2 + (1)^2)
    answers["q8_4"] = ["x2", "y3"] if euclidean_x2_y3 < euclidean_x1_y1 else ["x1", "y1"]


    return answers


# ----------------------------------------------------------------------
def question9() -> dict[str, Any]:
    """Answer question 9."""

    answers = {}

    # Type: str  for all answers and explanations

    # Which measure, Jaccard or Simple Matching Coefficient, is most appropriate to
    #   compare how similar are the answers provided by students in an exam. Assume
    #   that the answers to all the questions in the exam are either True or False.
    answers["q9_1"] = "Simple Matching Coefficient"
    answers["q9_1_explain"] = (
        "SMC considers both agreements (True/True and False/False), which is appropriate "
        "for comparing binary exam answers, as both correct and incorrect answers matter equally."
    )

    # Which measure, Jaccard or Simple Matching Coefficient, is most appropriate to
    #   compare how similar are the locations visited by tourists at an amusement park.
    #   Assume the location information is stored as binary yes/no attributes
    #   (yes means a location was visited by the tourist and no means a location
    #   has not been visited).
    answers["q9_2"] = "Jaccard"
    answers["q9_2_explain"] = (
        "Jaccard focuses on 'yes' matches (locations visited) and ignores 'no' matches, making it "
        "suitable for binary location data where only visited locations are relevant."
    )
    # Which measure, Euclidean distance or correlation coefficient, is most appropriate
    #   to compare two ﬂows in a network traffic. For each ﬂow, we record information
    #   about the number of packets transmitted, number of bytes transferred,
    #   number of acknowledgments sent, and duration of the session.
    answers["q9_3"] = "correlation coefficient"
    answers["q9_3_explain"] = (
        "Correlation is scale-invariant and measures the linear relationship between flows in network traffic, "
        "which is more appropriate than Euclidean distance when comparing patterns or trends."
    )
    # Which measure, Euclidean distance or cosine similarity, is most appropriate to
    #   compare the coordinates of a moving object in a 2-dimensional space. For
    #   example, using GPS data, the object may be located at ($31.4^\circ$ West,
    #   $12.4^\circ$ North)
    answers["q9_4"] = "Euclidean"
    answers["q9_4_explain"] = (
        "Euclidean distance directly measures physical distances in 2D space, making it appropriate "
        "for comparing coordinates of a moving object."
    )
    # Which measure, Euclidean distance or cosine similarity, is most appropriate to
    #   compare the similarity of items bought by customers at a grocery store.
    #   Assume each customer is represented by a 0/1 binary vector of items (where
    #   a 1 means the customer had previously bought the item).
    answers["q9_5"] = "Cosine Similarity"
    answers["q9_5_explain"] = (
        "Cosine similarity focuses on the similarity of patterns (angle between vectors) and is suitable "
        "for comparing binary purchase vectors, especially when the magnitude (number of items) varies."
    )

    return answers


# ----------------------------------------------------------------------
def question10() -> dict:
    
    """Answer question 10."""

    answers = {}

    # Type bool (True or False)

    # Noise is not a problem with count data.
    answers["q10_1"] = False
    answers["q10_1_explain"] = (
        "Noise can still be a problem with count data, as incorrect counts or fluctuations "
        "can impact analyses and lead to misleading results."
    )
    # For any two sets of real values, such as two vectors of size n > 0,
    #   the correlation is a value between -1 and 1.
    answers["q10_2"] = False
    answers["q10_2_explain"] = (
        "Correlation measures the linear relationship between two variables and always lies "
        "between -1 (perfect negative correlation) and 1 (perfect positive correlation)."
    )
    # For reducing the size of a daily time series, it would be better to sample
    #    than aggregate since sampling is a simpler process.
    answers["q10_3"] = False
    answers["q10_3_explain"] = (
        "Aggregation often preserves important trends and patterns in the data, while sampling "
        "may miss critical information and lead to biased results."
    )
    # Noise and outliers are sometimes the same. Explain.
    answers["q10_4"] = True
    answers["q10_4_explain"] = (
        "Noise and outliers can overlap, as both represent deviations from the expected pattern, "
        "though noise is usually random and outliers are extreme values."
    )
    # If an object is an outlier, then it is noise.
    answers["q10_5"] = False
    answers["q10_5_explain"] = (
        "Outliers are not always noise; they can represent valid but rare phenomena, and removing them "
        "without proper justification may lead to biased analyses."
    )
    # A binary attribute with values 0 or 1 is also an asymmetric binary attribute.
    answers["q10_6"] = False
    answers["q10_6_explain"] = (
        "A binary attribute with values 0 and 1 is considered asymmetric binary when one value (e.g., 1) "
        "is more important than the other (e.g., 0)."
    )
    # If vectors of counts have a cosine measure of 1, the objects are identical.
    answers["q10_7"] = False
    answers["q10_7_explain"] = (
        "Cosine similarity of 1 implies the vectors have the same direction, but their magnitudes "
        "may differ, so the objects are not necessarily identical."
    )

    # Discrete variables cannot be ratio.
    answers["q10_8"] = False
    answers["q10_8_explain"] = (
        "Discrete variables can be ratio if they have a meaningful zero point and allow for ratio comparisons, "
        "e.g., the number of items sold."
    )
    # Quantitative variables are continuous.
    answers["q10_9"] = False
    answers["q10_9_explain"] = (
        "Quantitative variables can be either discrete (e.g., counts) or continuous (e.g., weight), "
        "as long as they represent numerical data."
    )
    # Converting ordinal variables to asymmetric binary variables does not lose any information.
    answers["q10_10"] = False
    answers["q10_10_explain"] = (
        "Converting ordinal variables to binary loses information about the ordering and the distances "
        "between categories, which are critical for ordinal data."
    )

    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    answers_dict = {}

    # Create list of functions whose outputs are pickled.
    function_names = ["question" + str(i) for i in range(1, 11)]

    for name in function_names:
        answers_dict[name] = globals()[name]()

    with open("all_questions.pkl", "wb") as fd:
        pickle.dump(answers_dict, fd, protocol=pickle.HIGHEST_PROTOCOL)

# ----------------------------------------------------------------------

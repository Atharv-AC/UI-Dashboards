from db import execute_read, execute_write

#========================================
        # Sreamlit 
#========================================
def average():
    result = execute_read(
        """SELECT AVG(\"math_score\") AS Math, 
        AVG(\"reading_score\") AS Read,
        AVG(\"writing_score\") AS Write
          FROM Students""")
    
    return result

def Gender_analysis():
    result = execute_read(
    """SELECT gender,
        AVG(\"math_score\"),
        AVG(\"reading_score\"),
        AVG(\"writing_score\")
        FROM Students 
        GROUP BY gender;
        """)
    return result


def average_total_score():
    result = execute_read(
        """SELECT AVG(\"total_score\") FROM Students""")
    return result



def top_10_students():
    result = execute_read(
        """SELECT gender, \"math_score\", \"reading_score\", \"writing_score\", \"total_score\"
        FROM Students
        ORDER BY total_score DESC
        LIMIT 10""")
    return result


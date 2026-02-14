from db import execute_read, execute_write
import matplotlib.pyplot as plt

def get_gender_average():
    return execute_read("""
    SELECT gender,
    AVG(\"math_score\"),
    AVG(\"reading_score\"),
    AVG(\"writing_score\")
    FROM Students
    GROUP BY gender                  
    """)


#===============================
        # Streamlit
#===============================
def Chart():
    Achart = execute_read(
        """SELECT AVG(\"math_score\"),
        AVG(\"reading_score\"),
        AVG(\"writing_score\")
        FROM Students
        """)
   

    # math = [mth for mth in Achart]
    # read = [rd for rd in  Achart]
    # write = [w for w in Achart]
    score = [Achart[0][0], Achart[0][1], Achart[0][2]]
    categories = ['Math', 'Reading', 'Writing']

    # plt.bar(categories, score) # takes only two arguments x and y
    # plt.title("Average Student Scores")
    # plt.xlabel("Entities")
    # plt.ylabel("score")
    # plt.tight_layout()
    # plt.savefig(avg_chart)
    # plt.show()
    # plt.close()

    fig, ax = plt.subplots(figsize=(5,3))
    # ax.bar(categories, score )
    ax.bar(categories, score, color=["#4CAF50", "#2196F3", "#FF9800"])
    # Background colors
    fig.patch.set_facecolor("#F1FF98")   # figure background (outside plot)
    ax.set_facecolor("#FFF374")          # plot area background
    ax.set_title("Average Student Scores")
    ax.set_xlabel("Entities")
    ax.set_ylabel("Score")
    return fig


def Mcharts():
    Gchart = get_gender_average()

    scores = [Gchart[0][1], Gchart[1][1]]
    genders = [Gchart[0][0], Gchart[1][0]]


    # plt.bar(genders,scores)
    # plt.title("Gender Comparison -Math")
    # plt.xlabel("Gender")
    # plt.ylabel("Math score")
    # plt.tight_layout()
    # plt.savefig(math_chart)
    # plt.show()
    # plt.close()

    fig, ax = plt.subplots()
    ax.bar(genders, scores,  color=["#A42C1C",  "#1A8410"])
    # Background colors
    fig.patch.set_facecolor("#B3CAFA")   # figure background (outside plot)
    ax.set_facecolor("#AADEFF")          # plot area background
    ax.set_title("Gender Comparison -Math")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Math Score")
    return fig

def Rcharts():
    Gchart = get_gender_average()

    scores = [Gchart[0][2], Gchart[1][2]]
    genders = [Gchart[0][0], Gchart[1][0]]


    # plt.bar(genders,scores)
    # plt.title("Gender Comparison -Reading")
    # plt.xlabel("Gender")
    # plt.ylabel("Reading score")
    # plt.tight_layout()
    # plt.savefig(read_chart)
    # plt.show()
    # plt.close()
    fig, ax = plt.subplots()
    ax.bar(genders, scores, color=["#A42C1C", "#1A8410"])
    # Background colors
    fig.patch.set_facecolor("#FFDEEB")   # figure background (outside plot)
    ax.set_facecolor("#FEDEDE")          # plot area background
    ax.set_title("Gender Comparison -Reading")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Reading Score")
    return fig

def Wcharts():
    Gchart = get_gender_average()

    scores = [Gchart[0][3], Gchart[1][3]]
    genders = [Gchart[0][0], Gchart[1][0]]


    # plt.bar(genders,scores)
    # plt.title("Gender Comparison -Writing")
    # plt.xlabel("Gender")
    # plt.ylabel("Writing score")
    # plt.tight_layout()
    # plt.savefig(write_chart)
    # plt.show()
    # plt.close()

    fig, ax = plt.subplots()
    ax.bar(genders, scores, color=["#A42C1C", "#1A8410"])
    # Background colors
    fig.patch.set_facecolor("#FFEBD7")   # figure background (outside plot)
    ax.set_facecolor("#FFE2E2")          # plot area background
    ax.set_title("Gender Comparison -Writing")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Writing Score")
    return fig

def distributions():
    rows = execute_read(
        """SELECT \"math_score\" FROM Students """)
    
    data_list = [row[0] for row in rows]
        
    # print(data_list)

    # plt.hist(data_list, bins=15)
    # plt.title("Math Score Distribution")
    # plt.xlabel("Score")
    # plt.ylabel("Number of students")
    # plt.grid(axis='y', linestyle='--', alpha=0.4)
    # plt.tight_layout()
    # plt.savefig(Mhisto_chart)
    # plt.show()
    # plt.close()

    fig, ax = plt.subplots()
    ax.hist(data_list, bins=20, color="purple")
    # Background colors
    fig.patch.set_facecolor("#FABFFF")   # figure background (outside plot)
    ax.set_facecolor("#F0C6FD")          # plot area background

    ax.set_title("Math Score Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Number of students")
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    # ax.grid(axis='y', lineStyles='--', alphas=0.4)
    return fig


def Box_plots():
    boxes = execute_read(
        """SELECT \"math_score\", \"reading_score\", \"writing_score\" FROM Students """)
    
    math = [row[0] for row in boxes]
    reading = [row[1] for row in boxes]
    writing = [row[2] for row in boxes]

    # plt.boxplot([math, reading, writing], labels=['Math', 'Reading', 'Writing'])
    # plt.boxplot([math, reading, writing])   # This gives names as 1  2  3
    # plt.title("Box Plot of Scores")
    # plt.ylabel("Score")
    # plt.grid(axis='y', linestyle='--', alpha=0.4)
    # plt.tight_layout()
    # plt.savefig(boxplot)
    # plt.show()
    # plt.close()

    fig, ax = plt.subplots()
    ax.boxplot([math, reading, writing], labels=['Math', 'Reading', 'Writing'])
    # Background colors
    fig.patch.set_facecolor("#CAFA8F")   # figure background (outside plot)
    ax.set_facecolor("#D4FFB3")          # plot area background
    ax.set_title("Box Plot of Scores")
    ax.set_xlabel("Score")
    ax.set_ylabel("Number of students")
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    return fig


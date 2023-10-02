quiz= {
    "question1":{
        "question":"what is the full meaning of IC?",
        "answer":"integrated circuit"
    },

    "question2":{
        "question":"what is the full meaning of AI?",
        "answer":"artificial intelligent"
    },

    "question3":{
        "question":"what is the full meaning of PC?",
        "answer":"personal computer"
    },

    "question4":{
        "question":"what is the full meaning of CD?",
        "answer":"compact disk"
    },

    "question5":{
        "question":"what is the full meaning of CPU?",
        "answer":"central processing unit"
    },

}

count= 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("pls type in your answer ")
    
    if answer == value["answer"]:
        print("correct")
        count += 1
    else:
        print("wrong answer")
        print("")

print("you got " + str(count)+ " out 5")
print(f"and your percentage is {int(count/5*100)}%")
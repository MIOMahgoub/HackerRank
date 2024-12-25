if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
 
    # Initialized a count and total variable
    total = 0
    count = 0
    
    # Utilized for loop to identify how many scores for query_name student
    for score in student_marks[query_name]:
        total += score
        count += 1
    
    # Utilized count and total identified in for loop to output average 
    # with 2 decimal places     
    print(f"{total/count:.2f}")
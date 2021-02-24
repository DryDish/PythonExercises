# Model an organization of employees, management and board of directors in 3 sets.
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
# Management: Tine, Trunte, Rane
# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

#    who in the board of directors is not an employee?
#    who in the board of directors is also an employee?
#    how many of the management is also member of the board?
#    All members of the managent also an employee
#    All members of the management also in the board?
#    Who is an employee, member of the management, and a member of the board?
#    Who of the employee is neither a member or the board or management? """

board_of_directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels" , "Søren"}
management = {"Tine", "Trunte","Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allen", "Stine", "Claus", "James" , "Lars"}

answer = board_of_directors.difference(employees)
print(f"who in the board of directors is not an employee? Answer: {answer}")

answer = employees&(board_of_directors)
print(f"who in the board of directors is also an employee? Answer: {answer}")

answer = len(management&board_of_directors)
print(f"how many of the management is also member of the board? Answer: {answer}")

answer = management&employees
print(f"All members of the managent (that are) also an employee. (<-- im sorry what now?) Answer: {answer}")

answer = management&board_of_directors
print(f"All members of the management (that are) also in the board? Answer: {answer}")

answer = employees&(management & board_of_directors)
print(f"Who is an employee, member of the management, and a member of the board? Answer: {answer}")

answer = employees-management-board_of_directors
print(f"Who of the employee is neither a member o(f) the board (n)or management? Answer: {answer}")
import numpy as np

def input_matrix(name):
    print(f"\nEnter details for Matrix {name}")
    rows = int(input("enter number of rows:")) 
    cols = int(input("enter number of columns:"))
           
    print("Enter elements row-wise for Matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

def display_matrix(title, matrix):
     print("\n{title}:")
     print(matrix)

def matrix_operation():
     while True:
       print("====matrix operation tool======")
       print("1.ADDITION")
       print("2.SUBTRACTION")
       print("3.MULTIPLICATION")
       print("4.TRANSPOSE")
       print("5.DETERMINANT")
       print("6.EXIT")

       choice = input("select an operater (1-6) ")
                      
       try:
            if choice =='1':
                A = input_matrix("A")
                B = input_matrix("B")
                result = A + B
                display_matrix("Result (A + B)", result)

            elif choice == '2':
                A = input_matrix("A")
                B = input_matrix("B")
                result = A - B
                display_matrix("Result (A - B)", result)

            elif choice == '3':
                A = input_matrix("A")
                B = input_matrix("B")
                result = np.dot(A, B)
                display_matrix("Result (A × B)", result)

            elif choice == '4':
                A = input_matrix("A")
                result = A.T
                display_matrix("Transpose of Matrix A", result)

            elif choice == '5':
                A = input_matrix("A")
                det = np.linalg.det(A)
                print(f"\nDeterminant of Matrix A: {det:.2f}")

            elif choice == '6':
                print("\nExiting Matrix Operations Tool. Goodbye!")
                break

            else:
                print("\nInvalid choice! Please select between 1-6.")

       except ValueError:
            print("\nError: Invalid input format.")
       except np.linalg.LinAlgError:
            print("\nError: Determinant not defined for this matrix.")
       except Exception as e:
            print(f"\nUnexpected Error: {e}")


Attempt 1:
Attempted brute force initially with GRE_2.py and realised parsing a SET using JSON involves decoding and encoding custom procedures.

Execute the programs as follows from command prompt
>python GRE_2.py C:\Users\C5232886\Desktop\Python_Prac\GRE\Test

Output of GRE_2.py
"{'files': [{'C:\\\\Users\\\\C5232886\\\\Desktop\\\\Python_Prac\\\\GRE\\\\Test\\\\News.txt', 5915}, {17664, 'C:\\\\Users\\\\C5232886\\\\Desktop\\\\Python_Prac\\\\GRE\\\\Test\\\\ProfilePic.jpeg'}, {124298, 'C:\\\\Users\\\\C5232886\\\\Desktop\\\\Python_Prac\\\\GRE\\\\Test\\\\WebProject.zip'}]}"

Attempt 2:
Attempted writing custom decoder and encoder in GRE_2_FriFinal.py. Output as expected is in string format but unable to show in JSON format.

Execute the programs as follows from command prompt
>python GRE_2_FriFinal.py C:\Users\C5232886\Desktop\Python_Prac\GRE\Test

Output of GRE_2_FriFinal.py
{'files': [{5915, 'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\News.txt'}, {17664, 'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\ProfilePic.jpeg'}, {'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\WebProject.zip', 124298}]}

Attempt 3:
More optimized code

Execute the programs as follows from command prompt
>python GRE_CS_2.py C:\Users\C5232886\Desktop\Python_Prac\GRE\Test

Output of GRE_CS_2.py
{'files': [{5915, 'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\News.txt'}, {17664, 'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\ProfilePic.jpeg'}, {'C:\\Users\\C5232886\\Desktop\\Python_Prac\\GRE\\Test\\WebProject.zip', 124298}]}

Included the Test folder in the repository

Attempt 4: (Final. Please find the code in target_gre_dec_27.py file.)

Exception Management - try, catch #Feedback of Kate and Rasool. This is handled using if, else before
Error Map Dictionary - Error messages are declared as a dictionary and used. Other than declaring in the code, these could be read into the code from a Text file.

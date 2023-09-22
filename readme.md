[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11432870&assignment_repo_type=AssignmentRepo)
# HW. 2 BMI Calculator

You're working in a clinic called and your supervisor ask you to create a program that calculate patient BMI, in order to keep track and record of your patient health, by following the below condition.

- < 18.5, underweight
- 18.5 - 24.9, normal
- 25 - 29.9, overweight
- 30 - 34.9, obese
- 35 <, extremely obese

BMI Fomula:

```python
BMI = Weight in kg/(Height in m)^2
```

<br>

## Development Requirements

Functional Test (50%):

1. Create **bmi_check** function that take 2 parameters, **weight as float** and **height as float**.
2. **bmi_check** need to return **2 values base** on different occasion. correctly provided parameter shall return **result**, **bmi** example “normal”, 23.74, incorrect input shall return **error_info**, **error_code** example: “unrealistic information”, 2
3. The return **result** should return weight status as of, underweight, normal, overweight, obsese, and extremely obsese with its **bmi** score, example: `"normal", 23.74`
4. Unrealistic weight or height should return weight status of “unrealistic information” as **error_info** with **error\_\_code** of 2, example: `"unrealistic information", 2`
5. Any invalid parameter to the function should return “invalid information” as **error_info** with **error_code** of 1, example: `"invalid input", 1`

Application Test (50%):

1. The application should be able to ask for **user name**, **weight** and **height**.
2. Feedback **bmi information** to user based on their input information.
3. Provide an option to **repeat/restart** the application at the end of its bmi calculation.

<br>

### Task: your task is to write Python function that calculate user BMI, and return their BMI result.

<br>

### Instruction:

> - Ask for user input
>   > Input:
>   >
>   > - user's name
>   > - user's weight
>   > - user's height
> - Do a calcualtion by fomula provided above
> - Print output

> - Then display an option **`Y/N`**, for user to whether contiune or stop.

### Expected Output:

- Output: 1
  ![HW_2_BMI_1](resources/HW_2_BMI_1.png)

> If user pick "y" for yes.

- Output: 2
  ![HW_2_BMI_2](resources/HW_2_BMI_2.png)

### HINT:

> - Create 2 files:
>   1. One that contain function for currency [backend]
>   2. The other to ask for user input and calling back function for calculation [frontend]
> - Call the function to the main file.
> - Make use of loop:
>   1. while loop to keep the the program running
>   2. if loop to check for condition
> - Use this Flowchat to help you better understanding of BMI
>   ![HW_2_FC](resources/HW_2_FC.png)

<br><br>

<h1 style="text-align: center;">*** Be Creative ***</h1>

from pyscript import document, display # type: ignore

def adding_numbers(e): #we put e for event holding
    num1= float(document.getElementById("english").value) 
    num2= float(document.getElementById("science").value)
    num3= float(document.getElementById("social_studies").value)
    num4= float(document.getElementById("math").value)
    num5= float(document.getElementById("filipino").value)
    num6= float(document.getElementById("ict").value)   

    result = num1 + num2 + num3 + num4 + num5 + num6 # sum of 6 subjects
    average = result / 6 # to get the average of 6 subjects
    display(average, target="output1") # displays average in output1

    if num1 < 75 or num2 < 75 or num3 < 75 or num4 < 75 or num5 < 75 or num6 < 75: 
        display("You have subjects that need to be retaken.", target="output1") # if grade is less than 75 
        #it will state this
    if num1 >= 75 and num2 >= 75 and num3 >= 75 and num4 >= 75 and num5 >= 75 and num6 >= 75: # if grade passed,
        # meaning greater than 75, it will state this
        display("Congratulations! You passed all your subjects.", target="output1") 




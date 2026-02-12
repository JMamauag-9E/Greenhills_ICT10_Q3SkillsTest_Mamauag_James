from pyscript import display, document

def sign_in(e):
    document.getElementById('output').innerHTML = ' '

    UN = document.getElementById('user').value
    PW = document.getElementById('pass').value
    
    # This is how will the registration look like.
    if len(UN) < 7:
        display(f'Your username should contain at least 7 characters.', target='output') # This will result to this output if it is less than 7 characters
    if len(PW) < 10:
         display(f'Your password should contain at least 10 characters.', target='output') # This will result to this output if it is less than 10 characters
    if not PW.isdigit():
        if PW.isalpha():
            display(f'Your password should include numbers', target='output') # If you put only letters, this will appear.
        else:
            display('Wow! Your officially registered! Welcome!', target='output') # If you complete everything, this will appear.
    else:
        display(f'Your password should include letters', target='output') # # If you put only numbers, this will appear.
    

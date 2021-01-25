def cap_text(text):
    '''
    Input a string
    Output the capitalize string (first letter)
    '''
    #return text.capitalize() # capitalizes the first single letter.
    return text.title() # capitalizes the first letter of every word.

# NOTE: If we use "capitalize()" method above, and run the test_cap.py unittest,
# it will give us an error because it only capitalizes the first letter.
# If we use "title()" method above, we no longer receive errors, because it does capitalize
# all the words, as our unittest test expects (check test_cap.py for the expected result)
 

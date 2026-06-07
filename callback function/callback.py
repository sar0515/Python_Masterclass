# A call back function is a function that you pass as an argument to another function
#so that it can be called (executed) later, usally after some action is completed.


#for exmaple welcome text come after the click the button ,but the welcome text wait for call(click)


def on_button_click(callback):#show_message waiting here to call the fucntion 
    print("button clicked") # print the data 
    callback() #we cal the callback so that waited message will displayed

def show_message():
    print("hello sar welcome!")

on_button_click(show_message)
#we are passing the show_message ,value to on_button_click
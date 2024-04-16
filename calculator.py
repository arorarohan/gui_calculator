import time
import gradio as gr
from playsound import playsound
from helpers import add, subtract, multiply, divide, exponent, nth_root

def calculator(num1, operator, num2):
    if (num1 == None) or (num2 == None):
        return 'enter a number in both fields and try again!'

    if operator == '+':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return add(num1,num2)
    
    elif operator == '-':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return subtract(num1,num2)
    
    elif operator == 'x':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return multiply(num1,num2)
        

    elif operator == '÷':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return divide(num1,num2)
        
    elif operator == '^':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return exponent(num1,num2)
    
    elif operator == '√':
        time.sleep(1)
        playsound('generic_soundfile.mp3',False)
        return nth_root(num1,num2)

demo = gr.Interface(
    #give it our function
    fn=calculator,

    #use Radio for operator buttons
    inputs=[
        'number',
        gr.Radio(['+', '-', 'x', '÷', '^', '√']),
        'number'
        ],

    outputs = ['text'],
    clear_btn = 'clear',
    submit_btn='=',
    title= 'Zohandoggo funky calculator',
    allow_flagging='never',
    concurrency_limit=None
)

demo.launch()
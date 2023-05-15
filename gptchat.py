from ttkbootstrap import * 
import tkinter as tk 
import openai 


# Setting up openai api

openai.api_key = 'Enter Your API'  
messages = [{"role": "system", "content": "You are a coading experts that specializes in coding and solve any coding problem"}]


app = Window('Tech AI','superhero')
app.geometry('600x500+0+0')

Label(app,text='Tech AI',font=('Helvertica',25)).pack()
Separator(app).pack(fill=X)

outputs = []

# Setting ChatGpt Bot Ai =========================

def CustomChatGPT(user_input):

    messages.append({"role": "user", "content": user_input}) 
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages = messages) 
    ChatGPT_reply = response["choices"][0]["message"]["content"] 
    messages.append({"role": "assistant", "content": ChatGPT_reply}) 
    outputs.append(ChatGPT_reply) 


# Responce ========================================
def responce():
    prompts = prompt.get()
    prompt.delete(0,END)
    prompt.config(state='disabled')
    prompt_enter.config(state='disabled')
    CustomChatGPT(prompts)
    frame.config(state='normal')
    frame.insert(END,f"You : {prompts} \n")
    for i in outputs:
        frame.insert(END,f"Tech AI :\n{i} \n\n")
    frame.config(state='disabled')
    prompt.config(state='normal')
    prompt_enter.config(state='normal')
    outputs.clear()
# OutPut Frame ==================______--------------

output_frame = Frame(app)
output_frame.pack(fill=BOTH,expand=True,padx=(10,10),pady=(10,0))

# Create a Canvas widget with a scrollbar
canvas = Canvas(output_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

frame = Text(canvas,width=90,height=25,state='disabled')
scrollbar = Scrollbar(output_frame, command=frame.yview)
scrollbar.pack(side=RIGHT, fill=Y)

frame.configure(yscrollcommand=scrollbar.set)
frame.pack()

# Prompt Frame ===========================

prompt_frame = Frame(app)
prompt_frame.pack(side=BOTTOM,fill=X,padx=(10,10),pady=(10,20))

prompt = Entry(prompt_frame,width=80)
prompt.pack(side=LEFT,fill=X)

prompt_enter = Button(prompt_frame,text='Enter',command=responce)
prompt_enter.pack(side=RIGHT)

app.bind('<Return>',lambda e:responce())


app.mainloop()
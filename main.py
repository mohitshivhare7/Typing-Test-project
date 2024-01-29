from tkinter import * #importing all the classes and methods of tkinter module
import random
root=Tk()
root.geometry("940x735+200+10")
root.resizable(0,0)

mainframe=Frame(root,bd=4)
mainframe.grid()

titleframe=Frame(mainframe,bg="orange")
titleframe.grid()

titleLabel=Label(titleframe,text="Mastertyping",font=("algerian",28,"bold"),bg="goldenrod3",fg="white",width=38,bd=10)
titleLabel.grid(pady=5)


paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=["My best friend is my classmate at school. She and I have been studying together since we entered school in kindergarten. We have studied together all these years. We also travel by the school bus together because we stay close to each other. Her home is only a ten minute walk from my place."

" My friend is kindly and sweet-natured. We are always happy to be with each other. We enjoy studying, playing and eating together. If I am sad she will do all she can to make me smile and feel happy."

" She has always been kind and helpful to me. When I miss school because I am unwell she comes to my place to share with me all that has been done at school. When she misses school I too help her with all that has been covered at school. We also play badminton together in the evenings."]

random.shuffle(paragraph_list)

label_paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=("arial",14,"bold"))


textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea=Text(textarea_frame,font=("arial",12,"bold"),width=90,height=7,bd=8,relief=GROOVE,wrap="word",state=DISABLED)
textarea.grid()

frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text="Elapsed Time",font=("Tahoma",12,"bold"),fg="red")
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text="Remaining Time",font=("Tahoma",12,"bold"),fg="red")
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text="60",font=("Tahoma",12,"bold"))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_time_label=Label(frame_output,text="WPM",font=("Tahoma",12,"bold"),fg="red")
wpm_time_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"))
wpm_count_label.grid(row=0,column=5,padx=5)

totalwords_time_label=Label(frame_output,text="Total Words",font=("Tahoma",12,"bold"),fg="red")
totalwords_time_label.grid(row=0,column=6,padx=5)

totalwords_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"))
totalwords_count_label.grid(row=0,column=7,padx=5)

wrongwords_time_label=Label(frame_output,text="Wrong Words",font=("Tahoma",12,"bold"),fg="red")
wrongwords_time_label.grid(row=0,column=8,padx=5)

wrongwords_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"))
wrongwords_count_label.grid(row=0,column=9,padx=5)

button_Frame=Frame(mainframe)
button_Frame.grid(row=4,column=0)

startButton=Button(button_Frame,text="Start")
startButton.grid(row=0,column=0)

resetButton=Button(button_Frame,text="Reset")
resetButton.grid(row=0,column=1)

exitButton=Button(button_Frame,text="Exit")
exitButton.grid(row=0,column=2)

label_paragraph.grid(row=0,column=0)
root.mainloop()

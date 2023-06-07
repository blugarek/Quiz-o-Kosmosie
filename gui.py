import tkinter as tk
from tkinter import messagebox
import random


class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.current_question = 0
        self.score = 0

        self.questions = [
            {
                'question': 'Ile planet jest w układzie słonecznym?',
                'answers': ['5', '6', '8', '9'],
                'correct_answer': '8'
            },
            {
                'question': 'Jaka planeta jest najbliżej Ziemii?',
                'answers': ['Wenus', 'Księżyc', 'Jowisz', 'Uran'],
                'correct_answer': 'Wenus'
            },
            {
                'question': 'Co to Pas Kuipera?',
                'answers': ['Pas asteroid', 'Pierścień Saturna', 'Obszar wokół Słońca złożony z planet karłowatych i innych małych ciał', 'Grupa gwiazd tworzących konstelację'],
                'correct_answer': 'Obszar wokół Słońca złożony z planet karłowatych i innych małych ciał'
            },
            {
                'question': 'W ilu procentach wszechświat składa się z hipotetycznej ciemnej materii?',
                'answers': ['0,08%', '26,8%', '41,7%', '78,1%'],
                'correct_answer': '26,8%'
            },
            {
                'question': 'Czym jest Supernowa?',
                'answers': ['Eksplozja gwiazdy, która może być chwilowo jaśniejsza niż cała galaktyka', 'Zjawisko optyczne występujące w pobliżu równika Ziemi', 'Efekt, w którym długotrwałe zaćmienie Księżyca spowodowane przez cień Ziemi', 'Nazwa grupy gwiazd składających się z gwiazd podwójnych'],
                'correct_answer': 'Eksplozja gwiazdy, która może być chwilowo jaśniejsza niż cała galaktyka'
            },
            {
                'question': 'Ile lat temu powstał wszechświat?',
                'answers': ['14.72 miliona', '28.1 bilionów', '13.8 miliarda', '189,83 tysięce'],
                'correct_answer': '13.8 miliarda'
            },
            {
                'question': 'Co to jest Paradoks Fermiego?',
                'answers': ['Teoria mówiąca o istnieniu życia pozaziemskiego we wszechświecie', 'Hipoteza zakładająca, że kosmici ukrywają się przed ludzkością',
                            'Zagadnienie dotyczące pytania, dlaczego nie napotykamy na widoczne oznaki istnienia obcych cywilizacji',
                            'Koncepcja dotycząca możliwości podróży międzygwiezdnych'],
                'correct_answer': 'Zagadnienie dotyczące pytania, dlaczego nie napotykamy na widoczne oznaki istnienia obcych cywilizacji'
            },
            {
                'question': "Co to jest równanie Drake'a?",
                'answers': ['Matematyczna formuła szacująca liczbę zaawansowanych cywilizacji w naszej galaktyce', 'Model opisujący ruch planet wokół gwiazd', 'Algorytm do przeliczania odległości międzyplanetarnych', 'Teoria wyjaśniająca powstanie planetarnej atmosfery'],
                'correct_answer': 'Matematyczna formuła szacująca liczbę zaawansowanych cywilizacji w naszej galaktyce'
            },
            {
                'question': 'Czym jest Supermasywna Czarna Dziura?',
                'answers': ['Czarna dziura powstała w wyniku kolapsu masywnych gwiazd',
                            'Czarna dziura, która pochłania światło i inne materie w jej otoczeniu',
                            'Ekstremalnie gęste i potężne czarne dziury obecne w centrach galaktyk',
                            'Czarna dziura występująca na skraju wszechświata'],
                'correct_answer': 'Ekstremalnie gęste i potężne czarne dziury obecne w centrach galaktyk'
            },
            {
                'question': 'Jakie są dwie główne grupy gwiazd na diagramie Hertzsprunga-Russella?',
                'answers': ['Gwiazdy nadolbrzymy i białe olbrzymy', 'Gwiazdy ciągu głównego i białe karły', 'Czerwone olbrzymy i białe karły', 'Gwiazdy ciągu głównego i błękitne nadolbrzymy'],
                'correct_answer': 'Gwiazdy ciągu głównego i błękitne nadolbrzymy'
            },
        ]

        random.shuffle(self.questions)

        self.background_image = tk.PhotoImage(file='Bez tytułu.png')
        self.canvas = tk.Canvas(master, width=1920, height=1080, highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.canvas.pack()

        frame = tk.Frame(master, bg='black', width=800, height=600, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.question_label = tk.Label(frame, text='', font=('Times New Roman', 20, 'bold'), wraplength=600, bg='black',
                                       fg='white')
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(frame, text='', command=lambda i=i: self.check_answer(i),
                               font=('Times New Roman', 16, 'bold'),
                               width=40, height=2, bg='black', fg='white', bd=2, relief=tk.RAISED)
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.next_question()

    def reset_buttons(self):
        for button in self.answer_buttons:
            button.config(bg='black')

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data['question'])

            answers = question_data['answers']
            random.shuffle(answers)

            max_answer_width = max(len(answer) for answer in answers)
            for i, button in enumerate(self.answer_buttons):
                button.config(text=answers[i], width=max_answer_width, state=tk.NORMAL, bg='black')

            self.current_question += 1
        else:
            self.show_results()

    def check_answer(self, answer_index):
        question_data = self.questions[self.current_question - 1]
        selected_answer = question_data['answers'][answer_index]

        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)

        if selected_answer == question_data['correct_answer']:
            self.score += 1
            self.answer_buttons[answer_index].config(bg='green')
        else:
            self.answer_buttons[answer_index].config(bg='red')

        self.master.after(1000, self.reset_buttons)

    def show_results(self):
        messagebox.showinfo('Wyniki', f'Twój wynik: {self.score}/{len(self.questions)}')
        self.master.quit()


root = tk.Tk()
root.attributes('-fullscreen', True)
quiz = QuizGUI(root)
root.mainloop()
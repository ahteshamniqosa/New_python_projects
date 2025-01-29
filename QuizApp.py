import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.root.geometry("500x700")
        self.root.config(bg='#000')

        self.questions = [
            {
                'question': 'Question 1: What is the purpose of the <!DOCTYPE> declaration in HTML?',
                'options': ['To define the HTML version being used', 'To specify the language of the page', 'To link external resources', 'To add metadata to the document'],
                'answer': 'To define the HTML version being used'
            },
            {
                'question': 'Question 2: Which CSS property is used to control the spacing between lines of text?',
                'options': ['margin', 'padding', 'line-height', 'font-size'],
                'answer': 'line-height'
            },
            {
                'question': 'Question 3: In React, what is the purpose of the useEffect hook?',
                'options': ['To store component states', 'To handle side effects like data fetching', 'To manage component props', 'To trigger a re-render of the component'],
                'answer': 'To handle side effects like data fetching'
            },
            {
                'question': 'Question 4: What is the primary benefit of using Vue\'s v-model directive?',
                'options': ['Two-way data binding', 'One-way data binding', 'Component rendering optimization', 'Event handling'],
                'answer': 'Two-way data binding'
            },
            {
                'question': 'Question 5: In Next.js, which function is used to fetch data on the server side before rendering a page?',
                'options': ['getServerSideProps', 'useEffect', 'getStaticProps', 'fetchData'],
                'answer': 'getServerSideProps'
            },
            {
                'question': 'Question 6: How can you make a webpage responsive in CSS?',
                'options': ['By using absolute positioning', 'By using media queries', 'By using the float property', 'By setting a fixed width'],
                'answer': 'By using media queries'
            },
            {
                'question': 'Question 7: Which of the following is true about React components?',
                'options': ['Components are only functions', 'Components are only classes', 'Components can be either functions or classes', 'React components do not render anything'],
                'answer': 'Components can be either functions or classes'
            },
            {
                'question': 'Question 8: What is the main difference between v-if and v-show in Vue.js?',
                'options': ['v-if is used for conditional rendering, v-show is used for hiding elements', 'v-if renders the element immediately, v-show does not', 'v-if does not affect the DOM, v-show does', 'v-if is used for event handling, v-show for rendering'],
                'answer': 'v-if is used for conditional rendering, v-show is used for hiding elements'
            },
            {
                'question': 'Question 9: Which of the following methods is used in Next.js for static site generation?',
                'options': ['getServerSideProps', 'getStaticPaths', 'getStaticProps', 'getServerStatic'],
                'answer': 'getStaticProps'
            },
            {
                'question': 'Question 10: What is the correct syntax for embedding an external CSS file into an HTML document?',
                'options': ['<link rel="stylesheet" href="styles.css">', '<style href="styles.css"></style>', '<css src="styles.css"></css>', '<script href="styles.css"></script>'],
                'answer': '<link rel="stylesheet" href="styles.css">'
            }
        ]

        self.current_question = 0
        self.correct_answers = 0
        self.user_answers = []

        self.question_label = tk.Label(root, text=self.questions[self.current_question]['question'], font=("Arial", 16, 'bold'), fg='white', bg='#000')
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text=self.questions[self.current_question]['options'][i], 
                            width=80, height=2, font=("Arial", 14), 
                            bg='#16D1D3', fg='#000', activebackground='#00c3ff', relief="flat",
                            command=lambda i=i: self.store_answer(i))
            btn.pack(pady=10)

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00c3ff"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#16D1D3"))
            btn.bind("<ButtonPress>", lambda e, b=btn: b.config(bg="#00526a"))
            btn.bind("<ButtonRelease>", lambda e, b=btn: b.config(bg="#00c3ff"))

            self.option_buttons.append(btn)

    def store_answer(self, option_index):
        selected_option = self.questions[self.current_question]['options'][option_index]
        self.user_answers.append(selected_option)
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.load_next_question()
        else:
            self.show_result()

    def load_next_question(self):
        self.question_label.config(text=self.questions[self.current_question]['question'])
        for i in range(4):
            self.option_buttons[i].config(text=self.questions[self.current_question]['options'][i])

    def show_result(self):
        self.correct_answers = sum(1 for i in range(10) if self.user_answers[i] == self.questions[i]['answer'])
        if self.correct_answers >= 7:
            messagebox.showinfo("Result", f"You are clear for this interview! Correct Answers: {self.correct_answers}/10")
        else:
            messagebox.showinfo("Result", f"You are not eligible enough, you have time to improve more. Correct Answers: {self.correct_answers}/10")
            
        result_window = tk.Toplevel(self.root)
        result_window.title("Detailed Results")
        result_window.geometry("500x700")
        result_window.config(bg='#000')

        for i in range(10):
            question_frame = tk.Frame(result_window, bg='#000')
            question_frame.pack(fill="x", padx=10, pady=5)

            question_text = tk.Label(question_frame, text=f"Q{i+1}: {self.questions[i]['question']}", font=("Arial", 12, 'bold'), fg='white', bg='#000')
            question_text.pack()

            user_answer = self.user_answers[i]
            correct_answer = self.questions[i]['answer']

            answer_label = tk.Label(question_frame, text=f"Your answer: {user_answer} (Correct: {correct_answer})", font=("Arial", 12), fg='white', bg='#000')
            answer_label.pack()

            if user_answer == correct_answer:
                answer_label.config(fg="#2AD708")
            else:
                answer_label.config(fg="red")

root = tk.Tk()
app = QuizApp(root)

root.mainloop()

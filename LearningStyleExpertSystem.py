class LearningStyleExpertSystem:
    def __init__(self):
        self.visual_score = 0
        self.auditory_score = 0
        self.kinesthetic_score = 0

    def ask_questions(self):
        print("Answer the following questions with 'yes' or 'no'.")
        
        # Questions related to visual learning style
        visual_questions = [
            "Do you prefer to learn through diagrams, charts, or visual aids?",
            "Do you often take notes during a lecture or presentation?",
            "Do you find it easy to remember visual details of things you see?",
            "Do you use mind maps or sketches when studying?"
        ]

        for question in visual_questions:
            response = input(question + " ")
            if response.lower() == "yes":
                self.visual_score += 1

        # Questions related to auditory learning style
        auditory_questions = [
            "Do you prefer learning by listening to lectures or discussions?",
            "Do you learn better by hearing explanations rather than reading?",
            "Do you prefer podcasts or audio recordings over reading material?",
            "Do you find it easy to remember what you hear in conversations?"
        ]

        for question in auditory_questions:
            response = input(question + " ")
            if response.lower() == "yes":
                self.auditory_score += 1

        # Questions related to kinesthetic learning style
        kinesthetic_questions = [
            "Do you prefer hands-on activities or physical involvement while learning?",
            "Do you enjoy learning through experiments or physical trials?",
            "Do you find it difficult to stay still for long periods during study?",
            "Do you remember better when you engage in physical activities?"
        ]

        for question in kinesthetic_questions:
            response = input(question + " ")
            if response.lower() == "yes":
                self.kinesthetic_score += 1

    def identify_learning_style(self):
        # Determine the learning style based on the scores
        if self.visual_score >= self.auditory_score and self.visual_score >= self.kinesthetic_score:
            return "Visual"
        elif self.auditory_score >= self.visual_score and self.auditory_score >= self.kinesthetic_score:
            return "Auditory"
        else:
            return "Kinesthetic"

    def suggest_learning_content(self, learning_style):
        # Suggest suitable content based on the identified learning style
        if learning_style == "Visual":
            return "Suggested Content: Diagrams, Mind Maps, Infographics, Videos"
        elif learning_style == "Auditory":
            return "Suggested Content: Podcasts, Audio Lectures, Recorded Discussions"
        else:
            return "Suggested Content: Hands-on Activities, Physical Simulations, Experiment-based Learning"

    def run(self):
        # Run the expert system
        self.ask_questions()
        learning_style = self.identify_learning_style()
        print(f"\nYour preferred learning style is: {learning_style}")
        content = self.suggest_learning_content(learning_style)
        print(content)

# Run the expert system
if __name__ == "__main__":
    system = LearningStyleExpertSystem()
    system.run()

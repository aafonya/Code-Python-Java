from peewee import *
from models.applicant import Applicant
from models.mentor import Mentor
from models.answer import Answer
from models.question import Question


class ControllerMentor():
    'Mentors Controller'

    @staticmethod
    def mentor_interview_details(username):
        result = []
        mentor = Mentor.select().where(
            Mentor.user_name == username).get()
        slots = mentor.interviewslot_list
        for i in range(len(slots)):
            if slots[i].reserved == True:
                interview = slots[i].slot_list
                applicant = interview[0].applicant
                result.append(
                    [str(
                        slots[i].start), str(
                        slots[i].end), str(applicant.application_code),
                        applicant.first_name + " " + applicant.last_name])
        return result

    @staticmethod
    def mentor_question_details(username):

        try:
            mentor_id = Mentor.select(Mentor.id).where(
                Mentor.user_name == username).get()
            questions = Answer.select(Answer.question_id).where(
                Answer.mentor_id == mentor_id.id)

            question_list = []
            for i in questions:
                question_list.append(i.question_id)

            result = []
            for i in question_list:
                query = Question.select(Question.id, Question.question_date, Question.question_name, Applicant.id).join(
                    Applicant).where((Question.question_status == 'waiting for answer') & (Question.id == i))
                for i in query:
                    result.append(
                        [str(i.id), str(i.question_date), i.question_name, str(i.applicant.id)])

        except DoesNotExist:
            return "There is no question, please come back later!"

        return result

    @staticmethod
    def mentor_accept_questions():
        user_choice = input(
            '\nYou have these questions!\nWhich one do you want to answer? Please enter an id number! ')
        user_answer = input('\nPlease type in your answer! ')
        try:
            answers = Answer.select().where(
                Answer.question_id == user_choice).get()
            answers.answer_name = str(user_answer)
            answers.save()

            query = Question.select().where(
                (Question.question_status == 'waiting for answer') & (Question.id == user_choice)).get()
            query.question_status = 'answered'
            query.save()
        except:
            print("Wrong input! Please try again!")

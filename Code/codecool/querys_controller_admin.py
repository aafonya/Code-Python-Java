from models.applicant import Applicant
from models.city import City
from models.mentor import Mentor
from models.school import School
from models.interview import Interview
from models.interviewslot import InterviewSlot
from peewee import *


class ControllerAdmin():
    'Controller Admin'

    @staticmethod
    def admin_interview_filter(filter_name, filter_input):
        filter_list = ["school", "applicant", "mentor", "date"]
        query = None
        output = [["School name", "Application code",
                   "Mentor name", "Start date"]]
        if filter_name in filter_list:
            query = Interview.select().join(InterviewSlot).switch(
                Interview).join(Applicant).join(City).join(School)
            if filter_name == "applicant":
                query = query.select().where(
                    Applicant.first_name == filter_input)
            if filter_name == "mentor":
                query = query.select().where(
                    Mentor.first_name == filter_input).get()
            if filter_name == "date":
                query = query.select().where(
                    InterviewSlot.start == filter_input).get()
            if filter_name == "school":
                query = query.select().where(School.school_name == filter_input)

                # query = Interview.select().join(InterviewSlot).switch(
                # Interview).join(Applicant).join(City).join(School).where(School.school_name
                # == filter_input)

                # query = InterviewSlot.select().join(Interview).join(
                # Applicant).join(City).join(School)  # .where(
                # School.school_name == filter_input).get()
            for i in query:
                mentor_name = i.interview_slot.mentor.first_name + \
                    " " + i.interview_slot.mentor.last_name
                output.append([i.applicant.city.school_id.school_name,
                               i.applicant.application_code, mentor_name,
                               str(i.interview_slot.start)])
        return output

    @staticmethod
    def admin_get_filters(user_name):
        try:
            list_options = ['exit', 'application_status', 'original_city',
                            'first_name', 'last_name', 'email', 'school', 'mentor_name']
            for i in range(len(list_options)):
                print("(" + str(i) + ") " + list_options[i])
            input_option = input("Please enter a number")
            if input_option != '0':
                filter_input = input(
                    'Please enter ' + list_options[int(input_option)] + ' !')
                filter_name = list_options[int(input_option)]
                return ControllerAdmin.admin_get_filtered_list(filter_name, filter_input)
            elif input_option == '0':
                return [['', '', '', '', '', '']]
        except:
            print("Not in database, try again!")
            return [['', '', '', '', '', '']]

    @staticmethod
    def admin_get_filtered_list(filter_name, filter_input):
        applicants = None
        applicants_table = []
        app_filter = ['application_status',
                      'original_city', 'first_name', 'last_name', 'email']
        if filter_name in app_filter:
            applicants = Applicant.select().where(
                getattr(Applicant, filter_name) == filter_input)
            applicants_table = ControllerAdmin.convert_query_to_table(
                applicants)
        elif filter_name == 'school':
            school_filt = School.select().where(
                School.school_name == filter_input)
            city_filt = City.select().where(
                City.school_id == school_filt[0].id)
            applicants = city_filt[0].applicant_list
            applicants_table = ControllerAdmin.convert_query_to_table(
                applicants)
        elif filter_name == 'mentor_name':
            applics = []
            mentors_list = Mentor.select().where(
                Mentor.first_name == filter_input)
            interviewslotlist = mentors_list[0].interviewslot_list
            for i in interviewslotlist:
                slots = i.slot_list
                for j in slots:
                    x = Applicant.select().where(j.id == Applicant.id)
                    applics.append(x)
            print(len(applics))
            applicants_table = ControllerAdmin.convert_list_to_table(applics)
        applicants_table.insert(
            0, ["First name", "Last name", "Application Status", "Original City", "Email", "Username"])
        return applicants_table

    @staticmethod
    def convert_list_to_table(applicant_list):
        converted_applicant_list = []
        counter = -1
        for i in applicant_list:
            converted_applicant_list.append('')
            for j in i:
                counter += 1
                converted_applicant_list[
                    counter] = [j.first_name, j.last_name, j.application_status, j.original_city, j.email,
                                j.user_name]
        return converted_applicant_list

    @staticmethod
    def convert_query_to_table(query):
        final_list = []
        i = -1
        for j in query:
            final_list.append('')
            i += 1
            final_list[i] = [j.first_name, j.last_name,
                             j.application_status, j.original_city, j.email, j.user_name]
        return final_list

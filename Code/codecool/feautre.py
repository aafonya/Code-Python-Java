
@staticmethod
def details_for_email_to_appl(applicant_name):

    applicant = Applicant.select().where(
        Applicant.user_name == applicant_name).get()

    applicants_email = applicant.email

    mentors_name = applicant.interview.interviewslot.mentor

    interviewslot_id = applicant.interview.interviewslot
    interviewslot = Interviewslot.select().where(
        InterviewSlot.id == interviewslot).get()
    timeslot = [interviewslot.start, interviewslot.end]

    details = [applicants_email, applicant_name, mentors_name, timeslot]

    return details


@staticmethod
def email_to_appl_intwslot(applicant_name):
    recipient = details_for_email_to_appl(applicant_name)[0]
    subject = "Message about Interview date"
    body = "Dear {}, we kindly inform you about the date of your interview. It will be held:
        {} Your assigned mentors name is {}.format(details_for_email_to_appl[1], details_for_email_to_appl[3], details_for_email_to_appl[2])

    email_appl_intw = [recipient, subject, body]

    return email_appl_intw

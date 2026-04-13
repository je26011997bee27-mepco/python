class Doctors:
    def _init_(self,doc_id,doc_name,spec_id,treat_id):
        self.doctor_id=doc_id
        self.doctor_name=doc_name
        self.special_id=spec_id
        self.treatment_id=treat_id
    def get_doctor_id(self):
        return self.doctor_id

class patients:
    def _init_(self,pat_id,pat_name,doc_id,treat_id):
        self.patient_id=pat_id
        self.patient_name=pat_name
        self.doctor_id=doc_id
        self.treatment_id=treat_id
    def get_patient(self):
        return self.patient_id

class specialization:
    def _init_(self,spec_id,spec):
        self.specialization_id=spec_id
        self.specialization=spec
    def get_specialization(self):
        return self.specialization_id

class treatements:
    def _init_(self,treat_id,treat):
        self.treatement_id=treat_id
        self.treatement=treat
    def get_treatement_id(self):
        return self.treatement_id

class status:
    def _init_(self,status_id,status):
        self.status_id=status_id
        self.status=status
    def get_treatement_id(self):
        return self.status_id

class report:
    def _init_(self,doc_id,_name,patient_id,treat_id,status_id):
        self.doctor_id=doc_id
        self.doctor_name=doc_name
        self.special_id=spec_id
        self.treatment_id=treat_id
    def get_doctor_id(self):
        return self.doctor_id
    
class hospital:
    def _init_(self):
        self.doctors=[]
        self.patients=[]
    def add_doctor(self,doctor):
        self.doctor.append(doctor)
    def add_patient(self,patient):
        self.patients.append(patients)
        
